from domains.book import Book

class Catalog:
  def __init__(self):
    self._books: dict[str, Book] = {}
  
  def add_resource(self, book: Book):
    self._books[book.isbn] = book
    
  def search_by_title(self, query: str):
    results = []
    
    for b in self._books.values():
      if query.lower() in b.title.lower():
        results.append(b)
    return results
  
  '''
  def search_by_title(self, query: str):
  	return [b for b in self._books.values() if query.lower() in b.title.lower()]
  '''
    
  def get_by_isbn(self, isbn: str) -> Book:
    return self._books.get(isbn)