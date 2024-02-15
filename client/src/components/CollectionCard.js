import React from "react";
// import Collection from '../pages/Collection';
import { Link } from "react-router-dom";
// Shows first 4 items images
// Shows Name of collections
// clickable to enter the Collection page

function CollectionCard({ userCollection, removeCollection }) {
  const { name, id } = userCollection;

  function deleteCollection() {
    fetch(`/api/collections/${id}`, {
      method: "DELETE",
    })
      .then((response) => {
        if (response.ok) {
          removeCollection(id);
        } else {
          console.error("Failed to delete");
        }
      })
      .catch((error) => {
        console.error("Error deleting collection:", error);
      });
  }

  return (
    <div className="collection-card">
      <Link to={`/collections/${id}`}>
        <h2>{name}</h2>
      </Link>
      <button className="del-btn" onClick={deleteCollection}>
        Delete
      </button>
    </div>
  );
}

export default CollectionCard;
