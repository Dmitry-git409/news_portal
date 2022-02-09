# Generated by Django 4.0.1 on 2022-02-09 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0, verbose_name='Rating Author')),
                ('to_user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_field', models.CharField(max_length=255, unique=True, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_field', models.CharField(choices=[('PO', 'Post'), ('NW', 'News')], default='PO', max_length=2, verbose_name='Select Type')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Post Created')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Title Post')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
                ('post_rating', models.IntegerField(default=0, verbose_name='Rating Post')),
                ('to_author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.author')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.category')),
                ('to_post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='to_category',
            field=models.ManyToManyField(through='news.PostCategory', to='news.Category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(blank=True, verbose_name='Comment')),
                ('comment_time', models.DateTimeField(auto_now_add=True, verbose_name='Comment Created')),
                ('comment_rating', models.IntegerField(default=0, verbose_name='Rating Comment')),
                ('to_posts', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.post')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]