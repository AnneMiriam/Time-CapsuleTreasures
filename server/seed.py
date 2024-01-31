from random import choice as rc
import random
from faker import Faker

# Local imports
from config import app, db
from models import User, Collection, Comment, Item, Forum

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
    # },
]

CATEGORIES = [
    'Toys', 'VHS', 'Books', 'Stuffed Animals', 'Games', 'Clothes', 'DVD'
]

DECADES = [
    1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000
]

def seed_items():
    for event in ITEMS:
        new_event = Item(
            image = event['image'],
            name = event['name'],
            description = event['description'],
            decade = event['decade'],
            category = event['category'],
            trade_status = event['trade_status']
        )
        db.session.add(new_event) 
    db.session.commit()
    print("Events added!")

def seed_admins():
    new_user = User(
        first_name = fake.first_name(),
        last_name = fake.last_name(),
        username = "admin",
        email = "admin@email.com",
    )
    new_user.admin = True
    new_user.password_hash = "password"
    db.session.add(new_user)
    for _ in range(4):
        fake_username = fake.email().split("@")[0]

        if len(fake_username) < 5:
            fake_username + "xyz"

        new_user = User(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            username = fake_username,
            email = fake.email(),
        )
        new_user.admin = True
        new_user.password_hash = "password"
        db.session.add(new_user)
    db.session.commit()
    print("Admins added!")

def seed_users():
    for _ in range(25):
        fake_username = fake.email().split("@")[0]

        if len(fake_username) < 5:
            fake_username + "789"

        new_user = User(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            username = fake_username,
            email = fake.email(),
        )
        new_user.password_hash = "password"
        db.session.add(new_user)
    db.session.commit()
    print("Users added!")

def seed_pets():
    today = datetime.today()
    start_date = today - timedelta(days=365 * 8)
    end_date = today - timedelta(days=30 * 3)

    for pet in PETS:
        new_pet = Pet(
            image = pet["image"],
            name = fake.first_name(),
            species = rc(["cat", "dog"]),
            breed = rc(BREEDS),
            sex = rc(["female", "male"]),
            est_birthday = fake.date_between(start_date=start_date, end_date=end_date),
            description = pet["description"],
        )
        db.session.add(new_pet)
    db.session.commit()
    print("Pets added!")

def associate_user_events():
    for _ in range(30):
        user_instance = db.session.query(User).filter_by(id=random.randrange(1, 30)).first()
        event_instance = db.session.query(Event).filter_by(id=random.randrange(1, len(EVENTS))).first()

        existing_association = db.session.query(UserEvent).filter_by(
            user_id=user_instance.id, event_id=event_instance.id).first()

        if not existing_association:
            new_user_event = UserEvent(user_id=user_instance.id, event_id=event_instance.id)
            db.session.add(new_user_event)
    db.session.commit()
    print("Associations added!")

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        clear_tables()
        seed_events()
        seed_admins()
        seed_users()
        seed_pets()
        associate_user_events()
