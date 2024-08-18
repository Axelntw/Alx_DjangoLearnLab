import os
import sys
import django

# Add the project directory to the Python path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir)

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        # Using objects.filter(author=author)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")

def additional_queries():
    print("\nAdditional Queries:")
    
    # Count books by an author
    author = Author.objects.first()
    book_count = Book.objects.filter(author=author).count()
    print(f"Number of books by {author.name}: {book_count}")

    # Get all libraries that have a specific book
    book = Book.objects.first()
    libraries = Library.objects.filter(books=book)
    print(f"Libraries that have '{book.title}':")
    for library in libraries:
        print(f"- {library.name}")

    # Find librarians managing libraries with more than 1 book
    librarians = Librarian.objects.filter(library__books__count__gt=1).distinct()
    print("Librarians managing libraries with more than 1 book:")
    for librarian in librarians:
        print(f"- {librarian.name} ({librarian.library.name})")

if __name__ == "__main__":
    query_books_by_author("J.K. Rowling")
    list_books_in_library("New York Public Library")
    get_librarian_for_library("New York Public Library")
    additional_queries()
