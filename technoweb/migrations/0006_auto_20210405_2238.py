# Generated by Django 3.1.7 on 2021-04-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technoweb', '0005_auto_20210405_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrcorner',
            name='cab_facility',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='hrcorner',
            name='communication_skill',
            field=models.CharField(choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Average', 'Average')], max_length=100),
        ),
        migrations.AlterField(
            model_name='hrcorner',
            name='group_discussion',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='hrcorner',
            name='hr_round',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='hrcorner',
            name='incentive_plans',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='hrcorner',
            name='interview_process',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='hrcorner',
            name='job_experience',
            field=models.CharField(choices=[('Experienced', 'Experienced'), ('Fresher', 'Fresher')], max_length=100),
        ),
        migrations.AlterField(
            model_name='hrcorner',
            name='project',
            field=models.CharField(choices=[('Voice', 'Voice'), ('Non-Voice', 'Non-Voice'), ('Technical', 'Technical'), ('Non-Technical', 'Non-Technical')], max_length=100),
        ),
        migrations.AlterField(
            model_name='hrcorner',
            name='technical_round',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='hrcorner',
            name='work_environment',
            field=models.CharField(choices=[('24*7', '24*7'), ('Day Shift', 'Day Shift'), ('Sat-Sun Fixed Weekly-offs', 'Sat-Sun Fixed Weekly-offs'), ('Rotational Offs', 'Rotational Offs')], max_length=100),
        ),
    ]