# Generated by Django 2.2.4 on 2019-08-26 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default='screen.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(default='title', max_length=10),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.CharField(default='xie jian jie', max_length=100),
        ),
    ]
