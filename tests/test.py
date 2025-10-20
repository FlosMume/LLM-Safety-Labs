import os
import sys
import pathlib
import importlib
import pytest

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = REPO_ROOT / "docs"
REQ = REPO_ROOT / "requirements.txt"
README = REPO_ROOT / "README.md"

def test_readme_exists_and_mentions_uml():
    assert README.exists(), "README.md is missing"
    txt = README.read_text(encoding="utf-8", errors="ignore")
    assert "uml" in txt.lower(), "README should reference the UML diagram"

def test_requirements_exists_and_is_nonempty():
    assert REQ.exists(), "requirements.txt is missing"
    lines = [l.strip() for l in REQ.read_text(encoding="utf-8", errors="ignore").splitlines() if l.strip() and not l.strip().startswith('#')]
    assert len(lines) > 3, "requirements.txt looks too small or empty"

def test_docs_uml_svg_is_well_formed_xml():
    svg = DOCS / "uml_overview.svg"
    assert svg.exists(), "docs/uml_overview.svg is missing"
    import xml.etree.ElementTree as ET
    ET.parse(str(svg))

@pytest.mark.parametrize("pkg", ["requests", "pandas", "numpy", "matplotlib", "python_dotenv"])
def test_core_packages_import(pkg):
    name = "dotenv" if pkg == "python_dotenv" else pkg
    importlib.import_module(name)

@pytest.mark.parametrize("modname", [
    "ai_safety_demos",
    "chatgpt_api_safety_demo",
    "additional_hallucination_tests",
    "better_hallucination_tests",
    "advanced_jailbreak_tests",
    "setup_demo",
    "demo_runner",
])
def test_demo_modules_present_or_skipped(modname):
    pyfile = REPO_ROOT / f"{modname}.py"
    if not pyfile.exists():
        pytest.skip(f"{modname}.py not present in public starter (expected)")
    sys.path.insert(0, str(REPO_ROOT))
    importlib.import_module(modname)

def test_env_file_optional_but_loadable_if_present():
    envfile = REPO_ROOT / ".env"
    if not envfile.exists():
        import pytest
        pytest.skip(".env not present (that's fine for public repo)")
    from dotenv import dotenv_values
    vals = dotenv_values(envfile)
    assert isinstance(vals, dict)