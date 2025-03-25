from models import Artifact
from utils import load_artifacts_from_json

def main(json_file_path):

    artifacts = load_artifacts_from_json(json_file_path)
    print(artifacts[0])


if __name__ == "__main__":
    main(".data/Eascen-12475513.json")