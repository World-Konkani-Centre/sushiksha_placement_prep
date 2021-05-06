# Generated by Django 3.1.7 on 2021-05-04 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=1)),
                ('title', models.CharField(help_text='Provide the title of the Badge', max_length=50)),
                ('description', models.CharField(help_text='Reason to give this Badge', max_length=200)),
                ('image', models.ImageField(upload_to='badges')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='BadgeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awarded_by', models.CharField(default='admin', max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('descritpion', models.TextField()),
                ('badge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badge.badge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.AddField(
            model_name='badge',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='badge.badgecategory'),
        ),
    ]