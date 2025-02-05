from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ContactForm, PostForm
from .forms import PostForm
from .models import (
	Post,
	Category,
	Project,
	Contact,
)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'pages/post_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'pages/post_form.html'
    success_url = reverse_lazy('home')

    # Restrict edits to the post's author only
    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)
    
class DraftListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'pages/drafts.html'
    context_object_name = 'drafts'
    ordering = ['-created_on']

    def get_queryset(self):
        # Show drafts only for the logged-in author
        return Post.objects.filter(
            status="draft",
            author=self.request.user  # Only show drafts by the current user
        )
		
class ProjectListView(ListView):
	model = Project
	paginate_by = 5
	template_name = 'pages/projects.html'
	context_object_name = 'projects'


class ProjectDetailView(DetailView):
	model = Project
	template_name = 'pages/project_details.html'


class BlogListView(ListView):
	model = Post
	paginate_by = 10
	template_name = 'pages/home.html'
	context_object_name = 'posts'
	ordering = ['-created_on']
	
	# to filter published posts
	def get_queryset(self):
		return Post.objects.filter(status="published")
	


class BlogDetailView(DetailView):
	model = Post
	template_name = 'pages/post_detail.html'


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__slug__contains=category,
		status="published"
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "pages/category_list.html", context)


class ContactFormView(FormView):
	template_name = 'pages/contact.html'
	form_class = ContactForm
	success_url = '/contact/'

	def form_valid(self, form):
		name = form.cleaned_data['name']
		email = form.cleaned_data['email']
		message = form.cleaned_data['message']

		m = Contact(
			name=name,
			email=email,
			message=message,
		)
		m.save()

		messages.success(self.request, 'Your message has been sent.')

		return super().form_valid(form)


class AboutView(TemplateView):
	template_name = 'pages/about.html'



