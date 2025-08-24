#!/bin/bash

# Deploy Gen AI RAG LangChain to AWS ECS
set -e

# Configuration
AWS_REGION=${AWS_DEFAULT_REGION:-us-east-1}
ECR_REPOSITORY=${ECR_REPOSITORY:-gen-ai-rag-langchain}
ECS_CLUSTER=${ECS_CLUSTER_NAME:-gen-ai-rag-cluster}
ECS_SERVICE=${ECS_SERVICE_NAME:-gen-ai-rag-service}
ECS_TASK_DEFINITION=${ECS_TASK_DEFINITION:-gen-ai-rag-task}

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if AWS CLI is installed
if ! command -v aws &> /dev/null; then
    log_error "AWS CLI is not installed. Please install it first."
    exit 1
fi

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    log_error "jq is not installed. Please install it first."
    exit 1
fi

# Get AWS account ID
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
if [ -z "$ACCOUNT_ID" ]; then
    log_error "Failed to get AWS account ID. Check your AWS credentials."
    exit 1
fi

log_info "Deploying to AWS Account: $ACCOUNT_ID"
log_info "Region: $AWS_REGION"
log_info "ECR Repository: $ECR_REPOSITORY"
log_info "ECS Cluster: $ECS_CLUSTER"
log_info "ECS Service: $ECS_SERVICE"

# Update task definition with account ID
TASK_DEF_FILE="deployment/task-definition.json"
TEMP_TASK_DEF_FILE="deployment/task-definition-temp.json"

log_info "Updating task definition with account ID..."
sed "s/ACCOUNT_ID/$ACCOUNT_ID/g" "$TASK_DEF_FILE" > "$TEMP_TASK_DEF_FILE"

# Register new task definition
log_info "Registering new task definition..."
NEW_TASK_DEFINITION=$(aws ecs register-task-definition \
    --cli-input-json file://"$TEMP_TASK_DEF_FILE" \
    --region "$AWS_REGION" \
    --query 'taskDefinition.taskDefinitionArn' \
    --output text)

if [ -z "$NEW_TASK_DEFINITION" ]; then
    log_error "Failed to register task definition"
    rm -f "$TEMP_TASK_DEF_FILE"
    exit 1
fi

log_info "New task definition registered: $NEW_TASK_DEFINITION"

# Update service with new task definition
log_info "Updating ECS service..."
aws ecs update-service \
    --cluster "$ECS_CLUSTER" \
    --service "$ECS_SERVICE" \
    --task-definition "$NEW_TASK_DEFINITION" \
    --region "$AWS_REGION" \
    --force-new-deployment > /dev/null

# Wait for service to become stable
log_info "Waiting for service to become stable..."
aws ecs wait services-stable \
    --cluster "$ECS_CLUSTER" \
    --services "$ECS_SERVICE" \
    --region "$AWS_REGION"

# Get service status
SERVICE_STATUS=$(aws ecs describe-services \
    --cluster "$ECS_CLUSTER" \
    --services "$ECS_SERVICE" \
    --region "$AWS_REGION" \
    --query 'services[0].status' \
    --output text)

RUNNING_COUNT=$(aws ecs describe-services \
    --cluster "$ECS_CLUSTER" \
    --services "$ECS_SERVICE" \
    --region "$AWS_REGION" \
    --query 'services[0].runningCount' \
    --output text)

DESIRED_COUNT=$(aws ecs describe-services \
    --cluster "$ECS_CLUSTER" \
    --services "$ECS_SERVICE" \
    --region "$AWS_REGION" \
    --query 'services[0].desiredCount' \
    --output text)

log_info "Service Status: $SERVICE_STATUS"
log_info "Running Tasks: $RUNNING_COUNT/$DESIRED_COUNT"

# Clean up temp file
rm -f "$TEMP_TASK_DEF_FILE"

if [ "$SERVICE_STATUS" = "ACTIVE" ] && [ "$RUNNING_COUNT" = "$DESIRED_COUNT" ]; then
    log_info "Deployment completed successfully!"
    
    # Get load balancer URL if available
    LB_DNS=$(aws ecs describe-services \
        --cluster "$ECS_CLUSTER" \
        --services "$ECS_SERVICE" \
        --region "$AWS_REGION" \
        --query 'services[0].loadBalancers[0].targetGroupArn' \
        --output text 2>/dev/null || echo "")
    
    if [ "$LB_DNS" != "" ] && [ "$LB_DNS" != "None" ]; then
        log_info "Service is accessible via load balancer"
    else
        log_info "Service is running without load balancer"
    fi
    
    exit 0
else
    log_error "Deployment failed. Check ECS console for details."
    exit 1
fi
