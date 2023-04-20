from fastapi import FastAPI,Body

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


@app.post("/create_book")
async def create_book(book_request=Body(),):
    BOOKS.append(book_request)