# Comandos e arquivos importantes do Django

- django-admin: comando utilizado para executar tarefas administrativas, como por exemplo _startproject_.
- python manage.py: tem a mesma finalidade do _django-admin_, sendo a diferença que o manage.py carrega a veriável de ambiente e o arquivo de configurações do Django (_settings.py_). Podemos, por exemplo, iniciar um servidor local com _manage.py_ com o _runserver_.
- asgi e wsgi: ambos são usando para o mesmo proposito: rodar o django em servidores externos.
- settings: configurações do Django e o qual é carregado pelo arquivo _manage.py_.
- urls: endpoints das aplicações.

# Métodos de requisição HTTP

- GET: O método GET é utilizado quando é realizada **somente**  a requisição dos dados.
- POST: O método POST faz a submição de dados para um recurso específico, o que pode causar mudanças ou efeitos colaterais no lado do servidor.
- PUT: O método PUT faz alterações em um recurso especificado.
- DELETE: O método DELETE faz a exclusão de um recurso especificado.