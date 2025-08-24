// Smooth scrolling for navigation links
document.addEventListener('DOMContentLoaded', function() {
    // Handle navigation clicks
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offsetTop = target.offsetTop - 80; // Account for fixed navbar
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    let lastScrollY = window.scrollY;

    window.addEventListener('scroll', () => {
        const currentScrollY = window.scrollY;
        
        // Add/remove shadow based on scroll position
        if (currentScrollY > 10) {
            navbar.style.boxShadow = '0 4px 6px -1px rgb(0 0 0 / 0.1)';
        } else {
            navbar.style.boxShadow = 'none';
        }
        
        lastScrollY = currentScrollY;
    });

    // Copy code functionality
    function addCopyButtons() {
        const codeBlocks = document.querySelectorAll('pre code, .code-window code');
        
        codeBlocks.forEach(codeBlock => {
            const container = codeBlock.closest('pre') || codeBlock.closest('.code-window');
            if (!container) return;
            
            const copyButton = document.createElement('button');
            copyButton.className = 'copy-button';
            copyButton.innerHTML = `
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M8 4V16C8 17.1046 8.89543 18 10 18H18C19.1046 18 20 17.1046 20 16V7.24264C20 6.9755 19.8946 6.71852 19.7071 6.53107L16.4689 3.29289C16.2814 3.10536 16.0245 3 15.7574 3H10C8.89543 3 8 3.89543 8 5Z" stroke="currentColor" stroke-width="2"/>
                    <path d="M16 18V20C16 21.1046 15.1046 22 14 22H6C4.89543 22 4 21.1046 4 20V9C4 7.89543 4.89543 7 6 7H8" stroke="currentColor" stroke-width="2"/>
                </svg>
                Copy
            `;
            
            copyButton.addEventListener('click', async () => {
                try {
                    const text = codeBlock.textContent || '';
                    await navigator.clipboard.writeText(text);
                    
                    // Visual feedback
                    const originalText = copyButton.innerHTML;
                    copyButton.innerHTML = `
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M20 6L9 17L4 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                        Copied!
                    `;
                    copyButton.style.color = '#059669';
                    
                    setTimeout(() => {
                        copyButton.innerHTML = originalText;
                        copyButton.style.color = '';
                    }, 2000);
                } catch (err) {
                    console.error('Failed to copy text: ', err);
                }
            });
            
            // Style and position the button
            container.style.position = 'relative';
            copyButton.style.cssText = `
                position: absolute;
                top: 1rem;
                right: 1rem;
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                color: #cbd5e1;
                padding: 0.5rem;
                border-radius: 0.375rem;
                font-size: 0.75rem;
                cursor: pointer;
                display: flex;
                align-items: center;
                gap: 0.25rem;
                font-family: inherit;
                transition: all 0.2s;
                backdrop-filter: blur(4px);
                z-index: 10;
            `;
            
            // Hover effects
            copyButton.addEventListener('mouseenter', () => {
                copyButton.style.background = 'rgba(255, 255, 255, 0.2)';
                copyButton.style.borderColor = 'rgba(255, 255, 255, 0.3)';
            });
            
            copyButton.addEventListener('mouseleave', () => {
                copyButton.style.background = 'rgba(255, 255, 255, 0.1)';
                copyButton.style.borderColor = 'rgba(255, 255, 255, 0.2)';
            });
            
            container.appendChild(copyButton);
        });
    }
    
    // Add copy buttons after a short delay to ensure DOM is ready
    setTimeout(addCopyButtons, 100);

    // Intersection Observer for animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe elements for animation
    const animatedElements = document.querySelectorAll('.feature-card, .doc-link, .deployment-card, .step');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(2rem)';
        el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        observer.observe(el);
    });

    // Add staggered animation delay to grid items
    document.querySelectorAll('.features-grid .feature-card').forEach((card, index) => {
        card.style.transitionDelay = `${index * 0.1}s`;
    });

    // GitHub stars counter (if you want to show repo stats)
    async function updateGitHubStats() {
        try {
            const response = await fetch('https://api.github.com/repos/shyenuganti/gen_ai_rag_langchain');
            const data = await response.json();
            
            // Update stars count if element exists
            const starsElement = document.querySelector('.github-stars');
            if (starsElement && data.stargazers_count !== undefined) {
                starsElement.textContent = data.stargazers_count;
            }
        } catch (error) {
            console.log('Could not fetch GitHub stats:', error);
        }
    }

    // Uncomment if you want to show GitHub stats
    // updateGitHubStats();

    // Performance: Preload critical resources
    function preloadCriticalResources() {
        const criticalImages = [
            'assets/banner.png',
            'assets/favicon.png'
        ];

        criticalImages.forEach(src => {
            const link = document.createElement('link');
            link.rel = 'preload';
            link.as = 'image';
            link.href = src;
            document.head.appendChild(link);
        });
    }

    preloadCriticalResources();

    // Add keyboard navigation support
    document.addEventListener('keydown', (e) => {
        // Escape key to close any modals or overlays
        if (e.key === 'Escape') {
            // Close any open modals, dropdowns, etc.
            const activeModal = document.querySelector('.modal.active');
            if (activeModal) {
                activeModal.classList.remove('active');
            }
        }
    });

    // Add focus management for accessibility
    const focusableElements = 'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])';
    
    function trapFocus(element) {
        const focusableContent = element.querySelectorAll(focusableElements);
        const firstFocusableElement = focusableContent[0];
        const lastFocusableElement = focusableContent[focusableContent.length - 1];

        document.addEventListener('keydown', function(e) {
            if (e.key === 'Tab') {
                if (e.shiftKey) {
                    if (document.activeElement === firstFocusableElement) {
                        lastFocusableElement.focus();
                        e.preventDefault();
                    }
                } else {
                    if (document.activeElement === lastFocusableElement) {
                        firstFocusableElement.focus();
                        e.preventDefault();
                    }
                }
            }
        });
    }

    // Enhanced mobile experience
    function handleMobileInteractions() {
        // Add touch feedback for interactive elements
        const interactiveElements = document.querySelectorAll('button, .btn, .doc-link, .feature-card');
        
        interactiveElements.forEach(element => {
            element.addEventListener('touchstart', function() {
                this.style.transform = 'scale(0.98)';
            });
            
            element.addEventListener('touchend', function() {
                this.style.transform = '';
            });
        });

        // Improve scroll performance on mobile
        let ticking = false;
        
        function updateScrollEffects() {
            // Your scroll effects here
            ticking = false;
        }

        document.addEventListener('scroll', function() {
            if (!ticking) {
                requestAnimationFrame(updateScrollEffects);
                ticking = true;
            }
        }, { passive: true });
    }

    handleMobileInteractions();

    console.log('🚀 Gen AI RAG LangChain website loaded successfully!');
});
