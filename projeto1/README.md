# Comandos e arquivos importantes do Django

- django-admin: comando utilizado para executar tarefas administrativas, como por exemplo _startproject_.
- python manage.py: tem a mesma finalidade do _django-admin_, sendo a diferença que o manage.py carrega a veriável de ambiente e o arquivo de configurações do Django (_settings.py_). Podemos, por exemplo, iniciar um servidor local com _manage.py_ com o _runserver_.
- asgi e wsgi: ambos são usando para o mesmo proposito: rodar o django em servidores externos.
- settings: configurações do Django e o qual é carregado pelo arquivo _manage.py_.
- urls: endpoints das aplicações.