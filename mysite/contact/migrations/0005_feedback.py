# Generated by Django 2.0.3 on 2018-04-11 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0004_delete_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('query', models.CharField(max_length=800)),
                ('cust_name', models.CharField(max_length=200)),
                ('cust_email', models.CharField(max_length=200)),
                ('cust_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]
