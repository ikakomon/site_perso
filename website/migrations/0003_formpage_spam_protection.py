# Generated by Django 2.2.3 on 2019-08-13 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='formpage',
            name='spam_protection',
            field=models.BooleanField(default=True, help_text='When enabled, the CMS will filter out spam form submissions for this page.', verbose_name='Spam Protection'),
        ),
    ]
