from urls import db
from urls.models.url import Url

# Clear it all out

db.drop_all()

# Set it back up

db.create_all()
