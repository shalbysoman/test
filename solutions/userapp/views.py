from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render
from peace_app.models import Book
# Create your views here.


def listbook(request):
    books = Book.objects.all()

    # < !--pagination -->

    paginator=Paginator(books, 4)
    page_number=request.GET.get('page')

    try:
        page = paginator.get_page(page_number)

    except EmptyPage:

        page = paginator.page(page_number.num_pages)

    # < !--end of pagination -->

    return render(request, 'user/userlist.html', {'books': books, 'page': page})


def detailsbook(request, book_id):
    book = Book.objects.get(id=book_id)

    return render(request, 'user/userdetails.html', {'book': book})

# __SEARCH BAR__#


def searchview(request):
    query = None
    books = None

    if 'q' in request.GET:

        query = request.GET.get('q')
        # book name and author search chydh find aavan#
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))

    else:
        books = []

    context = {'books': books, 'query': query}
    return render(request, 'user/usersearch.html', context)
