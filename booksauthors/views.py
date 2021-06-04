from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    data = {"books":books,"authors":authors}
    authordata = {"authors":authors}
    return render(request, "booksauthors/home.html", data)


def addauthor(request):
    authorform = AuthorForm()
    
    if(request.method=='POST'):
        form = AuthorForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("/")
    
    data = {"authorform":authorform}
    return render(request, "booksauthors/addauthor.html",data)

def addbook(request):
    bookform = BookForm()
    if(request.method=='POST'):
        form = BookForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("/")
    
    data = {"bookform":bookform}

    return render(request, "booksauthors/addbook.html",data)

def deleteauthor(request,pk):
    author = Author.objects.get(id=pk)
    author.delete()
    return redirect("/")

def deletebook(request,pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect("/")

def updateauthor(request,pk):
    author = Author.objects.get(id=pk)
    authorform = AuthorForm(instance=author)

    if(request.method=="POST"):
        form =  AuthorForm(request.POST, instance=author)
        if(form.is_valid()):
            form.save()
            return redirect("/")

    data = {"authorform": authorform}
    return render(request, "booksauthors/updateauthor.html",data)

def updatebook(request,pk):
    book = Book.objects.get(id=pk)
    bookform = BookForm(instance=book)

    if(request.method=="POST"):
        form =  BookForm(request.POST, instance=book)
        if(form.is_valid()):
            form.save()
            return redirect("/")

    data = {"bookform": bookform}
    return render(request, "booksauthors/updatebook.html",data)