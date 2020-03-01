from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .choices import category_choices, book_choices, author_choices, address_choices
from .models import Book, Category


def index(request):
    books = Book.objects.all()
    paginator = Paginator(books, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'books': page_obj,

        'category_choices': category_choices,
        'author_choices': author_choices,
        'address_choices': address_choices,
        'book_choices': book_choices,
    }

    return render(request, 'books/books.html', context)


def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    context = {
        'book': book
    }
    return render(request, 'books/book.html', context)


def search(request):
    query = Book.objects.order_by('-list_date')

    if 'category_name' in request.GET:
        category_name = str(request.GET['category_name'])
        print(category_name)
        if category_name:
            queryset_list = query.filter(category__id__iexact=category_name)

    if 'book_name' in request.GET:
        book_name = request.GET['book_name']

        if book_name:
            queryset_list = query.filter(name__iexact=book_name)

    if 'author_name' in request.GET:
        author_name = request.GET['author_name']

        if author_name:
            queryset_list = query.filter(author__iexact=author_name)

    if 'address_name' in request.GET:
        address_name = request.GET['address_name']

        if address_name:
            queryset_list = query.filter(address__iexact=address_name)

    if 'des' in request.GET:
        des = request.GET['des']

        if des:
            queryset_list = query.filter(description__icontains=des)

    context = {
        'category_choices': category_choices,
        'author_choices': author_choices,
        'address_choices': address_choices,
        'book_choices': book_choices,
        'books': queryset_list,
        'values': request.GET
    }

    return render(request, 'books/search.html', context)
