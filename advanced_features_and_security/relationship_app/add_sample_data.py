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

def add_sample_data():
    # Create authors
    rowling = Author.objects.create(name="J.K. Rowling")
    tolkien = Author.objects.create(name="J.R.R. Tolkien")

    # Create books
    harry_potter = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=rowling)
    lotr = Book.objects.create(title="The Lord of the Rings", author=tolkien)

    # Create library
    library = Library.objects.create(name="New York Public Library")
    library.books.add(harry_potter, lotr)

    # Create librarian
    Librarian.objects.create(name="John Doe", library=library)

    print("Sample data added successfully!")

if __name__ == "__main__":
    add_sample_data()
