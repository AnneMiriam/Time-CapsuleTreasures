import React from "react";
import ItemCard from "./ItemCard";

function ItemContainer({ items, removeItem, updateItem, addLike }) {
    return (
        <div id='item-container'>
            {items.map((item) => (
                <ItemCard
                    userItem={item}
                    id={item.id}
                    key={item.id}
                    removeItem={removeItem}
                    updateItem={updateItem}
                    addLike={addLike}
                />
            ))}
        </div>
    )
}

export default ItemContainer;