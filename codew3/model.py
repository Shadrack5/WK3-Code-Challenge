# from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Float
# from sqlalchemy import create_engine
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# convention = {
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# }
# metadata = MetaData(naming_convention=convention)

# Base = declarative_base(metadata=metadata)
# # Base.metadata.create_all(engine)

# engine = create_engine('sqlite:///restuarants.db')
# Session = sessionmaker(bind=engine)
# session = Session()

# # restaurant model
# class Restaurant(Base):
#     # create restaurant table
#     __tablename__ = "restaurants"
#     # add restaurant column
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     price = Column(Float, nullable=False)
    
#      # Define the relationship with Review explicitly
#     reviews = relationship("Review", back_populates="restaurant")
    
#     # make restaurant object readable
#     def __repr__(self):
#         return f'<Restaurant name:{self.name}, price:{self.price}>'
    
#     # return all reviews for a specific restaurant 
#     def restaurant_reviews(self):
#         reviews=session.query(Review).filter_by(restaurant_id=self.id).all()
#         return reviews
    
#     # return customers who have made reviews for a specific restaurant
#     def restaurant_customers(self):
#         reviews=session.query(Review).filter_by(restaurant_id=self.id).all()
#         return [review.customer for review in reviews]
    
#     # return most expensive restaurant
#     @classmethod
#     def fanciest_restaurants(cls):
#         restaurant=session.query(Restaurant).order_by(Restaurant.price.desc()).first()
#         return restaurant
    
#     # return all reviews for a given restaurant in a specific format
#     def all_reviews(self):
#         reviews = session.query(Review).filter_by(restaurant_id=self.id).all()
#         return [review.full_review() for review in reviews]
       
   
   

# class Customer(Base):
#     __tablename__ = "customers"
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
    
#     reviews = relationship("Review", back_populates="customer")
#     restaurants=relationship("Review",back_populates="customer",overlaps="reviews")
    
#  # make customer object readable
#     def __repr__(self):
#         return f"<Customer {self.first_name} {self.last_name}>"
    
#     # return all reviews for a specific customer
#     def customer_reviews(self):
#         reviews=session.query(Review).filter_by(customer_id=self.id).all()
#         return reviews
#     # return all restaurant reviewed for a specific customer
#     def customer_restaurants(self):
#         reviews=session.query(Review).filter_by(customer_id=self.id).all()
#         return [review.restaurant for review in reviews]
    
#     # returns customers full name
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
    
#     # return reviewed restaurant with highest rating for a specific customer
#     def favorite_restaurant(self):
#         review=session.query(Review).filter_by(customer_id=self.id).order_by(Review.star_rating.desc()).limit(1).first()
#         return review.restaurant
    

#     # adds review and makes it persist in the database
#     def add_review(self, restaurant, rating):
#       new_review = Review(
#         star_rating=rating,
#         restaurant_id=restaurant,
#          customer=self
#       )
#       session.add(new_review)
#       session.commit()
#       return "Review added successfully"
  
#   # delete review from the database
#     def delete_review(self, restaurant):
#       print(f"Deleting reviews for customer_id={self.id} and restaurant_id={restaurant}")
#       reviews = session.query(Review).filter_by(customer_id=self.id, restaurant_id=restaurant).all()
    
#       for review in reviews:
#         print(f"Deleting review with id={review.id}")
#         session.delete(review)
    
#       session.commit()
    
#       return "Reviews deleted successfully"

    
    
    
# class Review(Base):
#     __tablename__ = "reviews"

#     id = Column(Integer, primary_key=True)
#     star_rating = Column(Integer)
#     restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
#     customer_id = Column(Integer, ForeignKey('customers.id'))

#     # Define the relationships explicitly
#     restaurant = relationship("Restaurant", back_populates="reviews")
#     customer = relationship("Customer", back_populates="reviews")
    
#     # return customer for a specific review
#     def review_customer(self):
#         return self.customer

#     # return restaurant for a specific review
#     def review_restaurant(self):
#         return self.restaurant
    
#     # make review object readable
#     def __repr__(self):
#         return f"<Review, Star rating: {self.star_rating},customer id:{self.customer_id},restaurant_id:{self.restaurant_id}>"
    
#     # return review in a specific format
#     def full_review(self):
#         return f"Review for {self.restaurant.name} by {self.customer.full_name()}  : {self.star_rating} stars"



# # test add review and  delete review methods
# customer1 = session.query(Customer).filter_by(id=20).first() # change id to desired customer
# print(customer1.delete_review(42))
# customer2 = session.query(Customer).filter_by(id=10).first() # change id to desired customer
# print(customer2.add_review(18, 5))

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    # Define the 'restaurants' table
    __tablename__ = 'restaurants'

    # Define columns for the 'restaurants' table
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # Establish relationships with other tables
    reviews = relationship('Review', back_populates='restaurant')  # One-to-many relationship with 'reviews'
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants')  # Many-to-many relationship with 'customers'

class Customer(Base):
    # Define the 'customers' table
    __tablename__ = 'customers'

    # Define columns for the 'customers' table
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Establish relationships with other tables
    reviews = relationship('Review', back_populates='customer')  # One-to-many relationship with 'reviews'
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers')  # Many-to-many relationship with 'restaurants'
   
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Review(Base):
    # Define the 'reviews' table
    __tablename__ = 'reviews'

     # Define columns for the 'reviews' table
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    # Establish relationships with other tables
    restaurant = relationship('Restaurant', back_populates='reviews')  # Many-to-one relationship with 'restaurants'
    customer = relationship('Customer', back_populates='reviews')  # Many-to-one relationship with 'customers'