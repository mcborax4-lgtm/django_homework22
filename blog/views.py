from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()

        if obj.views_count == 100:
            send_mail(
                subject=f'Статья "{obj.title}" набрала 100 просмотров!',
                message=f'Поздравляем! Статья "{obj.title}" достигла 100 просмотров.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
            )

        return obj


class BlogCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = BlogPost
    template_name = 'blog/form.html'
    fields = ['title', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('blog_list')

    def test_func(self):
        return self.request.user.has_perm('blog.add_blogpost')


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    template_name = 'blog/form.html'
    fields = ['title', 'content', 'preview', 'is_published']

    def test_func(self):
        return self.request.user.has_perm('blog.change_blogpost')

    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/confirm_delete.html'
    success_url = reverse_lazy('blog_list')

    def test_func(self):
        return self.request.user.has_perm('blog.delete_blogpost')