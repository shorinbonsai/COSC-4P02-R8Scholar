# Generated by Django 3.1.4 on 2021-02-24 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('nickname', models.CharField(default='Anonymous', max_length=20)),
                ('password', models.CharField(max_length=32)),
                ('is_active', models.BooleanField(default=False, verbose_name='is_active')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.IntegerField()),
                ('review_id', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('content', models.TextField(default=None)),
                ('date', models.DateTimeField(default=None)),
                ('numb_reports', models.IntegerField(default=None)),
                ('child', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.comment')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('reviewer', models.CharField(max_length=32)),
                ('subject', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField(default=None, null=True)),
                ('rating', models.FloatField(default=None, null=True)),
                ('numb_reports', models.IntegerField(default=None)),
                ('date_created', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=202)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default=None, null=True)),
                ('date', models.DateTimeField(default=None, null=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.comment')),
                ('nickname_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('subject_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='api.subject')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='comments',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.comment'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='forum_posts',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.forum'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='reviews',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.review'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.subject')),
                ('department', models.CharField(max_length=20)),
                ('rating', models.FloatField(default=None)),
                ('name', models.CharField(default=None, max_length=30)),
                ('reviews', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.review')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.subject')),
                ('name', models.CharField(default=None, max_length=20)),
                ('courses_rating', models.FloatField(default=None)),
                ('instructors_rating', models.FloatField(default=None)),
                ('overall_rating', models.FloatField(default=None)),
                ('review', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.review')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.subject')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('department', models.CharField(max_length=20)),
                ('rating', models.FloatField(default=None)),
                ('name', models.CharField(default=None, max_length=30)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.instructor')),
                ('reviews', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.review')),
            ],
        ),
        migrations.AddConstraint(
            model_name='comment',
            constraint=models.UniqueConstraint(fields=('comment_id', 'review_id'), name='comment_key'),
        ),
    ]
