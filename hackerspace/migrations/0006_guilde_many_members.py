# Generated by Django 2.2.6 on 2019-11-08 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackerspace', '0005_meetingnote_text_main_topics'),
    ]

    operations = [
        migrations.AddField(
            model_name='guilde',
            name='many_members',
            field=models.ManyToManyField(blank=True, related_name='m_members', to='hackerspace.Person'),
        ),
    ]