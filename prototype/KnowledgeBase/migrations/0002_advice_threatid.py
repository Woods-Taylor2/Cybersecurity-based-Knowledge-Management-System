# Generated by Django 3.0.5 on 2020-04-05 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advice',
            name='threatID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='KnowledgeBase.Threat'),
        ),
    ]