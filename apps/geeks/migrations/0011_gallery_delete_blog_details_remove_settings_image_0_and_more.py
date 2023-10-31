# Generated by Django 4.2.6 on 2023-10-31 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0010_alter_settings_image_alter_settings_image_0_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery_image', verbose_name='Фотография для галлери')),
            ],
            options={
                'verbose_name': ('Галерея',),
                'verbose_name_plural': 'Галерея',
            },
        ),
        migrations.DeleteModel(
            name='Blog_details',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='image_0',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='image_1',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='image_4',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='image_5',
        ),
    ]
