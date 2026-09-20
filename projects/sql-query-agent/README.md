# SQL Query Agent

Ask questions about a SQLite database in everyday language. The agent translates each question into SQL, executes it, and returns a readable answer.

## Highlights

- Natural-language-to-SQL workflow
- Built-in e-commerce demonstration database
- Read-only database access by default
- Interactive and one-question command-line modes

## Run

```bash
pip install -r requirements.txt
cp .env.example .env
python agent.py
python agent.py --question "What is total revenue by country?"
```

Use `--allow-write` only with a disposable database.

