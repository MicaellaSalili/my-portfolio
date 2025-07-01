// Smooth scrolling for navigation links
document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const sectionId = this.getAttribute('href');
        document.querySelector(sectionId).scrollIntoView({ behavior: 'smooth' });
    });
});

// Button click events (placeholder for now)
document.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', () => {
        if (button.textContent === 'View My Work') {
            document.querySelector('#works').scrollIntoView({ behavior: 'smooth' });
        } else if (button.textContent === 'Contact Me') {
            document.querySelector('#contact').scrollIntoView({ behavior: 'smooth' });
        }
    });
});

document.querySelectorAll('.skills-tabs button').forEach(btn => {
    btn.addEventListener('click', function() {
        // Remove active from all buttons
        document.querySelectorAll('.skills-tabs button').forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        // Hide all skills lists
        document.querySelectorAll('.skills-section .skills').forEach(list => list.style.display = 'none');
        // Show the selected skills list
        const tab = this.getAttribute('data-tab');
        document.querySelector('.skills-' + tab).style.display = 'flex';
    });
});

// Skills horizontal scroll function
function scrollSkills(direction) {
    const activeSkills = document.querySelector('.skills:not([style*="display: none"])');
    if (!activeSkills) return;
    
    const scrollAmount = 250; // Adjust scroll distance
    const currentScroll = activeSkills.scrollLeft;
    
    if (direction === 'left') {
        activeSkills.scrollTo({
            left: currentScroll - scrollAmount,
            behavior: 'smooth'
        });
    } else {
        activeSkills.scrollTo({
            left: currentScroll + scrollAmount,
            behavior: 'smooth'
        });
    }
}

// Show/hide navigation arrows based on scroll position
function updateNavigationVisibility() {
    const activeSkills = document.querySelector('.skills:not([style*="display: none"])');
    if (!activeSkills) return;
    
    const leftBtn = document.querySelector('.skills-nav-left');
    const rightBtn = document.querySelector('.skills-nav-right');
    
    const isScrollable = activeSkills.scrollWidth > activeSkills.clientWidth;
    const isAtStart = activeSkills.scrollLeft <= 0;
    const isAtEnd = activeSkills.scrollLeft >= activeSkills.scrollWidth - activeSkills.clientWidth;
    
    if (!isScrollable) {
        leftBtn.style.display = 'none';
        rightBtn.style.display = 'none';
    } else {
        leftBtn.style.display = isAtStart ? 'none' : 'flex';
        rightBtn.style.display = isAtEnd ? 'none' : 'flex';
    }
}

// Update navigation visibility when skills tab changes
document.querySelectorAll('.skills-tabs button').forEach(btn => {
    btn.addEventListener('click', function() {
        setTimeout(updateNavigationVisibility, 100); // Small delay to ensure display change
    });
});

// Update navigation on scroll
document.addEventListener('DOMContentLoaded', function() {
    const skillsContainers = document.querySelectorAll('.skills');
    skillsContainers.forEach(container => {
        container.addEventListener('scroll', updateNavigationVisibility);
    });
    updateNavigationVisibility();
});

// Update navigation on window resize
window.addEventListener('resize', updateNavigationVisibility);

// Certificate Modal Functions
function openCertificate(filePath, title) {
    const modal = document.getElementById('certificateModal');
    const titleElement = document.getElementById('certificateTitle');
    const viewer = document.getElementById('certificateViewer');
    const image = document.getElementById('certificateImage');
    
    titleElement.textContent = title;
    
    // Check if it's a PDF or image
    if (filePath.toLowerCase().endsWith('.pdf')) {
        // Show PDF in iframe with no-download parameter
        viewer.src = filePath + '#toolbar=0&navpanes=0&scrollbar=0&view=FitH';
        viewer.style.display = 'block';
        image.style.display = 'none';
        
        // Disable right-click context menu on iframe
        viewer.oncontextmenu = function() { return false; };
        
    } else {
        // Show image
        image.src = filePath;
        image.alt = title;
        image.style.display = 'block';
        viewer.style.display = 'none';
        
        // Disable right-click and drag on image
        image.oncontextmenu = function() { return false; };
        image.ondragstart = function() { return false; };
    }
    
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden'; // Prevent background scrolling
}

function closeCertificate() {
    const modal = document.getElementById('certificateModal');
    const viewer = document.getElementById('certificateViewer');
    const image = document.getElementById('certificateImage');
    
    modal.style.display = 'none';
    document.body.style.overflow = 'auto'; // Restore scrolling
    
    // Clear sources to stop loading
    viewer.src = '';
    image.src = '';
}

// Close modal when clicking outside of it
window.onclick = function(event) {
    const modal = document.getElementById('certificateModal');
    if (event.target === modal) {
        closeCertificate();
    }
}

// Close modal with Escape key
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closeCertificate();
    }
});

// Update certificate modal styling for skills
document.addEventListener('DOMContentLoaded', function() {
    const certSkills = document.querySelectorAll('.skills-certifications .skill > div');
    certSkills.forEach(skill => {
        skill.style.cursor = 'pointer';
        skill.style.transition = 'transform 0.3s ease';
        
        skill.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.02)';
        });
        
        skill.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });
});

// Download CV button functionality
document.addEventListener('DOMContentLoaded', function() {
    const downloadBtn = document.querySelector('.download-cv-btn');
    if (downloadBtn) {
        downloadBtn.addEventListener('click', function() {
            // You can replace this URL with your actual Resume file path
            const cvUrl = 'documents/Micaella_Salili_Resume.pdf'; // Update this path to your Resume file
            
            // Create a temporary link element and trigger download
            const link = document.createElement('a');
            link.href = cvUrl;
            link.download = 'Micaella_Salili_Resume.pdf';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            
            // Optional: Show a message or animation
            const originalText = downloadBtn.textContent;
            downloadBtn.textContent = 'Downloading...';
            downloadBtn.style.opacity = '0.7';
            
            setTimeout(() => {
                downloadBtn.textContent = originalText;
                downloadBtn.style.opacity = '1';
            }, 2000);
        });
    }
});