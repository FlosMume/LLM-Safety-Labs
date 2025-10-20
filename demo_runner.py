import subprocess, sys
for s in ['setup_demo.py','ai_safety_demos.py','chatgpt_api_safety_demo.py','additional_hallucination_tests.py','better_hallucination_tests.py','advanced_jailbreak_tests.py']:
 print(f'Running {s}'); subprocess.run([sys.executable, s])
