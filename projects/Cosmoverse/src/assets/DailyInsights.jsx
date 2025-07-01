import React, { useEffect, useState } from 'react';

function DailyInsights() {
    const [insight, setInsight] = useState('');

    useEffect(() => {
        // Fetch or generate daily insights here
        setInsight('Today is a great day for new beginnings!');
    }, []);

    return (
        <div className="card">
            <h2>Daily Zodiac Insights</h2>
            <p>{insight}</p>
        </div>
    );
}

export default DailyInsights;
