# 🛍️ Product CRUD API with Filters - Django

This is a simple Django-based backend API that supports:

- Bulk creation of products via POST
- Fetching products with powerful filters:
  - By Category
  - By Sold Status
  - By Title (search)
  - By Price Range (minPrice, maxPrice)

---

## 🔧 Tech Stack

- Python 3.x
- Django
- SQLite (or your configured database)

---

## 🚀 How to Run

### 1. Clone the repo

```bash
git clone https://github.com/shashankkumar8558/Product-crud-endpoint.git
cd Product-crud-endpoint

make migrations
python manage.py migrate

run server
python manage.py runserver


API ENDPOINTS

Add products in bulk
/products
send a json array of product object

Fetch products with filters
example Request
GET /products?category=Electronics&sold=true&minPrice=100&title=gam


Filters are optional. If you don't pass any, you'll get all products.
You can pass multiple categories.
Title search is case-insensitive: title=iphone will match iPhone, IPHONE, etc.
