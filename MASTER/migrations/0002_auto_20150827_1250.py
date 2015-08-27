# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MASTER', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dusun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_dusun', models.CharField(max_length=100)),
                ('keterangan', models.CharField(max_length=500)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provinsi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_provinsi', models.CharField(max_length=100)),
                ('keterangan', models.CharField(max_length=500)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='kecamatan',
            old_name='nama_kabupaten',
            new_name='id_kabupaten',
        ),
        migrations.RenameField(
            model_name='kelurahan',
            old_name='nama_kecamatan',
            new_name='id_kecamatan',
        ),
        migrations.AddField(
            model_name='dusun',
            name='id_kelurahan',
            field=models.ForeignKey(to='MASTER.Kelurahan'),
        ),
        migrations.AddField(
            model_name='kabupaten',
            name='id_provinsi',
            field=models.ForeignKey(default=1, to='MASTER.Provinsi'),
            preserve_default=False,
        ),
    ]
