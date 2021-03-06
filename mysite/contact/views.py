from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from mysite.forms import ContactForm

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
        form = ContactForm(
            initial = {'subject':"I love your Site!"}
        )
    return render_to_response('contact_form.html',locals())
