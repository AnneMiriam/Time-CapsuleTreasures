import React, { useEffect, useState, useContext } from 'react';
import CollectionForm from '../components/CollectionForm';
import CollectionContainer from '../components/CollContainer';
import { AuthContext } from '../components/AuthContext'

    // Show all of a users collections cards
    // New Collection Form

function User() {
    const { user } = useContext(AuthContext)
    const [collections, setCollections] = useState([]);

    useEffect(() => {
        if (user) {
            fetch('/api/collections')
            .then(r => r.json())
            .then(setCollections)
        }
    },[user])

    function addNewCltn(newCollection) {
        setCollections([...collections, newCollection])
    }

    function removeCollection(id) {
        setCollections(collections.filter(collection => collection.id !== id))
    }

    return (
        <>
            <CollectionContainer 
                collections={collections} 
                removeCollection={removeCollection} 
            />
            <CollectionForm handleNewCltn={addNewCltn} /> 
        </>
    )
}

export default User;