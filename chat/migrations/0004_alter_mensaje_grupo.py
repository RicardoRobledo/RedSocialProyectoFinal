# Generated by Django 3.2 on 2022-04-11 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupo', '0002_auto_20220410_1344'),
        ('chat', '0003_alter_mensaje_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='grupo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='grupo.grupo'),
        ),
    ]
