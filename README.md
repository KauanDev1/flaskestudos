# flaskestudos

Repositório de estudos pessoais focado em **Flask** e desenvolvimento web. A ideia aqui é ir aprendendo na prática: rotas, templates, ORM, migrations, formulários, e o que mais aparecer pelo caminho.

## Stack

- **Python 3** + **Flask 3**
- **Flask-SQLAlchemy** (ORM)
- **Flask-Migrate** / Alembic (versionamento do banco)
- **SQLite** (banco local, fica em `instance/`)
- **Jinja2** para os templates
- HTML/CSS no front (sem framework por enquanto)

## Estrutura do projeto

```
flaskestudos/
├── app/
│   ├── __init__.py      # cria o app Flask, configura db e migrate
│   ├── views.py         # rotas
│   ├── models.py        # modelos do SQLAlchemy
│   ├── form.py          # (futuro) formulários
│   ├── templates/       # HTMLs renderizados pelo Jinja
│   └── static/          # css, imagens, js
├── migrations/          # migrations geradas pelo Flask-Migrate
├── instance/            # database.db (gerado, não vai pro git)
├── main.py              # ponto de entrada (roda o app em modo debug)
└── .gitignore
```

## Como rodar

1. Clonar o repo e entrar na pasta:
   ```bash
   git clone <url> flaskestudos
   cd flaskestudos
   ```

2. Criar e ativar a venv:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Instalar as dependências:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Migrate
   ```

4. Aplicar as migrations (cria o `database.db` em `instance/`):
   ```bash
   flask --app main db upgrade
   ```

5. Rodar o servidor de desenvolvimento:
   ```bash
   python main.py
   ```

   App sobe em `http://127.0.0.1:5000`.

## Rotas atuais

| Método | Rota     | O que faz                                   |
|--------|----------|---------------------------------------------|
| GET    | `/`      | Homepage, renderiza `index.html`            |
| GET    | `/nova/` | Página simples retornando texto             |

## Models

- **Contato** — id, data_envio, nome, email, assunto, mensagem. Pensado pra alimentar um formulário de contato mais pra frente.

## Trabalhando com migrations

Sempre que mudar um model:
```bash
flask --app main db migrate -m "descrição da mudança"
flask --app main db upgrade
```

## Roadmap de estudo

- [x] Setup do Flask com factory básica
- [x] SQLAlchemy + Migrate funcionando
- [ ] Implementar o form de contato (`form.py` + WTForms)
- [ ] Persistir submissões na tabela `Contato`
- [ ] Página de listagem dos contatos
- [ ] Autenticação simples (login/logout)
- [ ] Deploy em algum lugar (Render / Fly.io)

---

Projeto pessoal — bagunça controlada, foco em aprender. 🛠️
