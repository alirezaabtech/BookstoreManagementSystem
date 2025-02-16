class Book:
    def __init__(self, 
             title: str, 
             author: str, 
             genre: str, 
             year_of_publication: int, 
             publisher: str, 
             page_count: int, 
             language: str, 
             price: float, 
             stock_quantity: int,
             id: int,
             show: bool) -> None:
        """
        Initializes a new Book object.

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
        """    
        self.title = title
        self.author = author
        self.genre = genre
        self.year_of_publication = year_of_publication
        self.publisher = publisher
        self.page_count = page_count
        self.language = language
        self.price = price
        self.stock_quantity = stock_quantity
        self.id = id
        self.show = show