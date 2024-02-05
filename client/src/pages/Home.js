import "../styles.css"
import React from "react";
import NavBar from "../components/NavBar";

function Home() {
  return (
    <>
      <header>

        <NavBar />
      </header>
      <div className="homeGridContainer">
        <div className="leftColumn homeColumn">
          <p> Featured Items</p>
        </div>
        <main className="homeBackground">
          <div>
            <h1 className="home-header">Time Capsule Treasures</h1>

          <div className="mainContent"></div>
          </div>
        </main>
        <div className="rightColumn homeColumn">
          <p></p>
        </div>
      </div>
    </>
  );
}

export default Home;
