import "../styles.css";
import React, { useState, useEffect } from "react";
import HomeItemContainer from "../components/HomeItemContainer";

function Home() {
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

export default Home;

// function Home() {
//   return (
//     <>
//       <header>

//       </header>
//       <div className="homeGridContainer">
//         <div className="leftColumn homeColumn">
//         </div>
//         <main className="homeBackground">
//           <div>
//             <h1 className="home-header">Time Capsule Treasures</h1>

//           <div className="mainContent"></div>
//           </div>
//         </main>
//         <div className="rightColumn homeColumn">
//           <p></p>
//         </div>
//       </div>
//     </>
//   );
// }

// export default Home;
