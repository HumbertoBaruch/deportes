# Generated by Django 3.0.6 on 2020-06-02 05:34

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
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(choices=[('Atletismo', 'Atletismo'), ('Basketball', 'Basketball'), ('eSports', 'ESports'), ('Futbol', 'Futbol'), ('Handball', 'Handball'), ('Tenis', 'Tenis'), ('Ping-Pong', 'Ping pong'), ('Tiro con arco', 'Tiro con arco'), ('Tochito', 'Tochito'), ('Voleibol', 'Voleibol')], default='Futbol', max_length=25)),
                ('max_students', models.IntegerField(blank=True, null=True)),
                ('schedule', models.CharField(max_length=50)),
                ('place', models.CharField(choices=[('La cancha de pasto', 'La cancha de pasto'), ('La cancha techada', 'La cancha techada'), ('Campo de tiro', 'Campo de tiro'), ('La cafe', 'La cafe')], default='La cancha de pasto', max_length=25)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expediente', models.IntegerField(unique=True)),
                ('last_name', models.CharField(max_length=150)),
                ('first_name', models.CharField(max_length=50)),
                ('group', models.IntegerField()),
                ('semester', models.IntegerField(choices=[(1, 'Primero'), (2, 'Segundo'), (3, 'Tercero')], default=1)),
                ('plan', models.CharField(choices=[('SOF18', 'SOF18'), ('LAT18', 'LAT18'), ('TEL18', 'TEL18'), ('INF18', 'INF18'), ('INC18', 'INC18')], default='SOF18', max_length=5)),
                ('liberado', models.BooleanField(blank=True, default=False)),
                ('date_enrollment', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Team')),
            ],
        ),
    ]
