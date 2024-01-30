from dogmanager import db 


class User(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    user_firstname = db.Column(db.String(25), unique=True, nullable=False)
    user_lastname = db.Column(db.String(25), unique=True, nullable=False)
    user_email = db.Column(db.String(50), unique=True, nullable=False)
    user_phone_number = db.Column(db.String(50), unique=True, nullable=False)
    dogs = db.relationship("Dog", backref="user", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.user_firstname


class Dog(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    dog_name = db.Column(db.String(25), unique=True, nullable=False)
    dog_age = db.Column(db.Date, nullable=False)
    dog_image = db.Column(db.LargeBinary)
    dog_description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"#{self.id} - Dog: {self.dog_name} | Description: {self.dog_description}"