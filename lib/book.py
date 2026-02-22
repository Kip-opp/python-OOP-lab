#!/usr/bin/env python3

class Book:
    """A class representing a book with title and page count.
    
    Attributes:
        title (str): The title of the book (required).
        page_count (int): The number of pages in the book (must be an integer).
    """
    
    def __init__(self, title, page_count):
        """Initialize a Book instance with title and page count.
        
        Args:
            title (str): The title of the book.
            page_count (int): The number of pages in the book.
        """
        self.title = title
        self._page_count = page_count  # Private attribute for property access
    
    @property
    def page_count(self):
        """Get the page count of the book."""
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        """Set the page count with validation.
        
        Args:
            value (int): The new page count.
            
        Raises:
            (Prints warning): If value is not an integer.
        """
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        """Simulate turning a page by printing a message."""
        print("Flipping the page...wow, you read fast!")
