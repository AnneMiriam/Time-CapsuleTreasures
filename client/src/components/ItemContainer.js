import React from "react";
import ItemCard from "./ItemCard";

function ItemContainer({ items, removeItem, editItem, addLike }) {
    return (
        <div id='item-card-container'>
            {items.map((item) => (
                <ItemCard
                    userItem={item}
                    id={item.id}
                    key={item.id}
                    removeItem={removeItem}
                    editItem={editItem}
                    addLike={addLike}
                />
            ))}
        </div>
    )
}

export default ItemContainer;