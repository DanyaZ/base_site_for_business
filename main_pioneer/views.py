from django.shortcuts import render, redirect
from django.views.generic.base import View
from .forms import *
from .models import *
from .models import Blog as BlogModel
from time import time
from datetime import datetime, date
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import ugettext_lazy as _

language = _('rus')


def convert_date():
    day = str(datetime.today().strftime("%d"))
    month = str(datetime.today().strftime("%m"))
    year = str(datetime.today().strftime("%Y"))
    month_ru = {
        '01': 'января',
        '02': 'февраля',
        '03': 'марта',
        '04': 'апреля',
        '05': 'мая',
        '06': 'июня',
        '07': 'июля',
        '08': 'августа',
        '09': 'сентября',
        '10': 'октября',
        '11': 'ноября',
        '12': 'декабря'
    }

    month_en = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }

    date_ru = day + ' ' + month_ru[month] + ' ' + year + ' ' + 'года'
    date_en = month_en[month] + ' ' + day + ', ' + year

    return [date_ru, date_en]


class Main(View):
    def get(self, request):
        news = BlogModel.objects.all().filter(language_ru=True).order_by('-url')[:6]
        news_en = BlogModel.objects.all().filter(language_ru=False).order_by('-url')[:6]
        form = SubscriptionForm()

        context = {
            'form': form,
            'news': news,
            'news_en': news_en,
            'language': language
        }
        return render(request, 'main_pioneer/index.html', context)

    def post(self, request):
        if request.method == "POST":
            form = SubscriptionForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.save()

                news = BlogModel.objects.all().filter(language_ru=True).order_by('-url')[:6]
                news_en = BlogModel.objects.all().filter(language_ru=False).order_by('-url')[:6]

                form = SubscriptionForm()
                message = 'digest'
                context = {
                    'form': form,
                    'message': message,
                    'news': news,
                    'news_en': news_en,
                    'language': language
                }
                return render(request, 'main_pioneer/index.html', context)
            else:
                return redirect('main')


class AboutUs(View):
    def get(self, request):

        form = SubscriptionForm()
        context = {
            'form': form,
            'language': language
        }
        return render(request, 'main_pioneer/about_us.html', context)

    def post(self, request):
        if request.method == "POST":
            form = SubscriptionForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.save()

                form = SubscriptionForm()
                message = 'digest'
                context = {
                    'form': form,
                    'message': message,
                    'language': language
                }
                return render(request, 'main_pioneer/about_us.html', context)
            else:
                return redirect('about_us')


class Services(View):
    def get(self, request):
        form = SubscriptionForm()
        context = {
            'form': form,
            'language': language
        }
        return render(request, 'main_pioneer/services.html', context)

    def post(self, request):
        if request.method == "POST":
            form = SubscriptionForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.save()

                form = SubscriptionForm()
                message = 'digest'
                context = {
                    'form': form,
                    'message': message,
                    'language': language
                }
                return render(request, 'main_pioneer/services.html', context)
            else:
                return redirect('services')


class Blog(View):
    def get(self, request):

        news = BlogModel.objects.all().filter(language_ru=True).order_by('-url')[:20]
        news_en = BlogModel.objects.all().filter(language_ru=False).order_by('-url')[:20]

        form = SubscriptionForm()
        form2 = Subscription2Form()
        context = {
            'form': form,
            'form2': form2,
            'news': news,
            'news_en': news_en,
            'language': language
        }

        return render(request, 'main_pioneer/blog.html', context)

    def post(self, request):
        if request.method == "POST":
            form = SubscriptionForm(request.POST)
            form2 = Subscription2Form(request.POST)
            if form.is_valid() or form2.is_valid():
                form = form.save(commit=False)
                form.save()
                form2 = form2.save(commit=False)
                form2.save()

                news = BlogModel.objects.all().filter(language_ru=True).order_by('-url')[:20]
                news_en = BlogModel.objects.all().filter(language_ru=False).order_by('-url')[:20]

                form = SubscriptionForm()
                form2 = Subscription2Form()
                message = 'digest'
                context = {
                    'form': form,
                    'form2': form2,
                    'message': message,
                    'news': news,
                    'news_en': news_en,
                    'language': language
                }
                return render(request, 'main_pioneer/blog.html', context)
            else:
                return redirect('blog')


