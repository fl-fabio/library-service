from typing import List
from .book import Book

class Member:
  def __init__(self, name: str, member_id: int):
    self.name = name
    self.member_id = member_id
    self.borrowed_books: List[Book] = []
    
  def take_book(self, book: Book):
    if len(self.borrowed_books) >= 3:
      raise PermissionError(f"{self.name} ha già raggiunto il limite di 3 libri.")
    book.loan()
    self.borrowed_books.append(book)
    
  def release_book(self, book: Book):
    if book in self.borrowed_books:
      book.return_book()
      self.borrowed_books.remove(book)