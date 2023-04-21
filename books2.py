from typing import Optional

from fastapi import FastAPI, Path,Query, HTTPException
from pydantic import BaseModel,Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    desc: str
    rating: int
    publish_date: int

    def __init__(self, id, title, author, desc, rating,publish_date):
        self.id = id
        self.title = title
        self.author = author
        self.desc = desc
        self.rating = rating
        self.publish_date=publish_date

class BookRequest(BaseModel):
    id: Optional[int]=Field(title='id is not needed')
    title: str =Field(min_length=3)
    author: str=Field(min_length=1)
    desc: str=Field(min_length=1,max_length=100)
    rating: int=Field(gt=-1,lt=6)
    publish_date: int=Field(gt=1999,lt=2032)

    class Config:
        schema_extra={
            'example':{
                'title':'A new book',
                'author':'dini',
                'desc':'A new desc',
                'rating':5,
                'publish_date':2029
        }
        }



BOOKS = [
     Book(1, 'computer science', 'dini', 'good book',4,2030),
     Book(2, 'fast api', 'dini','great book', 5,2030),
     Book(3, 'dsa', 'vivek', 'nice book', 4,2029),
     Book(4, 'api1', 'adi', 'awesomr book', 5,2028),
     Book(5, 'api2', 'akhil', 'good book', 4,2027),
     Book(6, 'ap3', 'adi', 'not bad book', 3,2026)
]



@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id:int = Path(gt=0)):
    for book in BOOKS:
        if book.id== book_id:
            return book
    raise HTTPException(status_code=404,detail="Item Not Found")

@app.get("/books/")
async def read_by_rating(book_rating: int =Query(gt=0,lt=6)):
    books_to_return=[]
    for book in BOOKS:
        if book.rating==book_rating:
            books_to_return.append(book)
    return books_to_return


@app.get("/books/publish/")
async def read_by_publish_date(publish_date:int =Query(gt=1999,lt=2032)):
    books_to_return=[]
    for book in BOOKS:
        if book.publish_date==publish_date:
            books_to_return.append(book)
    return books_to_return


@app.post("/create_book")
async def create_book(book_request:BookRequest):
    new_book=Book(**book_request.dict())
    BOOKS.append(book_id(new_book))

def book_id(book:Book):
    if len(BOOKS)> 0:
        book.id =BOOKS[-1].id+1
    else:
        book.id=1
    return book


@app.put("/books/update_book")
async def update_book(book:BookRequest):
    change=False
    for i in range(len(BOOKS)):
        if BOOKS[i].id==book.id:
            BOOKS[i]=book
            change=True
    if not change:
        raise HTTPException(status_code=404,detail="Item Not Found")


@app.delete("/books/{book_id}")
async def delete_book(book_id:int =Path(gt=0)):
    change = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id==book_id:
            BOOKS.pop(i)
            change = True
            break
    if not change:
        raise HTTPException(status_code=404,detail="Item Not Found")