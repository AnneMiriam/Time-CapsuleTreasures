from random import choice as rc
import random
from faker import Faker

# Local imports
from config import *
import bcrypt
from models import User, Collection, Comment, Item, UserCollection, ItemCollection


fake = Faker()

def clear_tables():
    db.drop_all()
    db.create_all()
    print("Database created!")


ITEMS = [
    # {
    #     'name': '',
    #     'image': '',
    #     'category': '',
    #     'decade': '',
    #     'description': '',
    #     'trade_status': '',
    #     'ebay_link': '',
        # 'likes': 0,
    # },
    {
        'name': 'VHS tape',
        'image': 'server/photos/VHS.png',
        'category': 'VHS',
        'decade': 2000,
        'description': 'VHS workout tape and VCR',
        'trade_status': True,
        'ebay_link': '',
        'likes': 0,
    },
    {
        'name': 'Lisa Frank Stationary',
        'image': 'server/photos/LisaFrank.png',
        'category': 'Other',
        'decade': 1990,
        'description': 'A Lisa Frank sticker sheet and pencil sharpener(missing eraser).',
        'trade_status': False,
        'ebay_link': '',
        'likes': 1,
    },
    {
        'name': 'GS teddy bear',
        'image': 'server/photos/MMRteddy.png',
        'category': 'Stuffed Animals',
        'decade': 1990,
        'description': 'A teddy bear from Meadow Mountain Ranch Girl Scout Camp in Colorado',
        'trade_status': False,
        'ebay_link': '',
        'likes': 3,
    },
]

CATEGORIES = [
    'Toys', 'VHS', 'Books', 'Stuffed Animals', 'Games', 'Clothes', 'DVD', 'Other'
]

DECADES = [
    1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000
]

# FORUMS = [
#     {
#         'post': 'I am looking for a top similar to one my sister had in the 90s, that she passed on to me. It was crush velvet, had a collar, and only three button in front at the bust. I loved that top and now that it is back in style I am sad I got rid of it.'
#     },
#     {
#         'post': 'I have been looking for a copy of a VHS of the Chipmunks for 20 years. It was called Around the World with the Chipmunks. Does anyone know where I could find one that still plays?'
#     }
# ]

def seed_items():
    for item in ITEMS:
        new_item = Item(
            image = item['image'],
            name = item['name'],
            description = item['description'],
            decade = rc(DECADES),
            category = item['category'],
            trade_status = item['trade_status'],
            ebay_link = item['ebay_link'],
            likes = item['likes']
        )
        db.session.add(new_item) 
    db.session.commit()
    print("Items added!")


def seed_users():
    users = []
    # generate unique usernames and emails
    while len(users) < 20:
        username = fake.user_name()
        email = fake.email()
        first_name = fake.first_name()  

        raw_password = fake.password(
            length=10, special_chars=True, digits=True, upper_case=True, lower_case=True
        )
        hashed_password = bcrypt.hashpw(raw_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

        user = User(username=username, email=email, first_name=first_name, _password_hash=hashed_password)
        users.append(user)
    db.session.add_all(users)
    print("Users added!")


def seed_collection():
    for cat in CATEGORIES:
        new_collection = Collection(
            name = rc(CATEGORIES)
        )
        db.session.add(new_collection)
    db.session.commit()
    print("Collection added")


def associate_collection():
    for _ in range(30):
        user_instance = db.session.query(User).filter_by(id=random.randrange(1, 30)).first()
        collection_instance = db.session.query(Collection).filter_by(id=random.randrange(1, 30)).first()

        if user_instance is not None and collection_instance is not None:
            existing_association = db.session.query(UserCollection).filter_by(
                user_id=user_instance.id, collection_id=collection_instance.id).first()

            if not existing_association:
                new_user_collection = UserCollection(user_id=user_instance.id, collection_id=collection_instance.id)
                db.session.add(new_user_collection)
    db.session.commit()
    print("Collection associations added!")


def associate_item():
    for _ in range(30):
        item_instance = db.session.query(Item).filter_by(id=random.randrange(1, len(ITEMS))).first()
        collection_instance = db.session.query(Collection).filter_by(id=random.randrange(1, 30)).first()

        if item_instance is not None and collection_instance is not None:
            existing_association = db.session.query(ItemCollection).filter_by(
                item_id=item_instance.id, collection_id=collection_instance.id).first()

            if not existing_association:
                new_item_collection = ItemCollection(item_id=item_instance.id, collection_id=collection_instance.id)
                db.session.add(new_item_collection)
    db.session.commit()
    print("Item associations added!")


def associate_comment():
    for _ in range(30):
        item_instance = db.session.query(Item).filter_by(id=random.randrange(1, len(ITEMS))).first()

        if item_instance is not None:
            existing_association = db.session.query(Comment).filter_by(
                item_id=item_instance.id).first()

            if not existing_association:
                new_user_item = Comment(item_id=item_instance.id)
                db.session.add(new_user_item)
    db.session.commit()
    print("Comment associations added!")




if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        clear_tables()
        seed_users()
        seed_items()
        seed_collection()
        associate_collection()
        associate_item()
        associate_comment()
