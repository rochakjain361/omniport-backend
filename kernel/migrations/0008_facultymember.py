# Generated by Django 2.0.3 on 2018-04-03 21:36

import swapper

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import kernel.mixins.period_mixin


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.KERNEL_DEPARTMENT_MODEL),
        ('kernel', '0007_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('removed', models.DateTimeField(blank=True, default=None, editable=False, null=True)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('designation', models.CharField(max_length=63)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=swapper.get_model_name('kernel', 'Department'))),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=swapper.get_model_name('kernel', 'Person'))),
            ],
            options={
                'swappable': swapper.swappable_setting('kernel', 'FacultyMember'),
            },
            bases=(kernel.mixins.period_mixin.PeriodMixin, models.Model),
        ),
    ]
