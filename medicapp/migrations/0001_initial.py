# Generated by Django 4.2.4 on 2023-08-14 10:45

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
            name='Medical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s1', models.CharField(max_length=200)),
                ('s2', models.CharField(max_length=200)),
                ('s3', models.CharField(max_length=200)),
                ('s4', models.CharField(max_length=200)),
                ('s5', models.CharField(max_length=200)),
                ('disease', models.CharField(max_length=200)),
                ('medicine', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('time', models.CharField(max_length=200, null=True)),
                ('treatment_day', models.DateTimeField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dor', to=settings.AUTH_USER_MODEL)),
                ('medical', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medical', to='medicapp.medical')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pat', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(default='None')),
                ('region', models.CharField(default='', max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('country', models.CharField(default='Tanzania', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
