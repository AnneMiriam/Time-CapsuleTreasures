import CollectionCard from './CollectionCard';

function CollectionContainer({collections, removeCollection}) {
    return (
        <div id="cltn-container">
            {collections.map((collection) => (
                <CollectionCard 
                    userCollection={collection}
                    id={collection.id}
                    key={collection.id}
                    removeCollection={removeCollection}
                />
            ))}
        </div>
    );
};

export default CollectionContainer;