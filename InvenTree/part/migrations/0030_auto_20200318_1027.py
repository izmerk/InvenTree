# Generated by Django 2.2.9 on 2020-03-18 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0029_auto_20200223_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bomitem',
            name='part',
            field=models.ForeignKey(help_text='Select parent part', limit_choices_to={'assembly': True, 'is_template': False}, on_delete=django.db.models.deletion.CASCADE, related_name='bom_items', to='part.Part'),
        ),
        migrations.AlterField(
            model_name='bomitem',
            name='sub_part',
            field=models.ForeignKey(help_text='Select part to be used in BOM', limit_choices_to={'component': True, 'is_template': False}, on_delete=django.db.models.deletion.CASCADE, related_name='used_in', to='part.Part'),
        ),
    ]
