from models import Artifact
from utils import load_json

def main(json_file_path):
    artifacts_list = [] # list of all the artifacts of the account

    account = load_json(json_file_path)

    for monsters in account["unit_list"]:
        # get the artifacts equiped to a monster
        for artifact in monsters["artifacts"]:
            artifacts_list.append(Artifact.from_json(artifact))

    print(artifacts_list[0])

if __name__ == "__main__":
    main("Eascen-12475513.json")