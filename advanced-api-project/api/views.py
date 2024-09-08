from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
import rest_framework.filters as filters
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    API endpoint that allows books to be viewed, filtered, searched, and ordered.
    
    Filtering:
    - title: ?title=<title>
    - author name: ?author__name=<name>
    - publication year: ?publication_year=<year>
    
    Searching:
    - Search by title or author name: ?search=<query>
    
    Ordering:
    - Order by title: ?ordering=title or ?ordering=-title (descending)
    - Order by publication year: ?ordering=publication_year or ?ordering=-publication_year (descending)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
