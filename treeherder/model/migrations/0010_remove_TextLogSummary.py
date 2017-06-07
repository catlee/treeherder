# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 14:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0009_add_is_try_repo'),
    ]

    operations = [migrations.RunSQL(
        sql="""
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE `text_log_summary_line` CASCADE;
DROP TABLE `text_log_summary` CASCADE;
""",
        reverse_sql="""
CREATE TABLE `text_log_summary_line` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `line_number` integer UNSIGNED NULL, `bug_number` integer UNSIGNED NULL, `verified` bool NOT NULL);
CREATE TABLE `text_log_summary` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `job_guid` varchar(50) NOT NULL, `text_log_summary_artifact_id` integer UNSIGNED NULL, `bug_suggestions_artifact_id` integer UNSIGNED NULL);
ALTER TABLE `text_log_summary_line` ADD COLUMN `summary_id` bigint NOT NULL;
ALTER TABLE `text_log_summary_line` ADD COLUMN `failure_line_id` bigint NULL;
ALTER TABLE `text_log_summary` ADD COLUMN `repository_id` integer NOT NULL;
ALTER TABLE `text_log_summary` ADD CONSTRAINT `text_log_summary_job_guid_repository_id_6b30431d_uniq` UNIQUE (`job_guid`, `repository_id`);
ALTER TABLE `text_log_summary_line` ADD CONSTRAINT `text_log_summary_line_summary_id_2ca77591_fk_text_log_summary_id` FOREIGN KEY (`summary_id`) REFERENCES `text_log_summary` (`id`);
ALTER TABLE `text_log_summary_line` ADD CONSTRAINT `text_log_summary_lin_failure_line_id_ff9925a9_fk_failure_l` FOREIGN KEY (`failure_line_id`) REFERENCES `failure_line` (`id`);
ALTER TABLE `text_log_summary` ADD CONSTRAINT `text_log_summary_repository_id_46c559dc_fk_repository_id` FOREIGN KEY (`repository_id`) REFERENCES `repository` (`id`);""",
        state_operations=[
            migrations.AlterUniqueTogether(
                name='textlogsummary',
                unique_together=set([]),
            ),
            migrations.RemoveField(
                model_name='textlogsummary',
                name='repository',
            ),
            migrations.RemoveField(
                model_name='textlogsummaryline',
                name='failure_line',
            ),
            migrations.RemoveField(
                model_name='textlogsummaryline',
                name='summary',
            ),
            migrations.DeleteModel(
                name='TextLogSummary',
            ),
            migrations.DeleteModel(
                name='TextLogSummaryLine',
            ),
        ]
    )]