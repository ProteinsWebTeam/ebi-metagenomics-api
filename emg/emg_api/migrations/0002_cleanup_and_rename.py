# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 10:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('emg_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel('BiomeHierarchyTree', 'Biome'),

        migrations.RenameModel('PipelineRelease', 'Pipeline'),

        migrations.RenameModel('AnalysisJob', 'Run'),
        migrations.AlterField(
            model_name='run',
            name='external_run_ids',
            field=models.CharField(
                db_column='EXTERNAL_RUN_IDS', max_length=100),
        ),
        migrations.RenameField(
            model_name='run',
            old_name='job_id',
            new_name='run_id',
        ),
        migrations.RenameField(
            model_name='run',
            old_name='external_run_ids',
            new_name='accession',
        ),
        migrations.RemoveField(
            model_name='run',
            name='re_run_count',
        ),

        migrations.AlterField(
            model_name='sample',
            name='ext_sample_id',
            field=models.CharField(
                db_column='EXT_SAMPLE_ID', max_length=20),
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='ext_sample_id',
            new_name='accession',
        ),

        migrations.AlterField(
            model_name='study',
            name='ext_study_id',
            field=models.CharField(
                db_column='EXT_STUDY_ID', max_length=20),
        ),
        migrations.RenameField(
            model_name='study',
            old_name='ext_study_id',
            new_name='accession',
        ),
        migrations.RemoveField(
            model_name='study',
            name='experimental_factor',
        ),
        migrations.RemoveField(
            model_name='study',
            name='ncbi_project_id',
        ),

        migrations.AlterField(
            model_name='pipelinereleasetool',
            name='how_tool_used_desc',
            field=models.TextField(blank=True, db_column='HOW_TOOL_USED_DESC', null=True),
        ),
        migrations.AlterField(
            model_name='pipelinereleasetool',
            name='pipeline',
            field=models.ForeignKey(db_column='PIPELINE_ID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='emg_api.Pipeline'),
        ),
        migrations.AlterField(
            model_name='pipelinereleasetool',
            name='tool',
            field=models.ForeignKey(db_column='TOOL_ID', on_delete=django.db.models.deletion.CASCADE, to='emg_api.PipelineTool'),
        ),

        migrations.AlterField(
            model_name='pipelinetool',
            name='description',
            field=models.TextField(blank=True, db_column='DESCRIPTION', null=True),
        ),
        migrations.AlterField(
            model_name='pipelinetool',
            name='exe_command',
            field=models.CharField(blank=True, db_column='EXE_COMMAND', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='pipelinetool',
            name='tool_name',
            field=models.CharField(blank=True, db_column='TOOL_NAME', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='pipelinetool',
            name='version',
            field=models.CharField(blank=True, db_column='VERSION', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='run',
            name='analysis_status',
            field=models.ForeignKey(db_column='ANALYSIS_STATUS_ID', on_delete=django.db.models.deletion.CASCADE, to='emg_api.AnalysisStatus'),
        ),
        migrations.AlterField(
            model_name='run',
            name='experiment_type',
            field=models.ForeignKey(db_column='EXPERIMENT_TYPE_ID', on_delete=django.db.models.deletion.CASCADE, related_name='runs', to='emg_api.ExperimentType'),
        ),
        migrations.AlterField(
            model_name='run',
            name='pipeline',
            field=models.ForeignKey(db_column='PIPELINE_ID', on_delete=django.db.models.deletion.CASCADE, related_name='runs', to='emg_api.Pipeline'),
        ),
        migrations.AlterField(
            model_name='run',
            name='sample',
            field=models.ForeignKey(db_column='SAMPLE_ID', on_delete=django.db.models.deletion.CASCADE, related_name='runs', to='emg_api.Sample'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='accession',
            field=models.CharField(db_column='EXT_SAMPLE_ID', default='ERS0000000', max_length=20),
        ),
        migrations.AlterField(
            model_name='sample',
            name='biome',
            field=models.ForeignKey(db_column='BIOME_ID', on_delete=django.db.models.deletion.CASCADE, related_name='samples', to='emg_api.Biome'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='study',
            field=models.ForeignKey(db_column='STUDY_ID', on_delete=django.db.models.deletion.CASCADE, related_name='samples', to='emg_api.Study'),
        ),
        migrations.AlterField(
            model_name='samplepublication',
            name='pub',
            field=models.ForeignKey(db_column='PUB_ID', on_delete=django.db.models.deletion.CASCADE, to='emg_api.Publication'),
        ),
        migrations.AlterField(
            model_name='samplepublication',
            name='sample',
            field=models.ForeignKey(db_column='SAMPLE_ID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='emg_api.Sample'),
        ),
        migrations.AlterField(
            model_name='study',
            name='accession',
            field=models.CharField(db_column='EXT_STUDY_ID', default='ERP000000', max_length=20),
        ),
        migrations.AlterField(
            model_name='study',
            name='biome',
            field=models.ForeignKey(db_column='BIOME_ID', on_delete=django.db.models.deletion.CASCADE, related_name='studies', to='emg_api.Biome'),
        ),
        migrations.AlterField(
            model_name='studypublication',
            name='pub',
            field=models.ForeignKey(db_column='PUB_ID', on_delete=django.db.models.deletion.CASCADE, to='emg_api.Publication'),
        ),
        migrations.AlterField(
            model_name='studypublication',
            name='study',
            field=models.ForeignKey(db_column='STUDY_ID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='emg_api.Study'),
        ),

        migrations.AlterModelOptions(
            name='analysisstatus',
            options={'ordering': ('analysis_status_id',)},
        ),
        migrations.AlterModelOptions(
            name='biome',
            options={'ordering': ('biome_id',)},
        ),
        migrations.AlterModelOptions(
            name='pipeline',
            options={'ordering': ('release_version',)},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ('pub_id',)},
        ),
        migrations.AlterModelOptions(
            name='run',
            options={'ordering': ('accession',)},
        ),
        migrations.AlterModelOptions(
            name='sample',
            options={'ordering': ('accession',)},
        ),
        migrations.AlterModelOptions(
            name='study',
            options={'ordering': ('accession',)},
        ),
        migrations.AlterUniqueTogether(
            name='pipeline',
            unique_together=set([('pipeline_id', 'release_version')]),
        ),
        migrations.AlterUniqueTogether(
            name='pipelinereleasetool',
            unique_together=set([('pipeline', 'tool_group_id'), ('pipeline', 'tool')]),
        ),
        migrations.AlterUniqueTogether(
            name='run',
            unique_together=set([('run_id', 'accession')]),
        ),
        migrations.AlterUniqueTogether(
            name='sample',
            unique_together=set([('sample_id', 'accession')]),
        ),
        migrations.AlterUniqueTogether(
            name='samplepublication',
            unique_together=set([('sample', 'pub')]),
        ),
        migrations.AlterUniqueTogether(
            name='study',
            unique_together=set([('study_id', 'accession')]),
        ),
        migrations.AlterUniqueTogether(
            name='studypublication',
            unique_together=set([('study', 'pub')]),
        ),

        # Ticket: IBU-6868
        # combine external_run_id and pipeline version to restrict duplicates
        migrations.AlterUniqueTogether(
            name='run',
            unique_together=set([('pipeline', 'accession')]),
        ),

        # FullText index
        migrations.RunSQL(
            "CREATE FULLTEXT INDEX biome_biome_name_ts_idx ON biome_hierarchy_tree (biome_name)"
        ),
        migrations.RunSQL(
            "CREATE FULLTEXT INDEX biome_lineage_ts_idx ON biome_hierarchy_tree (lineage)"
        ),
        migrations.RunSQL(
            "CREATE FULLTEXT INDEX study_study_name_ts_idx ON study(study_name)"
        ),
        migrations.RunSQL(
            "CREATE FULLTEXT INDEX study_study_abstract_ts_idx ON study (study_abstract)"
        ),
        migrations.RunSQL(
            "CREATE FULLTEXT INDEX publication_publication_title_ts_idx ON publication (pub_title)"
        ),
        migrations.RunSQL(
            "CREATE FULLTEXT INDEX publication_pub_abstract_ts_idx ON publication (pub_abstract)"
        ),
        migrations.RunSQL(
            "CREATE FULLTEXT INDEX pipeline_description_ts_idx ON pipeline_release (description)"
        ),
        migrations.RunSQL(
            "CREATE FULLTEXT INDEX pipeline_changes_ts_idx ON pipeline_release (changes)"
        ),
        migrations.RunSQL(
            "CREATE FULLTEXT INDEX sample_sample_name_ts_idx ON sample (sample_name)"
        ),
    ]
