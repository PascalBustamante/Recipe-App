from email import parser
#from typing_extensions import Required
from urllib.parse import ParseResultBytes
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import ast
import os

app = Flask(__name__)
api = Api(app)

basedir =  os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Recipies(db.Model):
   id = db.Column('recipeId', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   ingredients = db.Column(db.String(50))  
   instructions = db.Column(db.Text)

   def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
    
   def __repr__(self):
        return f'<Recipies {self.name}>'

class Ingredients(db.Model):
    id = db.Column('ingredientsId', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    description = db.column(db.Text)




class Recipies(Resource):

    def get(self):

        pass
    
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('recipeId', type=int, required=True)         #unique identifier
        parser.add_argument('recipeName', type=str, required=True)
        parser.add_argument('ingredients', type=dict, required=True)
        parser.add_argument('instructions', type=str)

        args = parser.parse_args()

        #because we are using csv to store data:
        df = pd.DataFrame({
            'recipeId': args['recipeId'],
            'recipeName': args['recipeName'],
            'ingredients': args['ingredients'],
            'instructions': args['instructions']
        })

        #load and add obj to csv

        #check if recipe already exits, might be able to add a recipe with the same name

    def put(self):
        parser = reqparse.RequestParser()

        parser.add_argument('recipeId', type=int, required=True)    #add extra args yo change?
        args = parser.parse_args()                                  #the ans is to not require the other fields and updates the ones that were inputed using a loop?
        #load csv
        #check csv contains id else return error msg

    def delete(self):
        parser = reqparse.RequestParser()                           # this might not be the best way to go since all we need is an id

        parser.add_argument('recipeId', type=int, required=True)
        args = parser.parse_args()

        #load csv
        #if/else to check if id exists

class Ingredients(Resource):                                        #there might be a better name?

    def get(self):
        pass

    def post(self):
        parser = reqparse.RequestParser

        parser.add_argument('ingredientId', type=int, required=True)
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('description', type=str)
        parser.add_argument('', type=str, required=True)

        pass

    def put(self):
        pass

    def delete(self):
        pass

    pass

api.add_resource(Recipies, '/recipies')
api.add_resource(Ingredients, '/ingredients')

if __name__ == '__main__':
    app.run()