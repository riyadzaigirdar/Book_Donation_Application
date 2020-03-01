from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        book = request.POST['book']
        book_id = request.POST['book_id']
        name = request.POST['name']
        try:
            phone = request.POST['phone']
        except ValueError:
            messages.error(request, 'Add Phone Number')
            return redirect('/book/'+book_id)
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']
        if User.is_authenticated:
            has_contacted = Contact.objects.all().filter(
                book_id=book_id, user_id=request.user.id)
            if has_contacted:
                messages.warning(request, 'You have already made contact')
                return redirect('/books/' + book_id)

        contact = Contact(book=book, book_id=book_id, name=name, email=email,
                          phone=phone, message=message, user_id=user_id)
        contact.save()

        send_mail(
            'Inquiry About ' + book + ' Book',
            'Yoy have successfully inquired about the ' +
            book + ' book, An admin will get to you :D',
            'riyadzaigir280@gmail.com',
            [email],
            fail_silently=False,
        )

        messages.success(request, "This inquiry has been successfully made")
        return redirect('/books/' + book_id)


def delete(request, id):
    contact = get_object_or_404(Contact, pk=id)
    contact.delete()
    return redirect('dashboard')
