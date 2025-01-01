import uuid
from book import Book
class BookOperations:
    
    def __init__(self):
        """
        Initializes the BookOperations object.

        Attributes:
            books (list): A list to store all the books in the system.
        """
        self.books = []
    
    def add_book(self, 
             title: str, 
             author: str, 
             genre: str, 
             year_of_publication: int, 
             publisher: str, 
             page_count: int, 
             language: str, 
             price: float, 
             stock_quantity: int) -> None:
        """
        Adds a new book to the collection.

        Parameters:
            title (str): The title of the book.
            author (str): The author of the book.
            genre (str): The genre of the book.
            year_of_publication (int): The year the book was published.
            publisher (str): The publisher of the book.
            page_count (int): The total number of pages in the book.
            language (str): The language the book is written in.
            price (float): The price of the book.
            stock_quantity (int): The quantity of the book available in stock.

        Notes:
            A unique identifier (id) is automatically generated for each book 
            using the UUID library.
            
        Returns:
            None
        """
        id = int(uuid.uuid4().int % 1e15)
        book = Book(title,author,genre,year_of_publication,publisher,page_count,language,price,stock_quantity,id)
        self.books.append(book)

    def delete_book(self, title: str, author: str, id: int) -> str:
        """
        Deletes a book from the collection.

        Parameters:
            title (str): The title of the book to delete.
            author (str): The author of the book to delete.
            id (int): The unique identifier of the book to delete.

        Returns:
            str: A message indicating whether the book was successfully deleted or not found.
        """
        for book in self.books:
            if title == book.title and author == book.author and id == book.id:
                self.books.remove(book)
                return f"Book '{title}' by {author} deleted successfully."
        return f"Book '{title}' by {author} not found."
    
    def title_search(self, title: str) -> list:
        """
        Searches for books by their title and returns their indices.

        Parameters:
            title (str): The title of the book to search for.

        Returns:
            list: A list of indices of books that match the given title.
                Returns an empty list if no books are found.
        """
        return [i for i, book in enumerate(self.books) if title.lower() == book.title.lower()]