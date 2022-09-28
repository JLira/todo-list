# TODO - List

Teste de Back-end ToDo List

## Como desenvolver?

1. Clone o reposotório.
2. Crie um virtualenv com Python 3.5
3. Ative o vitualenv.
4. Instale as dependências.
5. Configure as intância com o .env
6. Execute os testes.

```console
git clone git@github.com:JLira/todo-list.git
cd test-vibra
python -m venv .venv
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```
## Como fazer o deploy local?

1. execute o comando: docker-compose up -d 
2. Crie um superusuario: python manage.py createsuperuser
3. Suba o ambiente: python manage.py runserver
4. na barra de endeço do na nevegador digite: 
   http://127.0.0.1:8000/api/v1

Comece a usar a api


