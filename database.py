from flask_sqlalchemy import SQLAlchemy
from app import app

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipies.sqlite3'

db = SQLAlchemy(app)

class Recipies(db.Model):
   id = db.Column('recipeId', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   ingredients = db.Column(db.Dictionary(50))  
   instructions = db.Column(db.Text)

   def __init__(self, name, ingredients, instructions):
        self.name = name
        self.city = ingredients
        self.addr = instructions

class Ingredients(db.Model):
    id = db.Column('ingredientsId', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    description = db.column(db.Text)