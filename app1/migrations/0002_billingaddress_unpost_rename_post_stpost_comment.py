# Generated by Django 4.0.5 on 2022-11-06 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=100)),
                ('apartment_address', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('address_type', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Unpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('headerimage', models.ImageField(null=True, upload_to='')),
                ('title_tag', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('post_date', models.DateField(default=0)),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='Post',
            new_name='Stpost',
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_added', models.DateField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.stpost')),
            ],
        ),
    ]
