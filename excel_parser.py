from config import *
from openpyxl import load_workbook


def read_excel_file(file_name):
    workbook = load_workbook(filename=file_name)
    return workbook


def get_calculated_ma_cell_num(ma_value,
                               workbook=read_excel_file(MAS_FILE_PATH)):
    sheet_ranges = workbook.active
    for row in sheet_ranges[EXCEL_IRTH_COLUMN_INDEX]:
        if str(row.value) == str(ma_value):
            return row.coordinate


def get_clean_num_from_cell_coordinate(cell_coordinate):
    cell_values = list(cell_coordinate)
    cell_num = ''.join(
        [value for value in cell_values if str(value).isdigit()])
    return int(cell_num)


def get_measured_ma_by_calculated_ma_cell_num(cell_num,
                                              workbook=read_excel_file(
                                                  MAS_FILE_PATH)):
    work_cheet = workbook.active
    field_num = EXCEL_MA_MEASURED_COLUMN_INDEX + str(cell_num)
    measured_ma_cell_coordinate = work_cheet[field_num]
    measured_ma_value = measured_ma_cell_coordinate.value
    return measured_ma_value


def get_measured_ma():
    calculated_ma_cell_coordinate = get_calculated_ma_cell_num(IRTH_PARAM)
    calculated_ma_cell_num = get_clean_num_from_cell_coordinate(
        calculated_ma_cell_coordinate)
    measured_ma = get_measured_ma_by_calculated_ma_cell_num(
        calculated_ma_cell_num)
    return measured_ma


if __name__ == '__main__':
    get_measured_ma()
