# Generated by Django 4.2 on 2023-04-14 19:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SolidarityMatches",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("community_id", models.BigIntegerField()),
                ("created_at", models.DateTimeField()),
                ("status", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "solidarity_matches",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="SolidarityTickets",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("assignee_id", models.BigIntegerField(blank=True, null=True)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                ("custom_fields", models.JSONField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("group_id", models.BigIntegerField(blank=True, null=True)),
                ("ticket_id", models.BigIntegerField(unique=True)),
                ("organization_id", models.BigIntegerField(blank=True, null=True)),
                ("raw_subject", models.TextField(blank=True, null=True)),
                ("requester_id", models.BigIntegerField(blank=True, null=True)),
                ("status", models.TextField(blank=True, null=True)),
                ("subject", models.TextField(blank=True, null=True)),
                ("submitter_id", models.BigIntegerField(blank=True, null=True)),
                ("tags", models.JSONField(blank=True, null=True)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
                ("status_acolhimento", models.TextField(blank=True, null=True)),
                ("nome_voluntaria", models.TextField(blank=True, null=True)),
                ("link_match", models.TextField(blank=True, null=True)),
                ("nome_msr", models.TextField(blank=True, null=True)),
                ("data_inscricao_bonde", models.TextField(blank=True, null=True)),
                ("data_encaminhamento", models.TextField(blank=True, null=True)),
                ("status_inscricao", models.TextField(blank=True, null=True)),
                ("telefone", models.TextField(blank=True, null=True)),
                ("estado", models.TextField(blank=True, null=True)),
                ("cidade", models.TextField(blank=True, null=True)),
                ("community_id", models.BigIntegerField()),
                ("external_id", models.BigIntegerField(blank=True, null=True)),
                ("atrelado_ao_ticket", models.BigIntegerField(blank=True, null=True)),
                ("match_syncronized", models.BooleanField()),
            ],
            options={
                "db_table": "solidarity_tickets",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="SolidarityUsers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.BigIntegerField(unique=True)),
                ("url", models.TextField(blank=True, null=True)),
                ("name", models.TextField(blank=True, null=True)),
                ("email", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
                ("time_zone", models.TextField(blank=True, null=True)),
                ("iana_time_zone", models.TextField(blank=True, null=True)),
                ("phone", models.TextField(blank=True, null=True)),
                ("shared_phone_number", models.BooleanField(blank=True, null=True)),
                ("photo", models.JSONField(blank=True, null=True)),
                ("locale_id", models.BigIntegerField(blank=True, null=True)),
                ("locale", models.TextField(blank=True, null=True)),
                ("organization_id", models.BigIntegerField(blank=True, null=True)),
                ("role", models.TextField(blank=True, null=True)),
                ("verified", models.BooleanField(blank=True, null=True)),
                ("external_id", models.BigIntegerField(blank=True, null=True)),
                ("tags", models.JSONField(blank=True, null=True)),
                ("alias", models.TextField(blank=True, null=True)),
                ("active", models.BooleanField(blank=True, null=True)),
                ("shared", models.BooleanField(blank=True, null=True)),
                ("shared_agent", models.BooleanField(blank=True, null=True)),
                ("last_login_at", models.DateTimeField(blank=True, null=True)),
                ("two_factor_auth_enabled", models.BooleanField(blank=True, null=True)),
                ("signature", models.TextField(blank=True, null=True)),
                ("details", models.TextField(blank=True, null=True)),
                ("notes", models.TextField(blank=True, null=True)),
                ("role_type", models.BigIntegerField(blank=True, null=True)),
                ("custom_role_id", models.BigIntegerField(blank=True, null=True)),
                ("moderator", models.BooleanField(blank=True, null=True)),
                ("ticket_restriction", models.TextField(blank=True, null=True)),
                ("only_private_comments", models.BooleanField(blank=True, null=True)),
                ("restricted_agent", models.BooleanField(blank=True, null=True)),
                ("suspended", models.BooleanField(blank=True, null=True)),
                ("chat_only", models.BooleanField(blank=True, null=True)),
                ("default_group_id", models.BigIntegerField(blank=True, null=True)),
                ("report_csv", models.BooleanField(blank=True, null=True)),
                ("user_fields", models.JSONField(blank=True, null=True)),
                ("address", models.TextField(blank=True, null=True)),
                (
                    "atendimentos_concludos_calculado_field",
                    models.BigIntegerField(
                        blank=True,
                        db_column="atendimentos_concludos_calculado_",
                        null=True,
                    ),
                ),
                (
                    "atendimentos_concluidos",
                    models.BigIntegerField(blank=True, null=True),
                ),
                (
                    "atendimentos_em_andamento",
                    models.BigIntegerField(blank=True, null=True),
                ),
                (
                    "atendimentos_em_andamento_calculado_field",
                    models.BigIntegerField(
                        blank=True,
                        db_column="atendimentos_em_andamento_calculado_",
                        null=True,
                    ),
                ),
                ("cep", models.TextField(blank=True, null=True)),
                ("city", models.TextField(blank=True, null=True)),
                ("condition", models.TextField(blank=True, null=True)),
                ("cor", models.TextField(blank=True, null=True)),
                (
                    "data_de_inscricao_no_bonde",
                    models.DateTimeField(blank=True, null=True),
                ),
                (
                    "disponibilidade_de_atendimentos",
                    models.TextField(blank=True, null=True),
                ),
                ("encaminhamentos", models.BigIntegerField(blank=True, null=True)),
                (
                    "encaminhamentos_realizados_calculado_field",
                    models.BigIntegerField(
                        blank=True,
                        db_column="encaminhamentos_realizados_calculado_",
                        null=True,
                    ),
                ),
                ("latitude", models.TextField(blank=True, null=True)),
                ("longitude", models.TextField(blank=True, null=True)),
                ("occupation_area", models.TextField(blank=True, null=True)),
                ("registration_number", models.TextField(blank=True, null=True)),
                ("state", models.TextField(blank=True, null=True)),
                ("tipo_de_acolhimento", models.TextField(blank=True, null=True)),
                (
                    "ultima_atualizacao_de_dados",
                    models.DateTimeField(blank=True, null=True),
                ),
                ("whatsapp", models.TextField(blank=True, null=True)),
                ("permanently_deleted", models.BooleanField(blank=True, null=True)),
                ("community_id", models.BigIntegerField()),
            ],
            options={
                "db_table": "solidarity_users",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="SolidarityZdTickets",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("assignee_id", models.BigIntegerField(blank=True, null=True)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                ("custom_fields", models.JSONField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("group_id", models.BigIntegerField(blank=True, null=True)),
                ("ticket_id", models.BigIntegerField(unique=True)),
                ("organization_id", models.BigIntegerField(blank=True, null=True)),
                ("raw_subject", models.TextField(blank=True, null=True)),
                ("requester_id", models.BigIntegerField(blank=True, null=True)),
                ("status", models.TextField(blank=True, null=True)),
                ("subject", models.TextField(blank=True, null=True)),
                ("submitter_id", models.BigIntegerField(blank=True, null=True)),
                ("tags", models.JSONField(blank=True, null=True)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
                ("status_acolhimento", models.TextField(blank=True, null=True)),
                ("nome_voluntaria", models.TextField(blank=True, null=True)),
                ("link_match", models.TextField(blank=True, null=True)),
                ("nome_msr", models.TextField(blank=True, null=True)),
                ("data_inscricao_bonde", models.DateTimeField(blank=True, null=True)),
                ("data_encaminhamento", models.DateTimeField(blank=True, null=True)),
                ("status_inscricao", models.TextField(blank=True, null=True)),
                ("telefone", models.TextField(blank=True, null=True)),
                ("estado", models.TextField(blank=True, null=True)),
                ("cidade", models.TextField(blank=True, null=True)),
                ("community_id", models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "solidarity_zd_tickets",
                "managed": False,
            },
        ),
    ]