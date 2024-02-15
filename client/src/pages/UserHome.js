import "../styles.css";
import React, { useState, useEffect } from "react";
import HomeItemContainer from "../components/HomeItemContainer";

function UserHome() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch("/api/items")
      .then((r) => r.json())
      .then(setItems);
  }, []);

  function addLike(id) {
    setItems(
      items.map((item) => {
        if (item.id !== id) {
          return item;
        } else {
          return { ...item, likes: item.likes + 1 };
        }
      })
    );
  }

  return (
    <>
      <HomeItemContainer items={items} addLike={addLike} />
    </>
  );
}

export default UserHome;
