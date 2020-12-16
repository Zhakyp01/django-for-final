# Generated by Django 3.1.3 on 2020-12-14 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20201214_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='header_image',
        ),
        migrations.AddField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='news.articles')),
            ],
        ),
    ]
