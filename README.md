# LLM Safety Labs — Week 8 (AI Safety Demos)

> Pin-ready, job-facing repo showcasing AI Safety concepts: hallucination detection, jailbreak prevention, and bias checks for LLMs.

![UML](docs/uml_overview.svg)

## What this project demonstrates
- Hallucination checks and adversarial prompts
- Jailbreak defenses and a layered safety wrapper
- Basic bias/validation hooks and production-minded patterns

## Quickstart
```bash
conda create -n mod8venv python=3.10.8 -y
conda activate mod8venv
pip install --upgrade pip wheel setuptools
pip install -r requirements.txt
python -m ipykernel install --user --name mod8venv --display-name "Python (mod8venv)"
```
Create a `.env` file with `OPENAI_API_KEY=...`

## Example commands
```bash
python ai_safety_demos.py
python chatgpt_api_safety_demo.py
python additional_hallucination_tests.py
python better_hallucination_tests.py
python advanced_jailbreak_tests.py
```

## Suggested repo names
- `llm-safety-labs`
- `module8-llm-safety-demos`
