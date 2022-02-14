# Generated by Django 4.0.2 on 2022-02-14 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UsersCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogApp.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('postpicture', models.ImageField(upload_to='blogApp/static/img/')),
                ('content', models.CharField(max_length=300)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogApp.category')),
                ('tags', models.ManyToManyField(to='blogApp.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogApp.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogApp.user')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='followers',
            field=models.ManyToManyField(through='blogApp.UsersCategories', to='blogApp.User'),
        ),
    ]
