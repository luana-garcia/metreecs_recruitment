from typing import Dict, Literal

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Metreecs Stock Management System")

# Simulated database
product_stock_db: Dict[str, int] = {}
movements_db: list = []

# --- DATA MODEL ---

# Data model for product
class ProductStock(BaseModel):
    product_id: str = Field(..., description="Product ID", example="ABC123")
    quantity: int = Field(..., gt=-1, description="Quantity must be positive or zero", example=10)
    type: Literal["in", "out"] = Field(..., description="Movement type: 'in' or 'out'")

# Gentle welcome message for the Metreecs system
@app.get(
        "/",
        tags=["General"])
def read_root() -> Dict[str, str]:
    return {"Hello World": "Welcome to the Metreecs Stock Management System!"}

# --- ENDPOINTS ---

# Endpoint to get current stock of a product
@app.get(
        "/products/{product_id}/stock",
        tags=["Products"])
def read_product(product_id: str):
    # Check if product exists in the simulated database
    if product_id not in product_stock_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {product_id} not found!"
        )
    return {"product_id": product_id, "current_stock": product_stock_db[product_id]}

# Endpoint to register stock movements (inbound/outbound)
@app.post(
        "/movements",
        response_model=ProductStock,
        status_code=status.HTTP_201_CREATED,
        tags=["Movements"])
def register_movement(product: ProductStock) -> ProductStock:
    if product.product_id not in product_stock_db:
        product_stock_db[product.product_id] = 0

    # Update product stock
    if product.type == "out":
        if product_stock_db[product.product_id] >= product.quantity:
            product_stock_db[product.product_id] -= product.quantity
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"The product {product.product_id} is non-existent or has insufficient stock."
            )
    else:
        product_stock_db[product.product_id] += product.quantity

    # Update movements database
    movements_db.append(product.dict())

    return product