from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted")
print(f"Remaining books: {Book.objects.all()}")
