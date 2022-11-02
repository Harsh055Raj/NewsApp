
import email
from enum import unique
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Contact
import requests
from django.contrib import messages

API_KEY = '8547294386b24fb889d0c00e2b7152d1'

from django.contrib.auth import logout
from django.shortcuts import redirect


from django.shortcuts import redirect, render

from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/everything?q={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/everything?q={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context = {
        'articles' : articles
    }

    return render(request, 'home.html', context)

def login(request):
    return render(request, "login.html")

def logoutpage(request):
    logout(request)
    return redirect("home")



# def index(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)

#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             content = form.cleaned_data['content']
#             print("DASPODO")

#             html = render_to_string('templates/emails/contactform.html', {
#                 'name': name,
#                 'email': email,
#                 'content': content
#             })
#             print(html)
#             send_mail('The contact form subject', 'This is the message', 'agarwalsanchit08@gmail.com', ['hars09sp@gmail.com'], html_message=html)
#     else:
#         form = ContactForm()

#     return render(request, 'index.html', {
#         'form': form
#     })
    
from django.shortcuts import render, redirect
from . forms import SubscibersForm, MailMessageForm
from . models import Subscribers
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame
from newsapp import settings
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = SubscibersForm(request.POST)

        if form.is_valid():
            form.save()
            to = form.cleaned_data.get('email')
            # df = read_frame(email, fieldnames=['email'])
            # mail_list = df['email'].values.tolist()
         
            send_mail(
                'Welcome to Daily Shorts',
                'Hi, This is just a confirmation email, To let you know that you have subscribed to newsletter of Daily Shorts. You will be updated on this email if any new newsletter is published.'
                'Thank You,'
                'Team Daily Shorts' ,
                settings.EMAIL_HOST_USER,
                [to],
                fail_silently=False,
            )
            messages.success(request, 'Subscription Successful')
            return redirect('index')
    else:
        form = SubscibersForm()
    context = {
        'form': form,
    }
    return render(request, 'letter/index.html', context)


def mail_letter(request):
    emails = Subscribers.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)
    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Message has been sent to the Mail List')
            return redirect('mail-letter')
    else:
        form = MailMessageForm()
    context = {
        'form': form,
    }
    return render(request, 'letter/mail_letter.html', context)



def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()

    return render(request, 'contact.html')
