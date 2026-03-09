from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from apps.blog.models import Post, Comment
from apps.blog.forms import CommentForm


class BlogView(ListView):
    model = Post 
    template_name = 'pages/blog.html'
    context_object_name = 'posts'
    paginate_by = 6
    ordering = ['-id']


class BlogDetailView(DetailView):
    model = Post 
    template_name = 'pages/blog-detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context['comments'] = Comment.objects.filter(
            post=self.object,
            parent__isnull=True
        )
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            parent_id = request.POST.get('parent_id')
            if parent_id:
                comment.parent = Comment.objects.get(id=parent_id)
            comment.save()
        return redirect(self.object.get_absolute_url())
    
