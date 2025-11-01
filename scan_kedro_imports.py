import os
import re

# Dossier racine de ton projet Kedro
PROJECT_ROOT = "src/purchase_predict_reloaded"

# Mapping des anciens noms vers les nouveaux
replacements = {
    r"from kedro\.io import AbstractDataSet": "from kedro.io.core import AbstractDataSet",
    r"from kedro\.io import CSVDataSet": "from kedro.io.core import CSVDataSet",
    r"from kedro\.io import MemoryDataset": "from kedro.io.core import MemoryDataSet",
}

# Extensions à scanner
EXTENSIONS = (".py", ".ipynb")  # si tu veux inclure les notebooks


def scan_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    issues = []
    for old, new in replacements.items():
        if re.search(old, content):
            issues.append((old, new))
    return issues


def scan_project(root_dir):
    results = {}
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".py"):
                file_path = os.path.join(dirpath, filename)
                issues = scan_file(file_path)
                if issues:
                    results[file_path] = issues
    return results


if __name__ == "__main__":
    results = scan_project(PROJECT_ROOT)
    if not results:
        print("Aucun import Kedro.io à corriger trouvé !")
    else:
        print("Fichiers à corriger :\n")
        for file_path, issues in results.items():
            print(f"{file_path}:")
            for old, new in issues:
                print(f"  - Remplacer '{old}' par '{new}'")
        print("\n✅ Passe maintenant en revue ces fichiers et applique les changements.")
