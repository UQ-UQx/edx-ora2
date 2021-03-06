# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AIClassifierSet'
        db.create_table('assessment_aiclassifierset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rubric', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['assessment.Rubric'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, db_index=True)),
        ))
        db.send_create_signal('assessment', ['AIClassifierSet'])

        # Adding model 'AIClassifier'
        db.create_table('assessment_aiclassifier', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classifier_set', self.gf('django.db.models.fields.related.ForeignKey')(related_name='classifiers', to=orm['assessment.AIClassifierSet'])),
            ('criterion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['assessment.Criterion'])),
            ('classifier_data', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('algorithm_id', self.gf('django.db.models.fields.CharField')(max_length=128, db_index=True)),
        ))
        db.send_create_signal('assessment', ['AIClassifier'])

        # Adding model 'AITrainingWorkflow'
        db.create_table('assessment_aitrainingworkflow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=36, blank=True)),
            ('algorithm_id', self.gf('django.db.models.fields.CharField')(max_length=128, db_index=True)),
            ('classifier_set', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='training_workflow', null=True, to=orm['assessment.AIClassifierSet'])),
            ('scheduled_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, db_index=True)),
            ('completed_at', self.gf('django.db.models.fields.DateTimeField')(null=True, db_index=True)),
        ))
        db.send_create_signal('assessment', ['AITrainingWorkflow'])

        # Adding M2M table for field training_examples on 'AITrainingWorkflow'
        db.create_table('assessment_aitrainingworkflow_training_examples', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('aitrainingworkflow', models.ForeignKey(orm['assessment.aitrainingworkflow'], null=False)),
            ('trainingexample', models.ForeignKey(orm['assessment.trainingexample'], null=False))
        ))
        db.create_unique('assessment_aitrainingworkflow_training_examples', ['aitrainingworkflow_id', 'trainingexample_id'])


    def backwards(self, orm):
        # Deleting model 'AIClassifierSet'
        db.delete_table('assessment_aiclassifierset')

        # Deleting model 'AIClassifier'
        db.delete_table('assessment_aiclassifier')

        # Deleting model 'AITrainingWorkflow'
        db.delete_table('assessment_aitrainingworkflow')

        # Removing M2M table for field training_examples on 'AITrainingWorkflow'
        db.delete_table('assessment_aitrainingworkflow_training_examples')


    models = {
        'assessment.aiclassifier': {
            'Meta': {'object_name': 'AIClassifier'},
            'algorithm_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'classifier_data': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'classifier_set': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'classifiers'", 'to': "orm['assessment.AIClassifierSet']"}),
            'criterion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['assessment.Criterion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'assessment.aiclassifierset': {
            'Meta': {'object_name': 'AIClassifierSet'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rubric': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['assessment.Rubric']"})
        },
        'assessment.aitrainingworkflow': {
            'Meta': {'object_name': 'AITrainingWorkflow'},
            'algorithm_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'classifier_set': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'training_workflow'", 'null': 'True', 'to': "orm['assessment.AIClassifierSet']"}),
            'completed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scheduled_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'training_examples': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'+'", 'symmetrical': 'False', 'to': "orm['assessment.TrainingExample']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '36', 'blank': 'True'})
        },
        'assessment.assessment': {
            'Meta': {'ordering': "['-scored_at', '-id']", 'object_name': 'Assessment'},
            'feedback': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '10000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rubric': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assessment.Rubric']"}),
            'score_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'scored_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'scorer_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_index': 'True'}),
            'submission_uuid': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'})
        },
        'assessment.assessmentfeedback': {
            'Meta': {'object_name': 'AssessmentFeedback'},
            'assessments': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'related_name': "'assessment_feedback'", 'symmetrical': 'False', 'to': "orm['assessment.Assessment']"}),
            'feedback_text': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '10000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'related_name': "'assessment_feedback'", 'symmetrical': 'False', 'to': "orm['assessment.AssessmentFeedbackOption']"}),
            'submission_uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128', 'db_index': 'True'})
        },
        'assessment.assessmentfeedbackoption': {
            'Meta': {'object_name': 'AssessmentFeedbackOption'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'assessment.assessmentpart': {
            'Meta': {'object_name': 'AssessmentPart'},
            'assessment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parts'", 'to': "orm['assessment.Assessment']"}),
            'feedback': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'option': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['assessment.CriterionOption']"})
        },
        'assessment.criterion': {
            'Meta': {'ordering': "['rubric', 'order_num']", 'object_name': 'Criterion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order_num': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'prompt': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            'rubric': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'criteria'", 'to': "orm['assessment.Rubric']"})
        },
        'assessment.criterionoption': {
            'Meta': {'ordering': "['criterion', 'order_num']", 'object_name': 'CriterionOption'},
            'criterion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'options'", 'to': "orm['assessment.Criterion']"}),
            'explanation': ('django.db.models.fields.TextField', [], {'max_length': '10000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order_num': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'points': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'assessment.peerworkflow': {
            'Meta': {'ordering': "['created_at', 'id']", 'object_name': 'PeerWorkflow'},
            'completed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'course_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_index': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'grading_completed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'student_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_index': 'True'}),
            'submission_uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128', 'db_index': 'True'})
        },
        'assessment.peerworkflowitem': {
            'Meta': {'ordering': "['started_at', 'id']", 'object_name': 'PeerWorkflowItem'},
            'assessment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assessment.Assessment']", 'null': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'graded_by'", 'to': "orm['assessment.PeerWorkflow']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'scorer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'graded'", 'to': "orm['assessment.PeerWorkflow']"}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'submission_uuid': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'})
        },
        'assessment.rubric': {
            'Meta': {'object_name': 'Rubric'},
            'content_hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'assessment.studenttrainingworkflow': {
            'Meta': {'object_name': 'StudentTrainingWorkflow'},
            'course_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'student_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_index': 'True'}),
            'submission_uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128', 'db_index': 'True'})
        },
        'assessment.studenttrainingworkflowitem': {
            'Meta': {'ordering': "['workflow', 'order_num']", 'unique_together': "(('workflow', 'order_num'),)", 'object_name': 'StudentTrainingWorkflowItem'},
            'completed_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_num': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'started_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'training_example': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assessment.TrainingExample']"}),
            'workflow': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['assessment.StudentTrainingWorkflow']"})
        },
        'assessment.trainingexample': {
            'Meta': {'object_name': 'TrainingExample'},
            'content_hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'options_selected': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['assessment.CriterionOption']", 'symmetrical': 'False'}),
            'raw_answer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'rubric': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['assessment.Rubric']"})
        }
    }

    complete_apps = ['assessment']