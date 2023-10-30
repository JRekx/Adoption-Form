from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Database model for pets
class Pet(db.Model):
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    available = db.Column(db.Boolean, nullable=False, default=True)
    notes = db.Column(db.Text)

    # Method to get the image URL, defaults to None if photo_url is not provided
    def image_url(self):
        return self.photo_url or None
