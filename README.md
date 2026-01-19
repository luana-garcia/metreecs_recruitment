# Metreecs Recruitment Test

Candidate: Luana de Queiroz Garcia

I built a small backend system with FastAPI following the requirements from the email.

```
Backend

Créer un petit backend avec 2 endpoints REST

POST /movements - Enregistrer un mouvement de stock : 
format du payload accepté:
{ "product_id": "ABC123", "quantity": 50, "type": "in" | "out" }

GET /products/{product_id}/stock - Obtenir le stock actuel d'un produit

format du payload retourné:
{ "product_id": "ABC123", "current_stock": 150 }
```

To run the project you can activate a virtual environment and install fastapi.
After, use the following command to run the local server:
```
fastapi dev main.py
```

The server is normally started in `http://127.0.0.1:8000`.

You can access the docs on `http://127.0.0.1:8000/docs`.

Thanks for the attention!