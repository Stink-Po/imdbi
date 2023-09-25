# Generated by Django 4.2.5 on 2023-09-14 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('movies', '0001_initial'),
        ('movie_socialapp', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movielike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customuser'),
        ),
        migrations.AddField(
            model_name='moviecomment',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='movies.movie'),
        ),
        migrations.AddField(
            model_name='moviecomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customuser'),
        ),
    ]
