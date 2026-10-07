from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas, crud
from app.database import engine, get_db

# Create database tables automatically
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Product Management REST API",
    description="A CRUD API for managing products built with FastAPI, SQLAlchemy, and Pydantic.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Product Management REST API",
        "docs_url": "http://127.0.0.1:8000/docs"
    }

# 1. CREATE
@app.post("/api/v1/products", response_model=schemas.ProductResponse, status_code=status.HTTP_201_CREATED, tags=["Products"])
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    """Create a new product record."""
    return crud.create_product(db=db, product=product)

# 2. READ ALL
@app.get("/api/v1/products", response_model=List[schemas.ProductResponse], tags=["Products"])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve a paginated list of products."""
    return crud.get_products(db, skip=skip, limit=limit)

# 3. READ ONE
@app.get("/api/v1/products/{product_id}", response_model=schemas.ProductResponse, tags=["Products"])
def read_product(product_id: int, db: Session = Depends(get_db)):
    """Retrieve details of a specific product by ID."""
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {product_id} not found"
        )
    return db_product

# 4. UPDATE
@app.put("/api/v1/products/{product_id}", response_model=schemas.ProductResponse, tags=["Products"])
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    """Update an existing product by ID."""
    db_product = crud.update_product(db=db, product_id=product_id, product_update=product)
    if db_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {product_id} not found"
        )
    return db_product

# 5. DELETE
@app.delete("/api/v1/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Products"])
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """Delete a product by ID."""
    db_product = crud.delete_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {product_id} not found"
        )
    return None