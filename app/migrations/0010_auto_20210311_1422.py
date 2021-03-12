# Generated by Django 3.1.7 on 2021-03-11 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0009_auto_20210308_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='inhabitants',
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.status'),
        ),
        migrations.CreateModel(
            name='HouseMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.BooleanField(default=False)),
                ('currentHouse', models.BooleanField(default=False)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.house')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]