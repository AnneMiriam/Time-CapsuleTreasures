import React from "react";
import HomeItemCard from "./HomeItemCard";

function HomeItemContainer({ items,  addLike }) {
    return (
        <div id='item-container'>
            {items.map((item) => (
                <HomeItemCard
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