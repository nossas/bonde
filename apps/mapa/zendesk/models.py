# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SolidarityUsers(models.Model):
    user_id = models.BigIntegerField(unique=True)
    url = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    time_zone = models.TextField(blank=True, null=True)
    iana_time_zone = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    shared_phone_number = models.BooleanField(blank=True, null=True)
    photo = models.JSONField(blank=True, null=True)
    locale_id = models.BigIntegerField(blank=True, null=True)
    locale = models.TextField(blank=True, null=True)
    organization_id = models.BigIntegerField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)
    verified = models.BooleanField(blank=True, null=True)
    external_id = models.BigIntegerField(blank=True, null=True)
    tags = models.JSONField(blank=True, null=True)
    alias = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    shared = models.BooleanField(blank=True, null=True)
    shared_agent = models.BooleanField(blank=True, null=True)
    last_login_at = models.DateTimeField(blank=True, null=True)
    two_factor_auth_enabled = models.BooleanField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    role_type = models.BigIntegerField(blank=True, null=True)
    custom_role_id = models.BigIntegerField(blank=True, null=True)
    moderator = models.BooleanField(blank=True, null=True)
    ticket_restriction = models.TextField(blank=True, null=True)
    only_private_comments = models.BooleanField(blank=True, null=True)
    restricted_agent = models.BooleanField(blank=True, null=True)
    suspended = models.BooleanField(blank=True, null=True)
    chat_only = models.BooleanField(blank=True, null=True)
    default_group_id = models.BigIntegerField(blank=True, null=True)
    report_csv = models.BooleanField(blank=True, null=True)
    user_fields = models.JSONField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    atendimentos_concludos_calculado_field = models.BigIntegerField(db_column='atendimentos_concludos_calculado_', blank=True, null=True)  # Field renamed because it ended with '_'.
    atendimentos_concluidos = models.BigIntegerField(blank=True, null=True)
    atendimentos_em_andamento = models.BigIntegerField(blank=True, null=True)
    atendimentos_em_andamento_calculado_field = models.BigIntegerField(db_column='atendimentos_em_andamento_calculado_', blank=True, null=True)  # Field renamed because it ended with '_'.
    cep = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    condition = models.TextField(blank=True, null=True)
    cor = models.TextField(blank=True, null=True)
    data_de_inscricao_no_bonde = models.DateTimeField(blank=True, null=True)
    disponibilidade_de_atendimentos = models.TextField(blank=True, null=True)
    encaminhamentos = models.BigIntegerField(blank=True, null=True)
    encaminhamentos_realizados_calculado_field = models.BigIntegerField(db_column='encaminhamentos_realizados_calculado_', blank=True, null=True)  # Field renamed because it ended with '_'.
    latitude = models.TextField(blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)
    occupation_area = models.TextField(blank=True, null=True)
    registration_number = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    tipo_de_acolhimento = models.TextField(blank=True, null=True)
    ultima_atualizacao_de_dados = models.DateTimeField(blank=True, null=True)
    whatsapp = models.TextField(blank=True, null=True)
    permanently_deleted = models.BooleanField(blank=True, null=True)
    # community = models.ForeignKey('Communities', models.DO_NOTHING, blank=True, null=True)
    community_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'solidarity_users'
    
    def __str__(self):
        return self.name


class SolidarityTickets(models.Model):
    assignee_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    custom_fields = models.JSONField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    group_id = models.BigIntegerField(blank=True, null=True)
    ticket_id = models.BigIntegerField(unique=True)
    organization_id = models.BigIntegerField(blank=True, null=True)
    raw_subject = models.TextField(blank=True, null=True)
    requester_id = models.BigIntegerField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    submitter_id = models.BigIntegerField(blank=True, null=True)
    tags = models.JSONField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status_acolhimento = models.TextField(blank=True, null=True)
    nome_voluntaria = models.TextField(blank=True, null=True)
    link_match = models.TextField(blank=True, null=True)
    nome_msr = models.TextField(blank=True, null=True)
    data_inscricao_bonde = models.TextField(blank=True, null=True)
    data_encaminhamento = models.TextField(blank=True, null=True)
    status_inscricao = models.TextField(blank=True, null=True)
    telefone = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    cidade = models.TextField(blank=True, null=True)
    # community = models.ForeignKey('Communities', models.DO_NOTHING, blank=True, null=True)
    community_id = models.BigIntegerField()
    external_id = models.BigIntegerField(blank=True, null=True)
    atrelado_ao_ticket = models.BigIntegerField(blank=True, null=True)
    match_syncronized = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'solidarity_tickets'


class SolidarityZdTickets(models.Model):
    assignee_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    custom_fields = models.JSONField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    group_id = models.BigIntegerField(blank=True, null=True)
    ticket_id = models.BigIntegerField(unique=True)
    organization_id = models.BigIntegerField(blank=True, null=True)
    raw_subject = models.TextField(blank=True, null=True)
    requester_id = models.BigIntegerField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    submitter_id = models.BigIntegerField(blank=True, null=True)
    tags = models.JSONField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status_acolhimento = models.TextField(blank=True, null=True)
    nome_voluntaria = models.TextField(blank=True, null=True)
    link_match = models.TextField(blank=True, null=True)
    nome_msr = models.TextField(blank=True, null=True)
    data_inscricao_bonde = models.DateTimeField(blank=True, null=True)
    data_encaminhamento = models.DateTimeField(blank=True, null=True)
    status_inscricao = models.TextField(blank=True, null=True)
    telefone = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    cidade = models.TextField(blank=True, null=True)
    community_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solidarity_zd_tickets'


class SolidarityMatches(models.Model):
    individuals_ticket = models.ForeignKey(SolidarityTickets, models.DO_NOTHING, related_name='individuals', to_field='ticket_id', blank=True, null=True)
    volunteers_ticket = models.ForeignKey(SolidarityTickets, models.DO_NOTHING, related_name='volunteers', to_field='ticket_id', blank=True, null=True)
    individuals_user = models.ForeignKey(SolidarityUsers, models.DO_NOTHING, related_name='individuals', to_field='user_id', blank=True, null=True)
    volunteers_user = models.ForeignKey(SolidarityUsers, models.DO_NOTHING, related_name='volunteers', to_field='user_id', blank=True, null=True)
    # community = models.ForeignKey('Communities', models.DO_NOTHING, blank=True, null=True)
    community_id = models.BigIntegerField()
    created_at = models.DateTimeField()
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solidarity_matches'
        unique_together = (('individuals_ticket', 'volunteers_ticket'),)
