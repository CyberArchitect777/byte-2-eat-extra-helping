# Generated by Django 4.2.15 on 2024-09-01 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_alter_review_food_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='edited_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
