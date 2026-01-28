from domains.member import Member
from repositories.catalog import Catalog

class LibraryController:
    def __init__(self, catalog: Catalog):
        self.catalog = catalog
        self.members: dict[int, Member] = {}
    
    def register_loan(self, member_id: int, isbn: str):
        member = self.members.get(member_id)
        book = self.catalog.get_by_isbn(isbn)
        
        if not member:
            raise ValueError("Membro non trovato")
        if not book:
            raise ValueError("Libro non trovato nel catalogo")
        
        member.take_book(book)
        return f"Prestito ok: {book.title} a {member.name}"
  
    def deregister_loan(self, member_id: int, isbn: str):
        member = self.members.get(member_id)
        book = self.catalog.get_by_isbn(isbn)
    
        if not member:
            raise ValueError("Membro non trovato")
        if not book:
            raise ValueError("Libro non trovato nel catalogo")
      
        member.release_book(book)
        return f"Libro restituito: {book.title} da {member.name}"
    
    def get_all_loans(self):
        all_loans = []
        for m_id, member in self.members.items():
            for book in member.borrowed_books:
                all_loans.append({          
                "member_id": m_id,
                "member_name": member.name,
                "isbn": book.isbn,
                "title": book.title
                })
        return all_loans