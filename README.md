# LLM Safety Labs — AI Safety Demos

> Pin-ready repo showcasing AI Safety concepts: hallucination detection, jailbreak prevention, and bias checks for LLMs.

![UML](docs/uml_overview.svg)

## What this project demonstrates
- Hallucination checks and adversarial prompts
- Jailbreak defenses and a layered safety wrapper
- Basic bias/validation hooks and production-minded patterns

## Quickstart
```bash
conda create -n proj8venv python=3.10.8 -y
conda activate proj8venv
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
- `llm-safety-demos`

## 🔒 Technical Verification
This repository showcases the documented and structural components of my AI Safety project.

The complete functional implementation (including runnable demos, model wrappers,
and evaluation scripts) is available upon request.
The project has been successfully tested locally with:
- RTX 4070 SUPER GPU (CUDA 12.8)
- PyTorch 2.5 + cu121
- OpenAI API v1.0+

For verification, please refer to:
- UML diagram (`docs/uml_overview.svg`)
- Recorded execution screenshots and terminal logs in `/docs/demo_evidence/`(to be posted)
