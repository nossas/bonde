# Bonde APPS

Espaço para experimentar aplicativos Python e Django isoladamente, considerando as necessidades e demandas da organização NOSSAS que contribui com a construção e discussão de tecnologias para o setor de ativismo civico.

# Como usar

Faça download do codebase:

```
git clone --recurse-submodules https://github.com/nossas/bonde.git
```

Por ser baseado em projeto Python e Django, sugerimos o uso do ambiente virtual dísponivel nos módulos built-in do Python3.

```shell
python3 -m venv venv

source venv/bin/activate
```

## Gerenciamento de dependencias

Instale as dependencias para desenvolvimento

```
pip install -r requirements/development.txt
```

### Aplicações em desenvolvimento

Como descrevemos no início desse documento, esse espaço busca manter uma estrutura de experimentação para estrategias que queremos adotar dentro de tecnologia no NOSSAS, dentro da pasta `apps/` encontramos algumas aplicações que funcionam separadamente a esse projeto modelo, por esse motivo não se encontram nas dependencias de desenvolvimento, para instalar essas aplicações precisamos adicionar um link símbolico ao projeto modelo.

Criamos um comando no projeto modelo que facilita a criação dos links:

```
python manage.py installapps all
```


## Executando o projeto

Dentro da pasta `web` execute o comando para rodar o servidor de desenvolvimento, e acesse no seu navegador a url: http://localhost:8000

```
python manage.py runserver
```

## Gerenciamento de migrações

O django possui uma ORM que facilita a modelagem e o gerenciamento do banco de dados, a migração é uma extensão que permite versionar as mudanças dessa modelagem, você pode ler mais na [documentação oficial](https://docs.djangoproject.com/en/4.2/topics/migrations/)

Execute o comando `python manage.py migrate` para executar migrações pendentes em sua base de dados.

O comando `python manage.py makemigrations` verifica mudanças nos seus modelos de dados e cria novas migrações no caso de mudanças.
