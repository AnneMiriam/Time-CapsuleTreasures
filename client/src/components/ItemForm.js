import React, { useState } from "react";


function ItemForm({handleNewItem}) {
  const [name, setName] = useState('');
  const [image, setImage] = useState('');
  const [category, setCategory] = useState('');
  const [description, setDescription] = useState('');
  const [decade, setDecade] = useState('');
  
  function handleSubmit(e) {
    e.preventDefault();
    
    const newItem = {
      name, 
      image, 
      category,
      description,
      decade,
      likes: 0
    }
console.log("newItem", newItem);

    fetch('/api/items', {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      },
      body: JSON.stringify(newItem)
    })
    .then(res=>res.json())
    .then(handleNewItem)
  }

  return (
    <div className="container">
      <form className="add-item-form" onSubmit={handleSubmit} >
        <h3>Add items!</h3>
        <input
          type="text"
          name="name"
          placeholder="Item's name"
          className="input-text"
          value={name}
          onChange={e => setName(e.target.value)}
        />
        <br />
        <input
          type="text"
          name="image"
          placeholder="Enter the item's image URL..."
          className="input-text"
          value={image}
          onChange={e => setImage(e.target.value)}
        />
        <br />
        <input
          type="text"
          name="description"
          placeholder="Item's description"
          className="input-text"
          value={description}
          onChange={e => setDescription(e.target.value)}
        />
        <br />
        <select
          name="category"
          placeholder="What category is this item?"
          className="input-text"
          value={category}
          onChange={e => setCategory(e.target.value)}
        >
            <option value="" disabled>Select a category</option>
            <option value="Toys">Toys</option>
            <option value="VHS/VCR">VHS/VCR</option>
            <option value="DVD">DVD</option>
            <option value="Books">Books</option>
            <option value="Stuffed Animals">Stuffed Animals</option>
            <option value="Games">Games</option>
            <option value="Clothes">Clothes</option>
            <option value="Other">Other</option>
        </select>
        <br />
        <select
          name="decade"
          placeholder="What decade is this item?"
          className="input-text"
          value={decade}
          onChange={e => setDecade(e.target.value)}
        >
            <option value="" disabled>Select a decade</option>
            <option value="1900">1900 and earlier</option>
            <option value="1910">1910</option>
            <option value="1920">1920</option>
            <option value="1930">1930</option>
            <option value="1940">1940</option>
            <option value="1950">1950</option>
            <option value="1960">1960</option>
            <option value="1970">1970</option>
            <option value="1980">1980</option>
            <option value="1990">1990</option>
            <option value="2000">2000</option>
        </select>
        <br />
        <input
          type="submit"
          name="submit"
          value="Add New Item"
          className="submit"
        />
      </form>
    </div>
  );
}

export default ItemForm;
