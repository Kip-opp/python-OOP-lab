#!/usr/bin/env python3

class Coffee:
    """A class representing a coffee with size and price.
    
    Attributes:
        size (str): The size of the coffee (must be "Small", "Medium", or "Large").
        price (float): The price of the coffee.
    """
    
    # Valid coffee sizes
    VALID_SIZES = ["Small", "Medium", "Large"]
    
    def __init__(self, size, price):
        """Initialize a Coffee instance with size and price.
        
        Args:
            size (str): The size of the coffee.
            price (float): The price of the coffee.
        """
        self._size = size  # Private attribute for property access
        self.price = price
    
    @property
    def size(self):
        """Get the size of the coffee."""
        return self._size
    
    @size.setter
    def size(self, value):
        """Set the coffee size with validation.
        
        Args:
            value (str): The new coffee size.
            
        Raises:
            (Prints warning): If value is not one of the valid sizes.
        """
        if value in self.VALID_SIZES:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
    
    def tip(self):
        """Simulate tipping by printing a message and increasing price by 1."""
        print("This coffee is great, here’s a tip!")
        self.price += 1
