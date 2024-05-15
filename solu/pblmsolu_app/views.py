from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Book
# Create your views here.


def list_book(request):
    books = Book.objects.all()

    # < !--pagination -->

    paginator=Paginator(books, 4)
    page_number=request.GET.get('page')

    try:
        page = paginator.get_page(page_number)

    except EmptyPage:

        page = paginator.page(page_number.num_pages)

    # < !--end of pagination -->

    return render(request, 'userlist.html', {'books': books, 'page': page})


def details_book(request, book_id):
    book = Book.objects.get(id=book_id)

    return render(request, 'userdetails.html', {'book': book})


# __SEARCH BAR__#

def search_view(request):
    query = None
    books = None

    if 'q' in request.GET:

        query = request.GET.get('q')
        # book name and author search chydh find aavan#
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))


    else:
        books = []


    context = {'books': books, 'query': query}
    return render(request, 'usersearch.html', context)
