import React from "react";

function ItemCard({ userItem, removeItem, updateItem, addLike }){
    const {name, image, description, category, decade, tradeStatus, ebayLink, likes, id } = userItem

    function tradeItem() {
        fetch(`/items/${id}`, {
            method: 'DELETE'
        })
        .then(() => {
            removeItem(id)
        })
    }

    function like() {
        fetch(`/items/${id}`, {
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
        <div className="card">
            <h2>{name}</h2>
            <img
                src={image}
                alt={name}
                className="item-image"
            />
            <p>Description: {description}</p>
            <p>Category: {category}</p>
            <p>Decade: {decade}</p>
            <p>{likes} Likes</p>
            <button className="like-btn" onClick={like} >Like {"<3"}</button>
        </div>
    )
}

export default ItemCard;