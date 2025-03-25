from utils import load_runes_from_json

def main(json_file_path, excel_file_path):
    runes = load_runes_from_json(json_file_path)

    print(runes[0])

if __name__ == "__main__":
    main(".data/Eascen-12475513.json", ".data/Account Progression Suggestion - Eascen.xlsx")