import uvicorn
from fastapi import FastAPI
from domains.book import Book
from domains.member import Member # Corretto singolare
from repositories.catalog import Catalog
from services.library_service import LibraryController
from api.routes import create_router # Devi importare la funzione!

app = FastAPI(title="Sistema Biblioteca Microservice")

# Inizializzazione dati (Mock data per test)
catalog = Catalog()
catalog.add_resource(Book("123", "Il Signore degli Anelli"))

library_service = LibraryController(catalog)
# Aggiungiamo un membro di test altrimenti il dizionario è vuoto
library_service.members[1] = Member("Mario Rossi", 1)

# Iniezione del servizio nel router
app.include_router(create_router(library_service))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)