from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    desc: str
    rating: int

    def __init__(self, id, title, author, desc, rating):
        self.id = id
        self.title = title
        self.author = author
        self.desc = desc
        self.rating = rating

class BookRequest(BaseModel):
    id: Optional[int]=Field(title='id is not needed')
    title: str =Field(min_length=3)
    author: str=Field(min_length=1)
    desc: str=Field(min_length=1,max_length=100)
    rating: int=Field(gt=-1,lt=6)

    class Config:
        schema_extra={
            'example':{
            'title':'A new book',
            'author':'dini',
            'desc':'A new desc',
            'rating':5
        }
        }



BOOKS = [
     Book(1, 'computer science', 'dini', 'good book',4),
     Book(2, 'fast api', 'dini','great book', 5),
     Book(3, 'dsa', 'vivek', 'nice book', 4),
     Book(4, 'api1', 'adi', 'awesomr book', 5),
     Book(5, 'api2', 'akhil', 'good book', 4),
     Book(6, 'ap3', 'adi', 'not bad book', 3)
]



@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id:int):
    for book in BOOKS:
        if book.id== book_id:
            return book


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