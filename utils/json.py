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
        print(f"The file {json_file_path} doesn't exist.")
        return []
    except json.JSONDecodeError:
        print(f"The file {json_file_path} isn't a valid JSON.")
        return []