# Generated by Django 2.0.1 on 2019-11-22 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YkLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yk_video_jump_link', models.CharField(blank=True, max_length=200, null=True)),
                ('yk_lesson_name', models.CharField(blank=True, max_length=50, null=True)),
                ('yk_lesson_price', models.FloatField(blank=True, null=True)),
                ('yk_lesson_describe', models.CharField(blank=True, max_length=200, null=True)),
                ('yk_teacher_describe', models.CharField(blank=True, max_length=100, null=True)),
                ('yk_lesson_contents', models.CharField(blank=True, max_length=50, null=True)),
                ('yk_lesson_contents_mark', models.IntegerField(blank=True, null=True)),
                ('yk_lesson_img', models.CharField(blank=True, max_length=200, null=True)),
                ('yk_rotaion_id', models.IntegerField(blank=True, null=True)),
                ('yk_recommend_id', models.IntegerField(blank=True, null=True)),
                ('yk_lesson_price_type', models.CharField(blank=True, max_length=50, null=True)),
                ('yk_lesson_dis_price', models.FloatField(blank=True, null=True)),
                ('yk_lesson_list', models.IntegerField(blank=True, null=True)),
                ('yk_user_id', models.IntegerField(blank=True, null=True)),
                ('yk_buy_amount', models.IntegerField(blank=True, null=True)),
                ('yk_watch_amount', models.IntegerField(blank=True, null=True)),
                ('yk_course_chapter', models.CharField(blank=True, max_length=20, null=True)),
                ('yk_one_list_id', models.IntegerField(blank=True, null=True)),
                ('yk_tow_list_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'yk_lesson',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='YkRecommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yk_lesson_type', models.CharField(max_length=200)),
                ('yk_lesson_jump_link', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'yk_recommend',
            },
        ),
        migrations.CreateModel(
            name='YkRotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yk_is_rotation', models.IntegerField()),
            ],
            options={
                'db_table': 'yk_rotation',
            },
        ),
    ]
