from pandas import read_excel

path = ""


def get_test_data(sheet: str, id_test: str):
    file = read_excel(path, sheet_name=sheet)
    test_data = file[file['id_test'] == id_test].to_dict(orient="records")
    return test_data[0] if test_data else None
