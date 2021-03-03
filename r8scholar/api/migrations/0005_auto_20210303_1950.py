# Generated by Django 3.1.5 on 2021-03-03 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210303_0639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='department_name',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='course_rating',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='email',
            new_name='reviewer',
        ),
        migrations.RemoveField(
            model_name='review',
            name='code',
        ),
        migrations.RemoveField(
            model_name='review',
            name='department_rating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='instructor_name',
        ),
        migrations.RemoveField(
            model_name='review',
            name='instructor_rating',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='verification_code',
            field=models.CharField(default='F2A5BM', max_length=10),
        ),
    ]
