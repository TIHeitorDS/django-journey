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

Links úteis [status de respostas HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status) e
[HTTP request response](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods).

# Django Templates
Os **templates** no Django são arquivos HTML dinâmicos. Além disso, nos templates 
é possível usar variáveis, tags e filtros.

### Vaiáveis
As variáveis exibem os valores passado no **context**. Sua sintaxe é ``{{ my_var }}``.

### Tags e filters
As tags são usadas no processo de renderização lógica. Por exemplo: condicionais, laços de repetição, carregar templates 
parciais, herança de template etc.. A sintaxe para usar tags é `` {% and %} ``.

Os filtros transformam argumentos de variáveis e tags. Sintaxe: ``{{ something|some_filter }}``

Documentação oficial sobre de templates tags e filters: https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#top.