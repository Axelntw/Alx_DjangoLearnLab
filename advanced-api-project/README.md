# API Views

## BookListView
- Endpoint: `/api/books/`
- Methods: GET, POST
- Description: Lists all books and allows creation of new books.
- Permissions: Read-only access for unauthenticated users, full access for authenticated users.

## BookDetailView
- Endpoint: `/api/books/<int:pk>/`
- Methods: GET, PUT, PATCH, DELETE
- Description: Retrieves, updates, or deletes a specific book.
- Permissions: Read-only access for unauthenticated users, full access for authenticated users.