from flask import Flask, request
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)

data = [
    {'id':1,'book':'The Joy of Work','movie':'Harry Potter'},
    {'id':2,'book':'Developemnt With Dignity','movie':'Spider Man'},
    {'id':3,'book':'What is Mathematics?','movie':'Maze Runner'},
    {'id':4,'book':'Zero to One','movie':'Percy Jackson'}
]

def find_book(bookid):
    for book in data:
        if book['id'] == bookid:
            return book
    return None

class MovieBookDB(Resource):
    def get(self):
        return data
    def post(self):
        new_entry = {
            "id":len(data)+1,
            "book": 'How to not give a Fuck',
            "movie": "Batman"
        }
        data.append(new_entry)
        return new_entry, 201
    
class BookRe(Resource):
    def get(self, bookid):
        book= find_book(bookid)
        if book:
            return book
        return {"message": "Book not found"}, 404
    def put(self, bookid):
        book = find_book(bookid)
        if book:
            book['movie']= request.json['movie']
            book['book']= request.json['book']
            return book
        return {'message':"Book not found"}
    def delete(self, bookid):
        global data
        data = [book for book in data if book['id']!=bookid]
        return {"message": "person deleted successfully"}, 200
    def post(self, bookid):
        new_entry = {
            "id":len(data)+1,
            "book": 'How to not give a Fuck',
            "movie": "Batman"
        }
        data.append(new_entry)
        return new_entry, 201
    
api.add_resource(MovieBookDB,'/moviebook')
api.add_resource(BookRe,'/moviebook/<int:bookid>')


if __name__ == '__main__':
    app.run(debug=True)