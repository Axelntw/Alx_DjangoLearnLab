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
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")

def additional_queries():
    print("\nAdditional Queries:")
    
    # Get all books in a library using reverse relation
    library = Library.objects.first()
    if library:
        books = library.books.all()
        print(f"Books in {library.name} (using reverse relation):")
        for book in books:
            print(f"- {book.title}")
    
    # Find libraries with no books
    empty_libraries = Library.objects.filter(books__isnull=True)
    print("Libraries with no books:")
    for library in empty_libraries:
        print(f"- {library.name}")

    # Find authors with more than one book
    authors_with_multiple_books = Author.objects.annotate(book_count=models.Count('books')).filter(book_count__gt=1)
    print("Authors with more than one book:")
    for author in authors_with_multiple_books:
        print(f"- {author.name}")

    # Get the latest added book
    latest_book = Book.objects.latest('id')
    print(f"Latest added book: {latest_book.title} by {latest_book.author.name}")

if __name__ == "__main__":
    query_books_by_author("J.K. Rowling")
    list_books_in_library("New York Public Library")
    get_librarian_for_library("New York Public Library")
    additional_queries()
