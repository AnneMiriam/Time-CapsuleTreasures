import React from 'react';
// import Collection from '../pages/Collection';

// Shows first 4 items images 
// Shows Name of collections
// clickable to enter the Collection page

function CollectionCard({userCollection, removeCollection}) {
    const {name, id} = userCollection

    function deleteCollection() {
        fetch(`/api/collections/${id}`, {
            method: "DELETE"
        })
        .then((response) => {
            if (response.ok) {
                removeCollection(id)
            } else {
                console.error('Failed to delete')
            }
        })
        .catch(error => {
            console.error('Error deleting collection:', error);
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