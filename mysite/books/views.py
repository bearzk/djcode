from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from mysite.books.models import Book
from mysite.forms import ContactForm

def search(request):
    error = False
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            error = 1
            return render_to_response('search.html', locals())
        elif len(query) > 40:
            error = 2
            return render_to_response('search.html', locals())
        else:
            error = 3
            books = Book.objects.filter(title__icontains=query)
            return render_to_response('search.html',locals())
    else:
        return render_to_response('search.html',locals())

def contact(request):
    if request.method == 'post':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email','noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact_form.html',locals())
