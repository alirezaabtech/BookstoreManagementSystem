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
             stock_quantity: int,
             show: bool) -> None:
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
            id (int): The unique identifier of the book.
            
        Returns:
            None
        """
        id = len(self.books) + 100000001
        book = Book(title,author,genre,year_of_publication,publisher,page_count,language,price,stock_quantity,id,show)
        self.books.append(book) 

    def update_book(self,
             index: int,
             title: str, 
             author: str, 
             genre: str, 
             year_of_publication: int, 
             publisher: str, 
             page_count: int, 
             language: str, 
             price: float, 
             stock_quantity: int,
             show: bool) -> None:
        """
        Updates all attributes of an existing book in the collection.

        Parameters:
            index (int): The index of the book in the collection.
            title (str): The new title of the book.
            author (str): The new author of the book.
            genre (str): The new genre of the book.
            year_of_publication (int): The new year the book was published.
            publisher (str): The new publisher of the book.
            page_count (int): The new total number of pages in the book.
            language (str): The new language the book is written in.
            price (float): The new price of the book.
            stock_quantity (int): The new quantity of the book available in stock.
            show (bool): Determines whether the book is visible to users.

        Returns:
            None
        
        Example:
        >>> library.update_book(0, "1984", "George Orwell", "Dystopian", 1949, "Secker & Warburg", 328, "English", 15.0, 80, True)
        """
        self.books[index].title = title
        self.books[index].author = author
        self.books[index].genre = genre
        self.books[index].year_of_publication = year_of_publication
        self.books[index].publisher = publisher
        self.books[index].page_count = page_count
        self.books[index].language = language
        self.books[index].price = price
        self.books[index].stock_quantity = stock_quantity
        self.books[index].show = show


    # def delete_book(self, title: str, author: str) -> list:
    #     """
    #     Deletes a book from the collection.

    #     Parameters:
    #         title (str): The title of the book to delete.
    #         author (str): The author of the book to delete.

    #     Returns:
    #         list: A list of indices of the books that were deleted.
    #             Returns an empty list if no books were deleted.
    #     """
    #     list_of_books = []
    #     for i, book in enumerate(self.books):
    #         if title == book.title and author == book.author:
    #             list_of_books.append(i)
    #             self.books.remove(book)
    #     return list_of_books
    
    def title_search(self, title: str) -> list:
        """
        Searches for books by their title and returns their indices.

        Parameters:
            title (str): The title of the book to search for.

        Returns:
            list: A list of indices of books that match the given title.
                Returns an empty list if no books are found.
        """
        return [i for i, book in enumerate(self.books) if title.lower() in book.title.lower()]

    def author_search(self, author: str) -> list:
        """
        Searches for books by their author and returns their indices.

        Parameters:
            author (str): The author of the book to search for.

        Returns:
            list: A list of indices of books that match the given author.
                Returns an empty list if no books are found.
        """
        return [i for i, book in enumerate(self.books) if author.lower() in book.author.lower()]
    
    def genre_search(self, genre: str) -> list:
        """
        Searches for books by their genre and returns their indices.

        Parameters:
            genre (str): The genre of the book to search for.

        Returns:
            list: A list of indices of books that match the given genre.
                Returns an empty list if no books are found.
        """
        return [i for i, book in enumerate(self.books) if genre.lower() == book.genre.lower()]
    
    def year_search(self, year: int) -> list:
        """
        Searches for books by their year of publication and returns their indices.

        Parameters:
            year (int): The year of publication of the books to search for.

        Returns:
            list: A list of indices of books that were published in the given year.
                Returns an empty list if no books are found.
        """
        return [i for i, book in enumerate(self.books) if year == book.year_of_publication]
    
    def publisher_search(self, publisher: str) -> list:
        """
        Searches for books by their publisher and returns their indices.

        Parameters:
            publisher (str): The publisher of the book to search for.

        Returns:
            list: A list of indices of books that match the given publisher.
                Returns an empty list if no books are found.
        """
        return [i for i, book in enumerate(self.books) if publisher.lower() in book.publisher.lower()]
    
    def language_search(self, language: str) -> list:
        """
        Searches for books by their language and returns their indices.

        Parameters:
            language (str): The language of the book to search for.

        Returns:
            list: A list of indices of books that match the given language.
                Returns an empty list if no books are found.
        """
        return [i for i, book in enumerate(self.books) if language.lower() == book.language.lower()]