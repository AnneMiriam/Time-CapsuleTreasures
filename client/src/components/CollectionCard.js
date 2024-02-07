import React from 'react';

// Shows first 4 items images 
// Shows Name of collections
// clickable to enter the Collection page

function CollectionCard({userCollection, removeCollection}) {
    const {name, id} = userCollection

    function deleteCollection() {
        fetch(`/collections/${id}`, {
            method: "DELETE"
        })
        .then(() => {
            removeCollection(id)
        })
    }
    return (
        <div className='collection-card'>
            <a href={`/collections/${id}`}>
                <h2>{name}</h2>
            </a>
            <button className='del-btn' onClick={deleteCollection}>Delete</button>
        </div>
    )
}

export default CollectionCard;