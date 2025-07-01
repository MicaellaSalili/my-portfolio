import React from 'react';

function ShareButton({ text }) {
    const handleShare = () => {
        // Example: Open the sharing dialog (implement social media APIs as needed)
        alert(`Sharing: ${text}`);
    };

    return (
        <button className="button" onClick={handleShare}>Share</button>
    );
}

export default ShareButton;
