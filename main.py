from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

# Данные о продуктах
sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

sample_products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]

# Конечная точка для получения информации о продукте
@app.get("/product/{product_id}")
async def get_product(product_id: int):
    for product in sample_products:
        if product["product_id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

# Конечная точка для поиска товаров
@app.get("/products/search")
async def search_products(keyword: str, category: Optional[str] = None, limit: Optional[int] = 10):
    filtered_products = [product for product in sample_products if keyword.lower() in product["name"].lower()]
    
    if category:
        filtered_products = [product for product in filtered_products if product["category"].lower() == category.lower()]
    
    return filtered_products[:limit]
