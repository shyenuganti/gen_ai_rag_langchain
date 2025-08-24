"""Command line interface."""

import argparse
import sys
from typing import Optional

from gen_ai_rag_langchain.config import get_config
from gen_ai_rag_langchain.core import RAGSystem


def main(args: Optional[list] = None) -> int:
    """Main CLI entry point.
    
    Args:
        args: Command line arguments (for testing)
        
    Returns:
        Exit code
    """
    parser = argparse.ArgumentParser(
        description="Gen AI RAG LangChain CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0",
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Query command
    query_parser = subparsers.add_parser("query", help="Process a query")
    query_parser.add_argument("text", help="Query text to process")
    query_parser.add_argument(
        "--max-tokens", type=int, default=4000, help="Maximum tokens in response"
    )
    query_parser.add_argument(
        "--temperature", type=float, default=0.7, help="Temperature for generation"
    )
    
    # Server command
    server_parser = subparsers.add_parser("server", help="Start the API server")
    server_parser.add_argument(
        "--host", default="0.0.0.0", help="Host to bind to"
    )
    server_parser.add_argument(
        "--port", type=int, default=8000, help="Port to bind to"
    )
    server_parser.add_argument(
        "--reload", action="store_true", help="Enable auto-reload"
    )
    
    # Health check command
    health_parser = subparsers.add_parser("health", help="Check system health")
    
    # Parse arguments
    parsed_args = parser.parse_args(args)
    
    if not parsed_args.command:
        parser.print_help()
        return 1
    
    # Initialize components
    config = get_config()
    rag_system = RAGSystem(config.__dict__)
    
    try:
        if parsed_args.command == "query":
            result = rag_system.process_query(parsed_args.text)
            print(f"Query: {result['query']}")
            print(f"Response: {result['response']}")
            print(f"Sources: {result['sources']}")
            print(f"Metadata: {result['metadata']}")
            
        elif parsed_args.command == "server":
            import uvicorn
            from gen_ai_rag_langchain.api import app
            
            uvicorn.run(
                app,
                host=parsed_args.host,
                port=parsed_args.port,
                reload=parsed_args.reload,
            )
            
        elif parsed_args.command == "health":
            health_status = rag_system.health_check()
            print(f"Status: {health_status['status']}")
            print(f"Version: {health_status['version']}")
            
        return 0
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
