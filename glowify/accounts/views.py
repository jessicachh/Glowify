from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import BlogPost
from .forms import BlogPostForm
from django.shortcuts import render, redirect, get_object_or_404


# Get the custom user model dynamically
User = get_user_model()

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]

            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)

            # Show success message
            messages.success(request, "Registration successful! Please log in.")

            # Redirect to login page after successful registration
            return redirect('login')  # Redirect to the login page after registration
        else:
            # Print form errors to the console for debugging
            print(form.errors)
            messages.error(request, "Error during registration. Please try again.")
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home after successful login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def welcome(request):
    return render(request, 'welcome.html')

def home_view(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def skintype(request):
    return render(request, 'skintype.html')

def skincare(request):
    return render(request, 'skincare.html')

def products(request):
    return render(request, 'products.html')



def blog_view(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog')  
    else:
        form = BlogPostForm()

    # Fetch all blog posts to display
    blog_posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {'form': form, 'blog_posts': blog_posts})


@login_required
def edit_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    # Check if the logged-in user is the author of the post
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog')  # Redirect to the blog page after saving
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'edit_blog_post.html', {'form': form, 'post': post})

@login_required
def delete_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    # Check if the logged-in user is the author of the post
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    if request.method == 'POST':
        post.delete()
        return redirect('blog')  # Redirect to the blog page after deletion

    return render(request, 'delete_blog_post.html', {'post': post})