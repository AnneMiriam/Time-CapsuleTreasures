import React, { useState } from "react";

function ItemCard({ userItem, removeItem, addLike }){
    const {name, image, description, category, decade, trade_status, likes, id } = userItem
    // const [isTrade, setIsTrade] = useState(false)
    const [data, setData] = useState([])

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

    function editItem(updatedItem) {
        const cleanUpdatedItem = {
            id: updatedItem.id, // Ensure the id is included
            name: updatedItem.name,
            image: updatedItem.image,
            description: updatedItem.description,
            category: updatedItem.category,
            decade: updatedItem.decade,
            trade_status: updatedItem.trade_status
        }

        fetch(`/api/items/${id}`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(cleanUpdatedItem),
        })
        .then(r => r.json())
        .then(updatedItem => {
            setData(data.map(item => (item.id === updatedItem.id ? updatedItem : item)));
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
            <p>Description: {description}</p>
            <p>Category: {category}</p>
            <p>Decade: {decade}</p>
            {trade_status ? <p>Open to trade</p> : null}
            <button className="like-btn" onClick={like} >🧡 {likes} Likes</button>
            <button className="del-btn" onClick={tradeItem}>Remove Item</button>
            <button className="update" onClick={editItem}>Update Item</button>
        </div>
    )
}

export default ItemCard;