from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.

class HomeView(ListView):
    # here we accessing the Post Table
    model = Post
    # This is where Table is being used
    #template_name = "blog/index.html"
    # And this is the name we used to represent the table
    context_object_name = "posts"
    # This is for pagination
    paginate_by = 10

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements.html"
        return "blog/index.html"
