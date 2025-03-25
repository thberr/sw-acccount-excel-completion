import openpyxl
from config import excel_cases
from utils import load_artifacts_from_json

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
        print(f"Eroor during the Excel file update : {e}")