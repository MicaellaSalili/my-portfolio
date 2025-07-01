import React, { useState } from 'react';

function Favorites() {
    const [favorites, setFavorites] = useState([]);

    const addFavorite = (item) => {
        setFavorites([...favorites, item]);
    };

    return (
        <div className="card">
            <h2>Favorites</h2>
            <button className="button" onClick={() => addFavorite('New Insight')}>Add to Favorites</button>
            <ul>
                {favorites.map((fav, index) => (
                    <li key={index}>{fav}</li>
                ))}
            </ul>
        </div>
    );
}

export default Favorites;
