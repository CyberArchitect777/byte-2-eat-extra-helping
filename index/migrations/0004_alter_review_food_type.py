# Generated by Django 4.2.15 on 2024-08-18 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_alter_review_food_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='food_type',
            field=models.CharField(choices=[('Indian', 'Indian'), ('Italian', 'Italian'), ('Chinese', 'Chinese'), ('Thai', 'Thai'), ('Japanese', 'Japanese'), ('Mexican', 'Mexican'), ('British', 'British'), ('French', 'French'), ('Greek', 'Greek'), ('American', 'American'), ('Turkish', 'Turkish'), ('Korean', 'Korean'), ('Vietnamese', 'Vietnamese'), ('Spanish', 'Spanish'), ('Lebanese', 'Lebanese'), ('Caribbean', 'Caribbean'), ('Other', 'Other')], default='Indian', max_length=20),
        ),
    ]
