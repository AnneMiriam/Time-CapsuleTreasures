import React from "react";
import ItemCard from "./ItemCard";

function HomeItemContainer({ items,  addLike }) {
    return (
        <div id='item-container'>
            {items.map((item) => (
                <ItemCard
                    userItem={item}
                    id={item.id}
                    key={item.id}
                    addLike={addLike}
                />
            ))}
        </div>
    )
}

export default HomeItemContainer;