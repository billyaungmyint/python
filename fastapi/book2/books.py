from fastapi import FastAPI
from pydantic import BaseModel , Field

app = FastAPI()

class Book:
    id : int
    title : str
    author : str
    category : str
    description : str
    rating : int
    
    def __init__(self , id , title , author , category , description , rating):
        self.id = id
        self.title = title
        self.author = author
        self.category = category
        self.description = description
        self.rating = rating
        
BOOKS = [
    Book(1,"Title One" , "Author One" , "Math" , "Very good math book" , 5),
    Book(1,"Title Two" , "Author Two" , "Science" , "Good science textbook" , 4),
    Book(1,"Title Three" , "Author Three" , "Science" , "Bad science book" , 2),
    Book(1,"Title Four" , "Author Four" , "History" , "Ok History class book" , 3),
    Book(1,"Title Five" , "Author Four" , "Geography" , "Good Geo lessons" , 4),
    Book(1,"Title Six" , "Author Two" , "Literature" , "Very bad literature book" , 1),
]

   
@app.get("/books")
async def get_all_books():
    return BOOKS

@app.get("/hi")
def greet(who):
    return f"Hello? {who}?"
