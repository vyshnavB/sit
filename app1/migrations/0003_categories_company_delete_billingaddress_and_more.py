# Generated by Django 4.1.3 on 2023-08-08 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_billingaddress_unpost_rename_post_stpost_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('company_image', models.FileField(blank=True, null=True, upload_to='posts/')),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('alt_mobile', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('web_link', models.URLField(blank=True, null=True)),
                ('fb_link', models.URLField(blank=True, null=True)),
                ('insta_link', models.URLField(blank=True, null=True)),
                ('linkdin_link', models.URLField(blank=True, null=True)),
                ('twit_link', models.URLField(blank=True, null=True)),
                ('service_1', models.CharField(blank=True, max_length=255, null=True)),
                ('service_2', models.CharField(blank=True, max_length=255, null=True)),
                ('service_3', models.CharField(blank=True, max_length=255, null=True)),
                ('service_4', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, upload_to='posts/')),
                ('category_name', models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='cate', to='app1.categories')),
            ],
        ),
        migrations.DeleteModel(
            name='BillingAddress',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='orderitem',
        ),
        migrations.DeleteModel(
            name='Unpost',
        ),
        migrations.DeleteModel(
            name='comment',
        ),
        migrations.DeleteModel(
            name='Stpost',
        ),
    ]
