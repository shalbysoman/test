from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from winwinapp.models import Book
from user.models import Cart, CartItem


# Create your views here.


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


#def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)

    if book.quantity >0:

        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, item_created=CartItem.objects.get_or_create(cart=cart, book=book)

        if not item_created:
            # cartil ulla items nte quantity kittan
            cart_item.quantity +=1
            cart_item.save()

    return redirect('viewcart')


# def view_cart(request):

    cart,created=Cart.objects.get_or_create(user=request.user)

    cart_items=cart.cartitem_set.all()
    # cart itemil cart m ayitt related ayt kidakkunna objects kanan
    cart_item=CartItem.objects.all()
    total_price=sum(item.book.price * item.quantity for item in cart_items)
    total_items=cart_items.count()

    context={'cart_items': cart_items, 'cart_item': cart_item, 'total_price': total_price, 'total_items': total_items}

    return render('user/cart.html', context)


def increase_quantity(request, item_id):
    cart_item=CartItem.objects.get(id=item_id)

    if cart_item.quantity <cart_item.book.quantity:
        cart_item.quantity += 1
        cart_item.save()

    return render('add_to_cart')


def decrease_quantity(request,item_id):
    cart_item = CartItem.objects.get(id=item_id)

    if cart_item.quantity >1:
        cart_item.quantity -= 1
        cart_item.save()

    return render('add_to_cart')


def remove_from_cart(request,item_id):
    try:
        cart_item=CartItem.objects.get(id=item_id)
        cart_item.delete()

    except cart_item.DoesNotExist:
        pass

    return render('view_cart')



def viewcart(request):
    cart = Cart.objects.all()

    return render(request, 'user/cart.html', {'cart': cart})


def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)

    if book.quantity >0:

        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, item_created=CartItem.objects.get_or_create(cart=cart, book=book)

        if not item_created:
            # cartil ulla items nte quantity kittan
            cart_item.quantity +=1
            cart_item.save()


    return render(request, 'user/cart.html', {'book': book})


