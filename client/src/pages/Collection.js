import React, { useEffect, useState } from 'react';
import ItemForm from '../components/ItemForm';
import ItemContainer from '../components/ItemContainer'
import NavBar from '../components/NavBar'

// Collection should fetch all items that share that collection_id
// Collection should have a hidden form to add new items

function Collection() {
    const [showForm, setShowForm] = useState(false);
    const [items, setItems] = useState([]);

    useEffect(() => {
        fetch('/items')
        .then(r => r.json())
        .then(setItems)
    },[])

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
            <NavBar />
            <ItemContainer 
                items={items} 
                removeItem={removeItem} 
                addLike={addLike} 
                // updateItem={updateItem}
                />
            {showForm ? <ItemForm handleNewItem={addNewItem} /> : null}
        </>
    )
}

export default Collection;