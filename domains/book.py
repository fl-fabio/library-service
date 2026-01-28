class Book:
  def __init__(self, isbn: str, title: str):
    self.isbn = isbn
    self.title = title
    self.is_loaned = False
  
  def loan(self):
    if self.is_loaned:
      raise ValueError(f"Il libro '{self.title}' è già in prestito.")
    self.is_loaned = True
    
  def return_book(self):
    self.is_loaned = False

  def new_method(self):
    pass

