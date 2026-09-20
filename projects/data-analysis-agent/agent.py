"""
Data Analysis Agent using LangChain and pandas.

Loads CSV/Excel data and answers analytical questions in natural language.
Adapted from ashishpatel26/500-AI-Agents-Projects (MIT License).
"""
import argparse
import os
import random
from datetime import date, timedelta

import pandas as pd
from dotenv import load_dotenv
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI

load_dotenv()

def create_sample_data(path: str):
    random.seed(42)
    products = ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"]
    regions = ["North", "South", "East", "West"]
    start = date(2024, 1, 1)
    rows = []
    for _ in range(200):
        rows.append({
            "date": (start + timedelta(days=random.randint(0, 364))).isoformat(),
            "product": random.choice(products),
            "region": random.choice(regions),
            "quantity": random.randint(1, 20),
            "unit_price": round(random.uniform(50, 2000), 2),
        })
    df = pd.DataFrame(rows)
    df["revenue"] = df["quantity"] * df["unit_price"]
    df.to_csv(path, index=False)
    return df

def main():
    parser = argparse.ArgumentParser(description="Data Analysis Agent")
    parser.add_argument("--file", default="sample_data.csv")
    parser.add_argument("--question")
    parser.add_argument("--allow-dangerous-code", action="store_true")
    args = parser.parse_args()

    if args.file == "sample_data.csv" and not os.path.exists(args.file):
        df = create_sample_data(args.file)
    else:
        ext = os.path.splitext(args.file)[1].lower()
        df = pd.read_excel(args.file) if ext in {".xlsx", ".xls"} else pd.read_csv(args.file)

    print(f"Loaded {args.file}: {len(df)} rows x {len(df.columns)} columns")
    if not args.allow_dangerous_code:
        print("Generated Python execution is disabled. Use --allow-dangerous-code only with trusted prompts and non-sensitive data.")
        return

    agent = create_pandas_dataframe_agent(
        ChatOpenAI(model="gpt-4o", temperature=0),
        df,
        verbose=False,
        allow_dangerous_code=True,
    )
    if args.question:
        print(agent.invoke({"input": args.question})["output"])
        return
    while True:
        question = input("Question (or quit): ").strip()
        if question.lower() in {"quit", "exit", "q"}:
            break
        if question:
            print(agent.invoke({"input": question})["output"])

if __name__ == "__main__":
    main()
