# Generated by Django 2.2.4 on 2019-08-18 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lastever', '0003_league_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='league',
            name='slug',
            field=models.SlugField(editable=False),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_time', models.DateTimeField()),
                ('home_score', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('away_score', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('SCH', 'Scheduled'), ('FIN', 'Final'), ('FET', 'Final/Extra Time'), ('FPK', 'Final/Penalty Kicks'), ('CAN', 'Cancelled'), ('RES', 'Rescheduled')], default='SCH', max_length=3)),
                ('playoff', models.BooleanField()),
                ('slug', models.SlugField(editable=False)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='lastever.Team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='lastever.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lastever.Team')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(editable=False)),
                ('posted', models.DateTimeField()),
                ('tags', models.ManyToManyField(to='lastever.Tags')),
            ],
        ),
    ]
