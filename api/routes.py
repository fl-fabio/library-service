from fastapi import APIRouter, HTTPException
from typing import List
from services.library_service import LibraryController

def create_router(library_service: LibraryController):
    router = APIRouter()

    @router.post("/loans/{member_id}/{isbn}")
    def loan_endpoint(member_id: int, isbn: str):
        try:
            message = library_service.register_loan(member_id, isbn)
            return {"status": "success", "message": message}
        except (ValueError, PermissionError) as e:
            raise HTTPException(status_code=400, detail=str(e))

    @router.delete("/loans/{member_id}/{isbn}") # Aggiunto lo slash iniziale
    def return_endpoint(member_id: int, isbn: str):
        try:
            message = library_service.deregister_loan(member_id, isbn)
            return {"status": "success", "message": message}
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))
        except Exception as e:
            # Corretto errore di battitura 'deail' -> 'detail'
            raise HTTPException(status_code=400, detail=str(e))

    @router.get("/loans")
    def list_loans_endpoint():
        loans = library_service.get_all_loans()
        if not loans:
            return {"status": "success", "message": "Nessun prestito attivo", "data": []}
        return {"status": "success", "count": len(loans), "data": loans}

    @router.get("/loans/{member_id}")
    def member_loans_endpoint(member_id: int):
        member = library_service.members.get(member_id)
        if not member:
            raise HTTPException(status_code=404, detail="Membro non trovato")

        books = [{"isbn": b.isbn, "title": b.title} for b in member.borrowed_books]
        return {
            "member_name": member.name,
            "borrowed_count": len(books),
            "books": books
        }
        
    return router