# Generated by Django 4.0.5 on 2022-08-02 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectsapp', '0006_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
        migrations.AddField(
            model_name='project',
            name='num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]