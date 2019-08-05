# Generated by Django 2.2.3 on 2019-08-03 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('all_books', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('is_paid', models.BooleanField(default=False)),
                ('bKash_ac', models.IntegerField()),
                ('transaction_id', models.IntegerField()),
                ('fine_code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='all_books.Borrow')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]