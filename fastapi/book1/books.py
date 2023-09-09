from fastapi import FastAPI , Body

app = FastAPI()

BOOKS = [
    {"title" : "title 1" , "author" : "author 1" , "rating" : 5},
    {"title" : "title 2" , "author" : "author 2" , "rating" : 2},
    {"title" : "title 3" , "author" : "author 3" , "rating" : 4},
    {"title" : "title 4" , "author" : "author 4" , "rating" : 3},
    {"title" : "title 5" , "author" : "author 2" , "rating" : 4},
    {"title" : "title 6" , "author" : "author 6" , "rating" : 5},
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_books(book_title : str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
        
@app.get("/books/")
async def read_books_by_author(author : str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_rating_by_query(author : str , rating : int):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold() and \
            book.get("rating") == rating :
                books_to_return.append(book)
    return books_to_return

# post - to add a new book
@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)
    
# put is to update the existing book
@app.put("/books/update_book")
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == update_book.get("title").casefold():
            BOOKS[i] = update_book
            
# this is to delete existing book
@app.delete("/books/delete_book/")
async def delete_book_by_title(title : str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == title.casefold():
            BOOKS.pop(i)
            break