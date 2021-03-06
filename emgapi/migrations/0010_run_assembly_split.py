# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-17 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.db.models import Q


def populate_assemblies(apps, schema_editor):
    Run = apps.get_model("emgapi", "Run")
    Assembly = apps.get_model("emgapi", "Assembly")
    AssemblyRun = apps.get_model("emgapi", "AssemblyRun")
    AssemblySample = apps.get_model("emgapi", "AssemblySample")
    AnalysisJob = apps.get_model("emgapi", "AnalysisJob")
    ExperimentType = apps.get_model("emgapi", "ExperimentType")
    try:
        experiment_type = ExperimentType.objects.get(experiment_type="assembly")
    except ExperimentType.DoesNotExist:
        return
    AssemblyMapping = apps.get_model("emgena", "AssemblyMapping")

    # total = Run.objects.filter(experiment_type=experiment_type).count()
    for run in Run.objects.filter(experiment_type=experiment_type):
        run_origin = None
        if run.secondary_accession.startswith("ERR"):
            try:
                run_origin = Run.objects.get(accession=run.accession)
            except Run.DoesNotExist:
                pass

        _assembly = AssemblyMapping.objects.using('ena_pro') \
            .filter(
                Q(legacy_accession=run.accession) |
                Q(accession=run.accession) |
                Q(legacy_accession=run.secondary_accession) |
                Q(accession=run.secondary_accession)
            ).order_by('-legacy_version').first()

        try:
            run_origin = Run.objects.get(accession=_assembly.name)
        except Run.DoesNotExist:
            run_origin = None
        except AttributeError:
            run_origin = None

        if _assembly is None:
            a = Assembly.objects.create(
                accession=run.accession,
                legacy_accession=run.secondary_accession,
                status_id=run.status_id,
                experiment_type=experiment_type,
            )
            if run_origin is not None:
                AssemblyRun.objects.create(
                    assembly=a,
                    run=run_origin
                )
            AssemblySample.objects.create(
                assembly=a,
                sample=run.sample
            )
            _runs = Run.objects.filter(sample=run.sample) \
                .exclude(experiment_type=experiment_type)
            for r in _runs:
                AssemblyRun.objects.create(
                    assembly=a,
                    run=r
                )
        else:
            a = Assembly.objects.create(
                accession=_assembly.accession,
                legacy_accession=_assembly.legacy_accession,
                wgs_accession=_assembly.wgs_accession,
                status_id=run.status_id,
                experiment_type=experiment_type,
            )
            if run_origin is not None:
                AssemblyRun.objects.create(
                    assembly=a,
                    run=run_origin
                )
            AssemblySample.objects.create(
                assembly=a,
                sample=run.sample
            )
        for aj in AnalysisJob.objects.filter(run=run):
            aj.run = None
            aj.assembly = a
            aj.save()
        if AnalysisJob.objects.filter(run=run).count() < 1:
            run.delete()


class Migration(migrations.Migration):
    dependencies = [
        ('emgapi', '0009_remove_gsccvcv'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assembly',
            fields=[
                ('assembly_id', models.BigAutoField(db_column='ASSEMBLY_ID', primary_key=True, serialize=False)),
                ('accession', models.CharField(blank=True, db_column='ACCESSION', max_length=80, null=True)),
                ('wgs_accession', models.CharField(blank=True, db_column='WGS_ACCESSION', max_length=100, null=True)),
                ('legacy_accession', models.CharField(blank=True, db_column='LEGACY_ACCESSION', max_length=100, null=True)),
            ],
            options={
                'db_table': 'ASSEMBLY',
                'ordering': ('accession',),
            },
        ),
        migrations.CreateModel(
            name='AssemblyRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assembly', models.ForeignKey(db_column='ASSEMBLY_ID', on_delete=django.db.models.deletion.CASCADE, to='emgapi.Assembly')),
                ('run', models.ForeignKey(db_column='RUN_ID', on_delete=django.db.models.deletion.CASCADE, to='emgapi.Run')),
            ],
            options={
                'db_table': 'ASSEMBLY_RUN',
            },
        ),
        migrations.CreateModel(
            name='AssemblySample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assembly', models.ForeignKey(db_column='ASSEMBLY_ID', on_delete=django.db.models.deletion.CASCADE, to='emgapi.Assembly')),
                ('sample', models.ForeignKey(db_column='SAMPLE_ID', on_delete=django.db.models.deletion.CASCADE, to='emgapi.Sample')),
            ],
            options={
                'db_table': 'ASSEMBLY_SAMPLE',
            },
        ),

        migrations.AddField(
            model_name='assembly',
            name='experiment_type',
            field=models.ForeignKey(blank=True, db_column='EXPERIMENT_TYPE_ID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assemblies', to='emgapi.ExperimentType'),
        ),
        migrations.AddField(
            model_name='assembly',
            name='runs',
            field=models.ManyToManyField(blank=True, related_name='assemblies', through='emgapi.AssemblyRun', to='emgapi.Run'),
        ),
        migrations.AddField(
            model_name='assembly',
            name='samples',
            field=models.ManyToManyField(blank=True, related_name='assemblies', through='emgapi.AssemblySample', to='emgapi.Sample'),
        ),
        migrations.AddField(
            model_name='assembly',
            name='status_id',
            field=models.ForeignKey(db_column='STATUS_ID', default=2, on_delete=django.db.models.deletion.CASCADE, related_name='assemblies', to='emgapi.Status'),
        ),

        migrations.AlterUniqueTogether(
            name='assemblysample',
            unique_together=set([('assembly', 'sample')]),
        ),
        migrations.AlterUniqueTogether(
            name='assemblyrun',
            unique_together=set([('assembly', 'run')]),
        ),
        migrations.AlterUniqueTogether(
            name='assembly',
            unique_together=set([('accession', 'wgs_accession', 'legacy_accession'), ('assembly_id', 'accession')]),
        ),

        migrations.AddField(
            model_name='analysisjob',
            name='assembly',
            field=models.ForeignKey(blank=True, db_column='ASSEMBLY_ID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='analyses', to='emgapi.Assembly'),
        ),

        migrations.RunPython(populate_assemblies),

    ]
