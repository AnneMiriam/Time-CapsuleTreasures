import React, { useState } from "react";


function ItemForm({handleNewItem}) {
  const [name, setName] = useState('');
  const [image, setImage] = useState('');
  const [category, setCategory] = useState('');
  const [description, setDescription] = useState('');
  const [decade, setDecade] = useState('');
  const [tradeStatus, setTradeStatus] = useState('');
  const [ebayLink, setEbayLink] = useState('');

  
function handleSubmit(e) {
  e.preventDefault();
  
  const newItem = {
    name, 
    image, 
    category,
    description,
    decade,
    tradeStatus,
    ebayLink,
    likes: 0
  }
  fetch('/items', {
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
            <option value="category1">Toys</option>
            <option value="category2">VHS/VCR</option>
            <option value="category3">DVD</option>
            <option value="category4">Books</option>
            <option value="category5">Stuffed Animals</option>
            <option value="category6">Games</option>
            <option value="category7">Clothes</option>
            <option value="category8">Other</option>
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
            <option value="decade1">1900 and earlier</option>
            <option value="decade2">1910</option>
            <option value="decade3">1920</option>
            <option value="decade4">1930</option>
            <option value="decade5">1940</option>
            <option value="decade6">1950</option>
            <option value="decade7">1960</option>
            <option value="decade8">1970</option>
            <option value="decade9">1980</option>
            <option value="decade10">1990</option>
            <option value="decade11">2000</option>
        </select>
        <br />
        <input
          type="text"
          name="ebay_link"
          placeholder="Item's ebay_link if any"
          className="input-text"
          value={ebayLink}
          onChange={e => setEbayLink(e.target.value)}
        />
        <br />
        <select
          name="trade_status"
          className="input-text"
          value={tradeStatus}
          onChange={e => setTradeStatus(e.target.value)}
        >
            <option value="" disabled>Is this item up for trade?</option>
            <option value="trade1">False</option>
            <option value="trade2">True</option>
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
