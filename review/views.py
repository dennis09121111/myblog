from django.shortcuts import render, redirect
from .models import Review
from post.models import Post
from django.contrib.auth.decorators import login_required
from .forms import ReviewCreateForm # , ReviewUpdateForm
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

@login_required
def create_review(request, post):
    if request.method == 'POST':
        post_id = post
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            post = Post.objects.get(pk=post)
            author = request.user
            review.post = post
            review.author = author
            review.save()
            return redirect('post_detail', pk=post_id)
    else:
        form = ReviewCreateForm()
        context = {
            'form': form
        }
        return render(request, 'review/review_form.html', context)


class ReviewUpdate(UpdateView):
    model = Review
    fields = ['content',]

# @login_required
# def update_review(request, post, review_id):
#     review = Review.objects.get(pk=review_id)
#     if request.method == 'POST':
#         form = ReviewUpdateForm(request.POST, instance=review)
#         if form.is_valid():
#             review = form.save(commit=False)
#             post = Post.objects.get(pk=post)
#             author = request.user
#             review.post = post
#             review.author = author
#             review.save()
#             return redirect('post_detail', pk=post_id)
#     else:
#         form = ReviewUpdateForm(instance=review)
#         context = {
#             'form': form
#         }
#         return render(request, 'review/review_update.html', context)
