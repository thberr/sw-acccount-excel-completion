from models.rune_stat import RuneStat
from utils import calculate_eff_stat_rune_6

def main(json_file_path, excel_file_path):
    print(calculate_eff_stat_rune_6(RuneStat(4, 28, 7)))

if __name__ == "__main__":
    main(".data/Eascen-12475513.json", ".data/Account Progression Suggestion - Eascen.xlsx")