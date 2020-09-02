# from sqlalchemy import Column, ForeignKey, String
# from sqlalchemy.dialects.mysql import INTEGER
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
from app import db
from app import login
# from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Base = declarative_base()
# metadata = Base.metadata
# db = SQLAlchemy()
class User(UserMixin, db.Model):
    # """User account model."""
    __tablename__ = 'users'
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(100),
                     nullable=False,
                     unique=False)
    email = db.Column(db.String(40),
                      unique=True,
                      nullable=False)
    password = db.Column(db.String(200),
                         primary_key=False,
                         unique=False,
                         nullable=False)
    created_on = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=True)
    last_login = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=True)
    avatar = db.Column(db.String(200),
                           unique=False,
                           nullable=True)
    bio = db.Column(db.String(500),
                           unique=False,
                           nullable=True)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.name)

class Set_SQL(db.Model):
    __tablename__ = 'sets'

    set_id = db.Column(db.INTEGER(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500))
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False)
    public = db.Column(db.Boolean, nullable=False)

    user = db.relationship('User')

class Card_SQL(db.Model):
    __tablename__ = 'cards'
    __table_args__ = {'extend_existing': True}

    card_ID = db.Column(db.INTEGER(), primary_key=True)
    set_id = db.Column(db.ForeignKey('sets.set_id'), nullable=False, index=True)
    card_order = db.Column(db.INTEGER())

    set = db.relationship('Set_SQL')


class Side_SQL(db.Model):
    __tablename__ = 'sides'
    __table_args__ = {'extend_existing': True}

    side_id = db.Column(db.INTEGER(), primary_key=True)
    set_id = db.Column(db.ForeignKey('sets.set_id'), nullable=False, index=True)
    name = db.Column(db.String(255))
    side_order = db.Column(db.INTEGER())

    set = db.relationship('Set_SQL')


class Cell_SQL(db.Model):
    __tablename__ = 'cells'
    __table_args__ = {'extend_existing': True}

    cell_id = db.Column(db.INTEGER(), primary_key=True)
    card_id = db.Column(db.ForeignKey('cards.card_ID', ondelete="CASCADE"), nullable=False, index=True)
    side_id = db.Column(db.ForeignKey('sides.side_id', ondelete="CASCADE"), nullable=False, index=True)
    info = db.Column(db.String(1000))

    card = db.relationship('Card_SQL', cascade="delete")
    side = db.relationship('Side_SQL', cascade="delete")

@login.user_loader
def load_user(id):
    return User.query.get(int(id))