# Generated by Django 4.2 on 2023-05-10 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_commentcourse_article_commentcourse_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentcourse',
            name='course',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='commentscourse', to='blog.course'),
        ),
    ]