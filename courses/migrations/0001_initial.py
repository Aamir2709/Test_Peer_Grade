# Generated by Django 4.0.2 on 2022-03-21 17:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_name', models.CharField(max_length=100)),
                ('points', models.IntegerField()),
                ('due_date', models.DateTimeField()),
                ('grading_type', models.BooleanField(default=True)),
                ('teacher_ratio', models.FloatField(blank=True, null=True)),
                ('student_ratio', models.FloatField(blank=True, null=True)),
                ('no_of_peers', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CreatedClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_code', models.CharField(max_length=6)),
                ('class_name', models.CharField(max_length=100)),
                ('class_description', models.TextField(max_length=1000)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('marks', models.IntegerField(blank=True, default=0)),
                ('remark', models.CharField(default='Submitted on Time', max_length=100)),
                ('assignment_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='courses.assignments')),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubmittedLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube_link', models.URLField(default=None)),
                ('submission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.submission')),
            ],
        ),
        migrations.CreateModel(
            name='SubmittedFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.FileField(blank=True, upload_to='subs/files/')),
                ('submission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.submission')),
            ],
        ),
        migrations.CreateModel(
            name='notices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_name', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.createdclasses')),
            ],
        ),
        migrations.CreateModel(
            name='noticeFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='subs/files/')),
                ('notice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.notices')),
            ],
        ),
        migrations.CreateModel(
            name='JoinedClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.createdclasses')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=1000)),
                ('comment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.submission')),
            ],
        ),
        migrations.AddField(
            model_name='assignments',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.createdclasses'),
        ),
        migrations.CreateModel(
            name='AssignedPeers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_marks', models.IntegerField(blank=True, null=True)),
                ('question1', models.TextField(blank=True, max_length=1000)),
                ('question2', models.TextField(blank=True, max_length=1000)),
                ('question3', models.TextField(blank=True, max_length=1000)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.assignments')),
                ('peer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='peer', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
