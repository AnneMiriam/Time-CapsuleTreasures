import React, { useState } from "react";

function ItemCard({ userItem, removeItem, addLike, editItem }){
    const {name, image, description, category, decade, likes, id } = userItem
    // const [isTrade, setIsTrade] = useState(false)
    const [data, setData] = useState([])
    const [editableItem, setEditableItem] = useState(userItem)
    const [editMode, setEditMode] = useState(false)

    function handleChange(e) {
        const { name, value } = e.target;
        setEditableItem({ ...editableItem, [name]: value });
    }

    function handleSubmit(e) {
        e.preventDefault();
        editsItem(editableItem);
        setEditMode(false);
    }

    function toggleEdit() {
        setEditMode(!editMode);
    }

    function tradeItem() {
        fetch(`/api/items/${id}`, {
            method: 'DELETE'
        })
        .then(() => {
            removeItem(id)
        })
    }

    function like() {
        fetch(`/api/items/${id}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                likes: likes +1
            })
        })
        .then(() => {
            addLike(id)
        })
    }

    function editsItem(updatedItem) {
        const cleanUpdatedItem = {
            id: updatedItem.id, // Ensure the id is included
            name: updatedItem.name,
            image: updatedItem.image,
            description: updatedItem.description,
            category: updatedItem.category,
            decade: updatedItem.decade,
        }

        fetch(`/api/items/${id}`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(cleanUpdatedItem),
            // body: JSON.stringify(updatedItem),
        })
        .then(r => r.json())
        .then(updatedItem => {
            // setData(data.map(item => (item.id === updatedItem.id ? updatedItem : item)));
            // setEditableItem(updatedItem)
            editItem(updatedItem)
        })
        .catch(error => error)
    }

    return (
        <div className="item-card">
            <h2>{name}</h2>
            <img
                src={image}
                alt={name}
                className="item-image"
            />
            {editMode ? (
                <form onSubmit={handleSubmit}>
                    <input type="text" name="name" value={editableItem.name} onChange={handleChange} />
                    <input type="text" name="image" value={editableItem.image} onChange={handleChange} />
                    <textarea name="description" value={editableItem.description} onChange={handleChange} />
                    <input type="text" name="category" value={editableItem.category} onChange={handleChange} />
                    <input type="text" name="decade" value={editableItem.decade} onChange={handleChange} />
                    <button type="submit" className="update" >Update Item</button>
                </form>
            ) : (
                <>
                    <p>Description: {description}</p>
                    <p>Category: {category}</p>
                    <p>Decade: {decade}</p>
                    <button className="update" onClick={toggleEdit}>Edit Item</button>
                </>
            )}
            
            <button className="like-btn" onClick={like} >🧡 {likes} Likes</button>
            <button className="del-btn" onClick={tradeItem}>Remove Item</button>
            {/* <button className="update" onClick={editItem}>Update Item</button> */}
        </div>
    )
}

export default ItemCard;