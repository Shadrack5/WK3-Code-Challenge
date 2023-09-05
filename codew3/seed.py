# from faker import Faker
# import random
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# from model import Restaurant,Customer,Review

# fake = Faker()

# # ...

# if __name__ == '__main__':
    
#     engine = create_engine('sqlite:///restuarants.db')
#     Session = sessionmaker(bind=engine)
#     session = Session()
    
#     # Clear old data
#     session.query(Restaurant).delete()
#     session.query(Customer).delete()
#     session.query(Review).delete()
#     session.commit()

#     print("Seeding restaurants...")

#     restaurants = [
#         Restaurant(
#             name=fake.company(),
#             price=random.randint(300, 6000)
#         )
#         for i in range(50)
#     ]

#     session.add_all(restaurants)
#     session.commit()  # Commit the restaurants to get valid IDs

#     print("Seeding customers...")

#     customers = [
#         Customer(
#             first_name=fake.first_name(),
#             last_name=fake.last_name()
#         )
#         for i in range(50)
#     ]

#     session.add_all(customers)
#     session.commit()  # Commit the customers to get valid IDs

#     print("Seeding reviews...")

#     reviews = [
#         Review(
#             star_rating=random.randint(1, 100),  # Adjust the range as needed
#             restaurant_id=random.choice(restaurants).id,
#             customer_id=random.choice(customers).id
#         )
#         for i in range(100)
#     ]

#     session.add_all(reviews)

#     try:
#         session.commit()
#         print("Data committed successfully.")
#     except Exception as e:
#         session.rollback()
#         print("Error committing data:", e)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Restaurant, Customer, Review

## Create a SQLite database and bind it to SQLAlchemy models
engine = create_engine('sqlite:///restaurant.db')
Base.metadata.create_all(engine, checkfirst=True)  # Create the database schema

## Create a session
Session = sessionmaker(bind=engine)
session = Session()

## Create sample data
restaurant1 = Restaurant(name='presige', price=3)
restaurant2 = Restaurant(name='karen mall', price=2)
customer1 = Customer(first_name='Amos', last_name='Rono')
customer2 = Customer(first_name='Enock', last_name='lenny')

review1 = Review(star_rating=4, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=5, restaurant=restaurant2, customer=customer2)

## Add data to the session and commit
session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])
session.commit()