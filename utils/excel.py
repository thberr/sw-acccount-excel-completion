import openpyxl
from config import excel_cases
from utils import load_artifacts_from_json, load_runes_from_json

def artifacts_completion(json_file_path, excel_file_path):
    try:
        wb = openpyxl.load_workbook(excel_file_path)
        sheet = wb.active

        for case in excel_cases.keys():
            value_case = 0
            for artifact in load_artifacts_from_json(json_file_path):
                if artifact.its_case(
                    stat=excel_cases[case]["stat"],
                    value_min=excel_cases[case]["value_min"],
                    type=excel_cases[case]["type"],
                    subtype=excel_cases[case]["subtype"],
                    main_stat=excel_cases[case]["main_stat"],
                ):
                    value_case += 1
            sheet[case] = value_case

        wb.save(excel_file_path)
        print(f"Excel file update successful : {excel_file_path}")

    except Exception as e:
        print(f"Error during the Excel file update : {e}")

def giant_speed_completion(json_file_path, excel_file_path):
    try:
        wb = openpyxl.load_workbook(excel_file_path)
        sheet = wb.active

        max_speed_swift = [0] * 6
        max_speed_despair = [0] * 6 

        runes_list = load_runes_from_json(json_file_path)
        for rune in runes_list:
            for sub in rune.subs.values():
                if sub['stat'] == 8:
                    rune_speed = sub['value'] + sub['grind']
                    if rune.set == 3 and max_speed_swift[rune.slot - 1] < rune_speed:
                        max_speed_swift[rune.slot - 1] = rune_speed
                    elif rune.set == 10 and max_speed_despair[rune.slot - 1] < rune_speed:
                        max_speed_despair[rune.slot - 1] = rune_speed

        sheet["BF26"] = max_speed_swift[0]
        sheet["BF27"] = max_speed_swift[2]
        sheet["BF28"] = max_speed_swift[3]
        sheet["BF29"] = max_speed_swift[4]
        sheet["BF30"] = max_speed_swift[5]

        sheet["BF35"] = max_speed_despair[0]
        sheet["BF36"] = max_speed_despair[2]
        sheet["BF37"] = max_speed_despair[3]
        sheet["BF38"] = max_speed_despair[4]
        sheet["BF39"] = max_speed_despair[5]
            
        wb.save(excel_file_path)
        print(f"Excel file update successful : {excel_file_path}")

    except Exception as e:
        print(f"Error during the Excel file update : {e}")