class Contacts(View):
    def get(self, request):
        form = SubscriptionForm()
        form_contacts = ContactForm()
        context = {
            'form': form,
            'form_contacts': form_contacts,
            'language': language
        }
        return render(request, 'main_pioneer/contacts.html', context)

    def post(self, request):
        if request.method == "POST":
            form = SubscriptionForm(request.POST)
            form_contacts = ContactForm(request.POST)

            if form_contacts.is_valid():
                form_contacts = form_contacts.save(commit=False)
                form_contacts.save()

                form = SubscriptionForm()
                form_contacts = ContactForm()
                message = 'contact'
                context = {
                    'form': form,
                    'form_contacts': form_contacts,
                    'message': message,
                    'language': language
                }
                return render(request, 'main_pioneer/contacts.html', context)
                # здесь нужно сделать уведомление что на почту info@pioneer-it.ru

            elif form.is_valid():
                form = form.save(commit=False)
                form.save()

                form = SubscriptionForm()
                form_contacts = ContactForm()
                message = 'digest'
                context = {
                    'form': form,
                    'form_contacts': form_contacts,
                    'message': message,
                    'language': language
                }
                return render(request, 'main_pioneer/contacts.html', context)
            else:
                return redirect('contacts')


class Team(View):
    def get(self, request):
        form = SubscriptionForm()
        context = {
            'form': form,
            'language': language
        }
        return render(request, 'main_pioneer/team.html', context)

    def post(self, request):
        if request.method == "POST":
            form = SubscriptionForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.save()

                form = SubscriptionForm()
                message = 'digest'
                context = {
                    'form': form,
                    'message': message,
                    'language': language
                }
                return render(request, 'main_pioneer/team.html', context)
            else:
                return redirect('team')


class History(View):
    def get(self, request):
        form = SubscriptionForm()
        context = {
            'form': form,
            'language': language
        }
        return render(request, 'main_pioneer/historis.html', context)

    def post(self, request):
        if request.method == "POST":
            form = SubscriptionForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.save()

                form = SubscriptionForm()
                message = 'digest'
                context = {
                    'form': form,
                    'message': message,
                    'language': language
                }
                return render(request, 'main_pioneer/historis.html', context)
            else:
                return redirect('historis')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class AddBlog(View):
    def get(self, request):
        if request.user.is_authenticated:
            add_blog = AddBlogForm()
            context = {
                'add_blog': add_blog
            }
            return render(request, 'main_pioneer/add_blog.html', context)
        else:
            return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            if request.method == "POST":
                add_blog = AddBlogForm(request.POST)
                if add_blog.is_valid():
                    date = convert_date()
                    add_blog = add_blog.save(commit=False)
                    add_blog.url = str(int(time()))
                    add_blog.date_ru = str(date[0])
                    add_blog.date_en = str(date[1])
                    add_blog.save()

                    message = 'blog'
                    add_blog = AddBlogForm()
                    context = {
                        'add_blog': add_blog,
                        'message': message,
                    }
                    return render(request, 'main_pioneer/add_blog.html', context)
                else:
                    return redirect('add_blog')
        else:
            return redirect('login')


class NewShow(View):
    def get(self, request, slug):

        new = BlogModel.objects.get(url=slug)
        form = SubscriptionForm()
        context = {
            'form': form,
            'new': new,
            'language': language

        }
        return render(request, 'main_pioneer/article.html', context)

    def post(self, request, slug):
        if request.method == "POST":
            form = SubscriptionForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.save()

                new = BlogModel.objects.get(url=slug)
                form = SubscriptionForm()
                message = 'digest'
                context = {
                    'form': form,
                    'message': message,
                    'new': new,
                    'language': language
                }
                return render(request, 'main_pioneer/article.html', context)
            else:
                return redirect('article')
