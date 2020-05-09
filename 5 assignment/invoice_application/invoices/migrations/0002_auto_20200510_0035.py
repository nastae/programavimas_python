# Generated by Django 2.2 on 2020-05-09 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('invoices', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='commisioner_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commissioner1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='form',
            name='commisioner_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commissioner2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='form',
            name='commisioner_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commissioner3', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='form',
            name='commisioner_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commissioner4', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='form',
            name='responsible_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responsible_user', to=settings.AUTH_USER_MODEL),
        ),
    ]