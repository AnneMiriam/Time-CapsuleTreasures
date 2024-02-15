import "../styles.css";
import React, { useState, useEffect } from "react";


function Home() {
  // const [items, setItems] = useState([]);

  // useEffect(() => {
  //   fetch("/api/items")
  //     .then((r) => r.json())
  //     .then(setItems);
  // }, []);

  // function addLike(id) {
  //   setItems(
  //     items.map((item) => {
  //       if (item.id !== id) {
  //         return item;
  //       } else {
  //         return { ...item, likes: item.likes + 1 };
  //       }
  //     })
  //   );
  // }

  return (
    <>
      <div className="front-page">
        <h2>Welcome to</h2>
      </div>
      <div className="logoContainer"></div>
    </>
  );
}

export default Home;


