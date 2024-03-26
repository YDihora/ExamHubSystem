# Generated by Django 2.0.3 on 2018-03-11 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('answers', models.CharField(max_length=200)),
                ('choice_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.CharField(max_length=20)),
                ('student_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_id', models.CharField(max_length=20)),
                ('teacher_name', models.CharField(max_length=200)),
                ('stud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_home.Student')),
            ],
        ),
    ]
