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