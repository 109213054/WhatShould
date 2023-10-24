# Generated by Django 4.2.4 on 2023-09-07 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CostDetail',
            fields=[
                ('cid', models.AutoField(db_column='cID', primary_key=True, serialize=False)),
                ('uid', models.IntegerField(db_column='uID')),
                ('resname', models.CharField(db_column='ResName', max_length=20)),
                ('date', models.DateField()),
                ('which_meal', models.IntegerField()),
                ('rid', models.IntegerField(db_column='rID')),
                ('price', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('my_text', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': '1_cost_detail',
                'managed': False,
            },
        ),
    ]
