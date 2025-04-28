
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Comment
from .forms import ItemForm, CommentForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required 

# home page to welcome users
def home_page_views(request):
    return render(request, 'home_page.html')

# user to view items and add items
def items_views(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES) # if uploading image, add request.FILES
        if form.is_valid():
            item = form.save(commit=False) # we don't want to save it yet
            item.seller = request.user # associate item to the current user
            item.save()
            return redirect('online_app:items') # redirect to the same page
    else:
        form = ItemForm()

    items = Item.objects.all() # gets all items
    context = {
        'items': items,
        'form': form, # passing the form to template to upload items
    }
    return render(request, 'items.html', context)


# user to login and logout
def Login_views(request):
    return render(request, 'login.html')

def Logout_views(request):
    return render(request, 'logout.html')


# user to signup and signout
def signup_view(request):
    return render(request, 'signup.html')

def signout_view(request):
    return render(request, 'signout.html')

# Detail view of a particular item
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    comments = item.comments.all() # Get all comments of the item

    if request.method == 'POST':
        comment_form = CommentForm(request.POST) # get the comment form
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) # we don't want to save it yet
            comment.item = item # associate comment with item
            comment.author = request.user # associate the comment to the logged in user
            comment.save()
            return redirect('online_app:item_detail', pk=pk)
    else:
        comment_form = CommentForm()

    context = {
        'item': item,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'item_detail.html', context)

def upload_item_view(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES) # if uploading image, add request.FILES
        if form.is_valid():
            item = form.save(commit=False) # we don't want to save it yet
            item.seller = request.user # associate item to the current user
            item.save()
            return redirect('online_app:items') # redirect to the same page
    else:
        form = ItemForm()

    items = Item.objects.all() # gets all items
    context = {
        'items': items,
        'form': form, # passing the form to template to upload items
    }
    return render(request, 'up_items.html', context)
