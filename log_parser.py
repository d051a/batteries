import re
import json
import itertools
from datetime import datetime
from config import *


REGEX_STR = """\{\s{2}\"state\" : \"idle\"[\s\S]*?\]\s{2}\}\s{2}\]\s\}|{\s{2}\"state\" : \"duty_load\"[\s\S]*?\]\s{2}\}\s{2}\]\s\}"""


def file_read(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8', errors='ignore') as file:
            return file.read()
    except FileNotFoundError:
        print(f"No such file: '{file_name}'")


def get_log_elements(log_text):
    log_elements = re.findall(REGEX_STR, log_text, re.DOTALL)
    return log_elements


def get_mv(log_entry_data):
    data_list = log_entry_data['data']
    mv_elems_list = [data['mV'] for data in data_list]
    clean_mv = list(itertools.chain(*mv_elems_list))
    return clean_mv


def get_load(log_entry_data):
    data_list = log_entry_data['data']
    load_elems_list = [data['load'] for data in data_list]
    clean_load = list(itertools.chain(*load_elems_list))
    return clean_load


def date_time_convert(date_time):
    datetime_object = datetime.strptime(date_time,
                                        '%d.%m.%y_%H:%M:%S')
    return datetime_object


def log_data():
    log_lines = file_read(LOG_FILE_PATH)
    log_elements = get_log_elements(log_lines)
    clean_log_data = {}
    for log_entry_num, log_entry in enumerate(log_elements):
        log_entry_data = json.loads(log_entry)
        data_time = log_entry_data['date_time']
        mv = get_mv(log_entry_data)
        load = get_load(log_entry_data)
        clean_log_data[log_entry_num] = {'time': date_time_convert(data_time),
                                         'mv': mv,
                                         'load': load}
    return clean_log_data


if __name__ == '__main__':
    log_data()
