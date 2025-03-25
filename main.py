from utils import load_runes_from_json, giant_speed_completion

def main(json_file_path, excel_file_path):
    giant_speed_completion(json_file_path, excel_file_path)

if __name__ == "__main__":
    main(".data/Eascen-12475513.json", ".data/Account Progression Suggestion - Eascen.xlsx")