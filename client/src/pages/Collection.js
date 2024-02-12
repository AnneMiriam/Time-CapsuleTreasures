import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import ItemForm from '../components/ItemForm';
import ItemContainer from '../components/ItemContainer'


// Collection should fetch all items that share that collection_id
// Collection should have a hidden form to add new items

function Collection() {
    const [showForm, setShowForm] = useState(false);
    const [items, setItems] = useState([]);
    const [filterItems, setFilterItems] = useState([]);
    // const collectionId = JSON.parse(localStorage.getItem("collection"))?.id;
    const {id} = useParams()

    useEffect(() => {
        fetch(`/api/collections/${id}`)
        .then(r => r.json())
        .then(collection => {
            setItems(collection.items);
            console.log(collection.items)
        })
    },[id])

    function handleClick() {
        setShowForm((showForm) => !showForm);
    }

    function addNewItem(newItem) {
        setItems([...items, newItem])
    }

    function removeItem(id) {
        setItems(items.filter(item => item.id !== id))
    }

    function addLike(id) {
        setItems(items.map(item => {
            if(item.id !== id) {
                return item
            } else {
                return {...item, likes: item.likes +1}
            }
        }))
    }

    return (
        <>
            <ItemContainer 
                items={items} 
                removeItem={removeItem} 
                addLike={addLike} 
                />
            {showForm ? <ItemForm handleNewItem={addNewItem} /> : null}
            <div className='btnContainer'>
                <button className='submit' onClick={handleClick}>Add an Item</button>
            </div>
        </>
    )
}

export default Collection;