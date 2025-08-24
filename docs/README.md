# Enabling GitHub Pages

To enable GitHub Pages for this project:

## Quick Setup

1. **Push to GitHub** (if not already done):
   ```bash
   git add .
   git commit -m "Add GitHub Pages website"
   git push origin main
   ```

2. **Enable GitHub Pages**:
   - Go to your repository on GitHub
   - Click on **Settings** tab
   - Scroll down to **Pages** section
   - Under **Source**, select **Deploy from a branch**
   - Choose **main** branch and **/ (root)** folder
   - Click **Save**

3. **Configure for docs folder** (recommended):
   - Change the source to **main** branch and **/docs** folder
   - This uses the website files in the `docs/` directory

4. **Access your website**:
   - Your site will be available at: `https://shyenuganti.github.io/gen_ai_rag_langchain/`
   - It may take a few minutes to deploy initially

## Custom Domain (Optional)

If you have a custom domain:

1. Add a `CNAME` file in the `docs/` directory with your domain
2. Configure DNS settings with your domain provider
3. Enable HTTPS in repository settings

## Website Features

The generated website includes:

### 🎯 **Comprehensive Landing Page**
- Modern, responsive design with dark/light mode support
- Hero section with quick start code example
- Feature highlights with icons and descriptions
- Technology stack showcase with badges

### 📚 **Developer Onboarding**
- Step-by-step quick start guide
- Prerequisites and installation instructions
- Environment setup and configuration
- First steps and verification

### 🏗️ **System Architecture**
- Visual architecture diagram
- Design principles explanation
- Component relationships
- Clean architecture overview

### ⚡ **Make Commands Reference**
- Categorized command reference
- Development, testing, Docker, deployment commands
- Copy-to-clipboard functionality
- Usage examples and descriptions

### 🚀 **Deployment Guides**
- Docker deployment instructions
- AWS ECS production deployment
- CI/CD pipeline explanation
- Automated deployment setup

### 🔧 **Technical Information**
- Complete technology stack with badges
- Tool descriptions and links
- Framework explanations
- Infrastructure components

### ✨ **Interactive Features**
- Smooth scrolling navigation
- Code block copy buttons
- Responsive design for all devices
- Hover effects and animations
- Accessibility support

## Files Created

```
docs/
├── index.html          # Main website page
├── styles.css          # Complete styling with CSS variables
├── script.js          # Interactive functionality
└── README.md          # This setup guide
```

## Customization

### Update Content
- Edit `docs/index.html` to modify content
- Update links, descriptions, and examples
- Add new sections as needed

### Styling
- Modify `docs/styles.css` for visual changes
- CSS variables make theming easy
- Responsive breakpoints included

### Functionality
- Enhance `docs/script.js` for new features
- Add analytics, forms, or other interactive elements

## SEO and Social Media

The website includes:
- Meta tags for SEO
- Open Graph tags for social sharing
- Twitter Card support
- Semantic HTML structure
- Proper heading hierarchy

## Performance

Optimized for performance:
- Minimal dependencies (only Prism.js for syntax highlighting)
- Efficient CSS with variables
- Optimized images and fonts
- Fast loading times

Your professional GitHub Pages website is now ready! 🎉
