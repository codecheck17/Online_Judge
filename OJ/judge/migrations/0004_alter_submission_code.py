# Generated by Django 4.0.5 on 2022-07-04 06:35

from django.db import migrations, models
import judge.models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0003_rename_problem_testcase_problem_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='Code',
            field=models.FileField(upload_to=judge.models.Submission.upload_code_name),
        ),
    ]