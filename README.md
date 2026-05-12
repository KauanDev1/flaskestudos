# flaskestudos

Repositório de estudos pessoais focado em **Flask** e desenvolvimento web. A ideia aqui é ir aprendendo na prática: rotas, templates, ORM, migrations, formulários, e o que mais aparecer pelo caminho.

> Este README funciona como um **mapa mental** do meu aprendizado: serve pra fixar o que já estudei, conectar os conceitos e ter um lugar único pra consultar quando esquecer como uma peça encaixa na outra. Vai crescendo junto comigo.

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

## Conceitos-chave (mapa mental)

Anotações só do que **já está no projeto**. Cresce conforme o código cresce.

### Flask app (`app/__init__.py`)
- `app = Flask(__name__)` cria a instância do Flask. O `__name__` ajuda o Flask a localizar templates e arquivos estáticos.
- `app.config['SQLALCHEMY_DATABASE_URI']` aponta o ORM pro banco. Aqui é `sqlite:///database.db` — o SQLite vira um arquivo dentro de `instance/`.
- `db = SQLAlchemy(app)` "pluga" o SQLAlchemy no app — é por esse `db` que os models e queries passam.
- `migrate = Migrate(app, db)` conecta o Flask-Migrate (Alembic) no app + db, habilitando os comandos `flask db ...`.
- Os imports de `views` e `models` ficam **no final do arquivo** de propósito: evita import circular, já que ambos importam de `app`.

### Rotas e views (`app/views.py`)
- Cada `@app.route('/...')` registra uma URL e amarra ela numa função (a *view*).
- A view retorna **o corpo da resposta**: pode ser uma string (como `/nova/`) ou um template renderizado (como `/`).
- `render_template('index.html', usuario=usuario)` carrega o HTML de `templates/` e passa variáveis pro Jinja.
- `url_for('homepage')` (já importado) gera a URL pelo **nome da função view**, não pela string — se a rota mudar, os links não quebram.

### Models — SQLAlchemy (`app/models.py`)
- **ORM**: em vez de escrever SQL, defino classes Python e o ORM traduz pra tabelas.
- Classe `Contato(db.Model)` → tabela `contato`. Cada `db.Column(...)` → uma coluna.
- `primary_key=True` define a chave primária; `nullable=True` permite valor vazio.
- `default=datetime.utcnow()` preenche `data_envio` automaticamente.
  - ⚠️ Detalhe: do jeito que está (`utcnow()` **com** parênteses), o valor é calculado **uma vez quando o app sobe** e fica congelado. Pra rodar a cada insert, o correto é passar a função **sem chamar**: `default=datetime.utcnow`.

### Migrations (Flask-Migrate)
- Migration = "diff versionado" do schema. Permite evoluir tabelas sem perder dados.
- Fluxo que uso:
  1. `flask --app main db migrate -m "..."` — gera um script comparando os models com o banco atual.
  2. `flask --app main db upgrade` — aplica o script no banco.
- Os scripts gerados ficam em `migrations/versions/` e vale **dar uma olhada antes** de aplicar (autogen às vezes vira rename em drop+create).

### Templates (Jinja2) — pasta `templates/`
- Separa lógica (Python) de apresentação (HTML).
- Variáveis vindas da view aparecem com `{{ usuario }}`.
- Controle de fluxo: `{% if %}`, `{% for %}`, `{% block %}`.

### Estáticos — pasta `static/`
- CSS, imagens e JS ficam aqui. No template, referenciar com `url_for('static', filename='style.css')` (não hardcodar caminho).

### Ponto de entrada (`main.py`)
- Roda o app em modo debug pra desenvolvimento. O `--app main` dos comandos `flask` aponta pra esse arquivo.

### Como as peças se conectam

```
navegador ──HTTP──> Flask ──> view (views.py)
                                 │
                                 ├──> model (models.py) ──> SQLAlchemy ──> SQLite (instance/database.db)
                                 │
                                 └──> template (Jinja2 em templates/) ──> HTML ──> resposta
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
