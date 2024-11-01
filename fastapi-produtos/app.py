from fastapi import FastAPI
from models.product import Product

data = [
	Product(id=1, name="Smartphone", description="A very cool smartphone.", price=999.99),
	Product(id=2, name="Tablet", description="A great tablet.", price=399.99),
	Product(id=3, name="Laptop", description="A powerful laptop.", price=899.99),
]

app = FastAPI()

@app.get("/api/products")
async def get_products():
	return data

@app.get("/api/products/{id}")
def get_product_by_id(id: int):
    for product in data:
        if product.id == id:
            return product
    return {"message": "Nenhum produto encontrado com o ID fornecido"}
