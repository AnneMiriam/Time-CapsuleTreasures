import React, { useState } from "react";

function CollectionForm({handleNewCltn}) {
    const [name, setName] = useState('');

    function handleSubmit(e) {
        e.preventDefault();

        const newCollection = {
            name
        }
        fetch('/api/collections', {
            method: "POST",
            headers: {
                "Content-Type":"application/json"
            },
            body: JSON.stringify(newCollection)
        })
        .then(r => r.json())
        .then(handleNewCltn)
    }
    return (
        <div className="container">
            <form className="add-cltn-form" onSubmit={handleSubmit} >
                <h3>Create a Collection!</h3>
                <input
                    type="text"
                    name="name"
                    placeholder="Name your Collection"
                    className="input-text"
                    value={name}
                    onChange={e => setName(e.target.value)}
                />
                <br />
                <input
                    type="submit"
                    name="submit"
                    value="Create Collection"
                    className="submit"
                />
            </form>
        </div>
    );
}
export default CollectionForm;