import React, { useEffect, useState, useContext } from 'react';
import CollectionForm from '../components/CollectionForm';
import CollectionContainer from '../components/CollContainer';
import { AuthContext } from '../components/AuthContext'

    // Show all of a users collections cards
    // New Collection Form

function User() {
    const [collections, setCollections] = useState([]);
    const { user } = useContext(AuthContext)
    

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

    useEffect(() => {
        // console.log(collections);
    }, [collections]); // Log collections whenever it changes


    function removeCollection(id) {
        setCollections(collections.filter(collection => collection.id !== id))
    };

    const userData = JSON.parse(localStorage.getItem('user'));
    const userName = userData ? userData.first_name: "New User";
    return (
        <>
            <div className='user-name'>
                <h2>{userName}'s Collections</h2>
            </div>
            <CollectionContainer 
                collections={collections} 
                removeCollection={removeCollection} 
            />
            <CollectionForm handleNewCltn={addNewCltn} /> 
        </>
    )
}

export default User;