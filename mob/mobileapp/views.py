from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm
from .models import Book
# Create your views here.


def createbook(request):
    books = Book.objects.all()
    if request.method == "POST":

        form = BookForm(request.POST, request.FILES)
        print(form)

        if form.is_valid():
            form.save()

            return redirect('/')

    else:
        form = BookForm()

    return render(request, 'admin/book.html', {'form': form, 'books': books})


def create_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')

    else:
        form = AuthorForm()

    return render(request, 'admin/author.html', {'form': form})


class EmptyPAGE:
    pass


def listbook(request):
    books = Book.objects.all()

    # < !--pagination -->

    paginator = Paginator(books, 4)
    page_number = request.GET.get('page')

    try:
        page = paginator.get_page(page_number)

    except EmptyPage:

        page = paginator.page(page_number.num_pages)

    # < !--end of pagination -->

    return render(request, 'admin/list.html', {'books': books, 'page': page})


def detailsbook(request, book_id):
    book = Book.objects.get(id=book_id)

    return render(request, 'admin/details.html', {'book': book})


def updatebook(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":

        form = BookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            form.save()

            return redirect('/')

    else:
        form = BookForm(instance=book)
    return render(request, 'admin/update.html', {'form': form})


def deletebook(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('/')

    return render(request, 'admin/delete.html', {'book': book})


def index(request):
    return render(request, 'admin/base.html')

# __SEARCH BAR__#


def search_book(request):
    query = None
    books = None

    if 'q' in request.GET:

        query = request.GET.get('q')
        # book name and author search chydh find aavan#
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))

    else:
        books = []

    context = {'books': books, 'query': query}
    return render(request, 'admin/search.html', context)
