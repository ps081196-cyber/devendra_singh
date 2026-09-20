# Data Analysis Agent

Load a CSV or Excel workbook and ask analytical questions in natural language. The project combines pandas with an LLM-powered analysis agent.

## Highlights

- CSV and Excel support
- Automatic sample sales dataset
- Interactive or one-question CLI
- Revenue, product, region, trend, and correlation analysis
- Explicit safety control for model-generated Python

## Run

```bash
pip install -r requirements.txt
cp .env.example .env
python agent.py --allow-dangerous-code
python agent.py --file sales.xlsx --question "What is the monthly revenue trend?" --allow-dangerous-code
```

Only enable generated-code execution for trusted prompts and non-sensitive data.

