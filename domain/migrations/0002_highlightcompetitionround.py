# Generated by Django 4.0 on 2022-10-21 00:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighlightCompetitionRound',
            fields=[
                ('h_round_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('lifted_weight', models.FloatField(default=0.0, verbose_name='Peso Levantado (Kg)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('competitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.competitor')),
            ],
        ),
    ]
