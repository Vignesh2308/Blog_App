from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm, CommentForm

from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView

from .models import Post, Comment
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        # print('POST REQUEST')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('Login:home'))
            else:
                return render(request, 'Login/login.html')
        else:
            return render(request, 'Login/login.html', {"valid": True})
    else:
        return render(request, 'Login/login.html', {"valid": False})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login:index'))


def user_register(request):
    registered = False
    if request.method == 'POST':
        userform = UserRegisterForm(request.POST)
        if userform.is_valid():
            # user = userform.save()
            # user.set_password(user.password)
            userform.save()
            registered = True

        else:
            print(userform.errors)

    else:
        userform = UserRegisterForm()

    context = {'user_form': userform, 'registered': registered}
    return render(request, 'Login/register.html', context)


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'Login/home_page.html'


class AboutView(LoginRequiredMixin, TemplateView):
    template_name = 'Login/about.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'Login/add_post.html'
    fields = ('author', 'title', 'content',)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'Login/update_post.html'
    fields = ('author', 'title', 'content')


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post_detail'
    template_name = 'Login/post_detail.html'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'Login/delete_post.html'
    success_url = reverse_lazy('Login:home')


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = User
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.name = request.user.username
            comment.save()
            return redirect('Login:home')

    else:
        form = CommentForm()
        return render(request, 'Login/add_comment.html',{'form': form, 'title': post.title, 'user': request.user.username})


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'Login/update_comment.html'
    fields = ('comment_text',)


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'Login/delete_comment.html'
    success_url = reverse_lazy('Login:home')