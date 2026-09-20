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

## Attribution

Adapted for this portfolio from [500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects/tree/main/agents/04-sql-query-agent), created by ashishpatel26 and distributed under the MIT License. See [THIRD_PARTY_LICENSES.md](../../THIRD_PARTY_LICENSES.md).
