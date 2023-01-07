# Generated by Django 4.1.2 on 2023-01-03 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Designation', models.CharField(max_length=100)),
                ('Orgnization_name', models.CharField(max_length=100)),
                ('Experience', models.IntegerField()),
                ('No_of_openings', models.IntegerField()),
                ('Salary', models.IntegerField()),
                ('Job_Description', models.TextField()),
                ('Job_Location', models.CharField(max_length=100)),
                ('Key_skills', models.TextField()),
                ('Education', models.TextField()),
                ('Employment_Type', models.CharField(max_length=100)),
                ('About_company', models.TextField()),
                ('HR_details', models.TextField()),
                ('Job_posted_days', models.IntegerField()),
                ('Job_Category', models.CharField(max_length=100)),
                ('Link_to_apply', models.URLField(max_length=500)),
                ('Perks', models.CharField(max_length=100)),
                ('Activity_of_employer', models.TextField()),
                ('Additional_information', models.TextField()),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]