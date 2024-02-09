import React, { useState } from "react";

function ItemCard({ userItem, removeItem, updateItem, addLike }){
    const {name, image, description, category, decade, trade_status, ebayLink, likes, id } = userItem
    // const [isTrade, setIsTrade] = useState(false)

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
        </div>
    )
}

export default ItemCard;