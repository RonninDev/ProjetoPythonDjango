### INICIANDO UM PROJETO DJANGO ###
-----------------------------------
# O primeiro passo é Configurar a venv e pasta com o projeto, isso pode ser feito através do VenvWrapper
# que ainda não domino (Atualizar este conteúdo) - Ou por hora utilizando a venv do Pycharm

# Instalando o Django
    pip install django
# Criando um Projeto
    django-admin startproject 'nome_do_projeto' . <- o Ponto final define a criação de um diretório extra
# Criando um App
    django-admin startapp 'nome_do_app'
# RODANDO SERVIDOR #
# 1º Forma - Utilizando o Debbug do PyCharm
# 2º Forma - Utilizando o Terminal
    'python manage.py runserver'
------------------------------------
### CONFIGURAÇÕES INICIAIS DO PROJETO ###

# VERIFICANDO O IMPORT DO 'OS'

# CONFIGURANDO A SECRETKEY (Atualizar)
# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-!y6hqp=c8ahl8-ou(q2a5h14qgv=b$2r)6vto+bs(!_ykw)7_1'

# ARQUIVO SETTINGS.py
# Incluindo Apps
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'NOME_DO_NOVO_APP',
# ]

# Incluindo Templates (Atualizar)
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
