from urls import db

# Clear it all out

db.drop_all()

# Set it back up

db.create_all()
