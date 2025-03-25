import json
from models import Artifact

def load_artifacts_from_json(json_file_path):
    try:
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            account = json.load(json_file)

            artifacts_list = []

            for monster in account.get("unit_list", []):
                for artifact in monster.get("artifacts", []):
                    artifacts_list.append(Artifact.from_json(artifact))

            for artifact in account.get("artifacts", []):
                artifacts_list.append(Artifact.from_json(artifact))

            return artifacts_list

    except FileNotFoundError:
        print(f"Le fichier {json_file_path} n'existe pas.")
        return []
    except json.JSONDecodeError:
        print(f"Le fichier {json_file_path} n'est pas un JSON valide.")
        return []