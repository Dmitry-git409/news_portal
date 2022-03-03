from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect


class Author(models.Model):
    to_user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    rating = models.IntegerField(default=0, verbose_name='Rating Author')

    def update_rating(self, rating=0):
        for post in Post.objects.filter(to_author=self):
            rating += post.post_rating * 3
            print(post)
        for comment in Comment.objects.filter(to_user=self.to_user):
            rating += comment.comment_rating
            print(comment, '=')
        for comment_post in Comment.objects.filter(to_posts__in=Post.objects.filter(to_author=self)):
            rating += comment_post.comment_rating
            print(comment_post)
        self.rating = rating
        self.save()

    def __str__(self):
        return f'{self.to_user.username}'


class Category(models.Model):
    category_field = models.CharField(max_length=255, unique=True, verbose_name='Category')

    def __str__(self):
        return f'{self.category_field}'


class Post(models.Model):
    SELECTOR = [('PO', 'Post'), ('NW', 'News')]
    to_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    select_field = models.CharField(max_length=2, choices=SELECTOR, default='PO', verbose_name='Select Type')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Post Created')
    to_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255, unique=True, verbose_name='Title Post')
    content = models.TextField(blank=True, verbose_name='Content')
    post_rating = models.IntegerField(default=0, verbose_name='Rating Post')

    class Meta:
        ordering = ['time_create']

    def get_absolute_url(self):
        return f'/news_portal/{self.pk}'

    def __str__(self):
        return f'date: {self.time_create}, username: {self.to_author.to_user.username}, rating: {self.post_rating},' \
               f' title: {self.title}, preview: {self.preview()}'

    def like(self):
        self.post_rating += 1
        self.save()

    def dis_like(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return self.content[:124] + '...'


class PostCategory(models.Model):
    to_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    to_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.to_post}:{self.to_category}'


class Comment(models.Model):
    to_posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField(blank=True, verbose_name='Comment')
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name='Comment Created')
    comment_rating = models.IntegerField(default=0, verbose_name='Rating Comment')

    def __str__(self):
        return f'date: {self.comment_time}, username: {self.to_user.username}, ' \
               f'rating: {self.comment_rating}, text: {self.comment_text}'

    def like(self):
        self.comment_rating += 1
        self.save()

    def dis_like(self):
        self.comment_rating -= 1
        self.save()
