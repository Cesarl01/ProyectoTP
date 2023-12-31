# Generated by Django 3.2.18 on 2023-05-14 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interno',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='public.persona')),
                ('CUIL', models.CharField(max_length=10, verbose_name='CUIL')),
                ('baja', models.BooleanField(default=0)),
            ],
            bases=('public.persona',),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='public.persona')),
                ('CUIT', models.CharField(max_length=10, verbose_name='CUIT')),
                ('baja', models.BooleanField(default=0)),
            ],
            bases=('public.persona',),
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
    ]
