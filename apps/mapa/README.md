=====
mapa
=====

Quick start
-----------

1. Instale "mapa.zendesk" em INSTALLED_APPS no settings do seu projeto assim::

    INSTALLED_APPS = [
        ...
        'mapa.zendesk',
    ]

2. Adiciona o roteamento para base de dados::

    DATABASE_ROUTERS = [
        'mapa.zendesk.routers.ZendeskRouter'
    ]

3. Configure uma nova base de dados que seria utilizada para o roteamento dos modelos deste aplicativo:

    MAPA_ZENDESK_DATABASE_NAME = 'bonde'

    DATABASES = {
        ...,
        MAPA_ZENDESK_DATABASE_NAME: {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': 5432,
        }
    }