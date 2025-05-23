# Book Manager Project

Este projeto é um gerenciador de livros simples construído com Django. Ele fornece uma interface web para adicionar, listar e remover livros de uma biblioteca pessoal, e inclui uma API RESTful para interação com os dados. O frontend utiliza Tailwind CSS para a estilização.

## Funcionalidades

* **Adicionar Livros:** Adicione novos livros à sua biblioteca por meio de um formulário web intuitivo.
* **Listar Livros:** Visualize toda a sua coleção de livros, com opção de busca por título ou autor.
* **Remover Livros:** Exclua livros da sua biblioteca usando o ISBN.
* **API RESTful:** Acesse e gerencie seus dados de livros programaticamente usando requisições GET, POST e DELETE.

## Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Django:** Framework web de alto nível para desenvolvimento rápido.
* **Django REST framework:** Framework para construção de APIs RESTful com Django.
* **SQLite:** Banco de dados leve para armazenamento de dados.
* **Tailwind CSS:** Framework CSS para estilização da interface.
* **JavaScript (Frontend):** Script do lado do cliente para elementos interativos.

## Instalação

1. **Pré-requisitos:** Certifique-se de que o Python 3.12 ou superior está instalado. É recomendável usar um ambiente virtual para isolar as dependências do projeto.

2. **Clonar o Repositório:**

```bash
git clone <URL_DO_REPOSITORIO>
cd book-manager-project
```

3. **Criar Ambiente Virtual:**

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

4. **Instalar Dependências:**

```bash
pip install -r requirements.txt
```

5. **Migrar Banco de Dados:**

```bash
python manage.py migrate
```

6. **Executar Servidor de Desenvolvimento:**

```bash
python manage.py runserver
```

## Como Usar

Após iniciar o servidor de desenvolvimento, acesse a interface web em `http://127.0.0.1:8000/`. Adicione livros preenchendo o formulário e enviando os dados.

A API RESTful está disponível em:

* **GET /api/books/:** Retorna uma lista de todos os livros. Use `?search=<termo>` para buscar por título ou autor.
* **POST /api/books/:** Cria um novo livro. Requer um payload JSON com os campos `title`, `author`, `isbn` e `year`.
* **DELETE /api/books/<isbn>/:** Exclui um livro identificado pelo ISBN.

## Estrutura do Projeto

O projeto segue a estrutura padrão do Django:

* `book_manager_project/`: Diretório principal do projeto.
* `book_manager_project/asgi.py`: Ponto de entrada ASGI.
* `book_manager_project/settings.py`: Configurações do projeto.
* `book_manager_project/urls.py`: Rotas principais.
* `book_manager_project/wsgi.py`: Ponto de entrada WSGI.
* `library/`: Aplicação Django com a lógica de gerenciamento de livros.

  * `library/admin.py`: Registro da interface administrativa.
  * `library/apps.py`: Configuração da aplicação.
  * `library/models.py`: Modelos de banco de dados.
  * `library/tests.py`: Casos de teste.
  * `library/views.py`: Views da API.
  * `library/urls.py`: Rotas da aplicação.
  * `library/templates/library/book_management.html`: Template da interface.


