# Testing CRUD Operations for the Item Model Using curl

This guide provides step-by-step instructions to test basic CRUD (Create, Read, Update, Delete) operations for the `Item` model in Django using curl.

---

## Prerequisites

1. Ensure you're in the correct folder:
   ```bash
   backend/   
2. Ensure the Django development server is running:
   ```bash
   python manage.py runserver

	2.	Use the following curl commands in your terminal to test each operation.
Step-by-Step Instructions
1. List All Items

Retrieve all items stored in the database:

curl -X GET http://127.0.0.1:8000/api/items/

Expected Response:

[
    {
        "id": 1,
        "name": "Test Item",
        "description": "This is a test item.",
        "price": 19.99
    }
]

2. Create a New Item

Add a new item to the database:

curl -X POST -H "Content-Type: application/json" \
-d '{"name": "Sample Item", "description": "A sample description", "price": 25.50}' \
http://127.0.0.1:8000/api/items/

Expected Response:

{
    "id": 2,
    "message": "Item created successfully!"
}

3. Retrieve a Specific Item

Retrieve an item by its ID:

curl -X GET http://127.0.0.1:8000/api/items/<id>/

Replace <id> with the ID of the item you want to retrieve.
Example:

curl -X GET http://127.0.0.1:8000/api/items/1/

Expected Response:

{
    "id": 1,
    "name": "Test Item",
    "description": "This is a test item.",
    "price": 19.99
}

4. Update an Item

Update an existing item by its ID:

curl -X PUT -H "Content-Type: application/json" \
-d '{"name": "Updated Item", "description": "Updated description", "price": 30.00}' \
http://127.0.0.1:8000/api/items/<id>/

Replace <id> with the ID of the item you want to update.
Example:

curl -X PUT -H "Content-Type: application/json" \
-d '{"name": "Updated Item", "description": "Updated description", "price": 30.00}' \
http://127.0.0.1:8000/api/items/1/

Expected Response:

{
    "message": "Item updated successfully!"
}

5. Delete an Item

Delete an item by its ID:

curl -X DELETE http://127.0.0.1:8000/api/items/<id>/

Replace <id> with the ID of the item you want to delete.
Example:

curl -X DELETE http://127.0.0.1:8000/api/items/1/

Expected Response:

{
    "message": "Item deleted successfully!"
}

Notes
	•	Replace <id> with the actual ID of the item you are working with.
	•	Ensure the Django development server is running at http://127.0.0.1:8000/ during testing.
	•	Use valid JSON format for POST and PUT requests.
