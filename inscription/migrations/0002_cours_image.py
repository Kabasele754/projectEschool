# Generated by Django 3.2.8 on 2021-12-26 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='image',
            field=models.ImageField(default='laisse moi passer', upload_to=''),
            preserve_default=False,
        ),
    ]