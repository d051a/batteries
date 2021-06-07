import os

LOG_FILE_NAME = '27042021_LUS_20.log'
IRTH_PARAM = 180

EXCEL_IRTH_COLUMN_INDEX = 'A'
EXCEL_MA_CALCULATED_COLUMN_INDEX = 'B'
EXCEL_MA_MEASURED_COLUMN_INDEX = 'C'

WORK_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(WORK_DIR, "data")
LOGS_DIR = os.path.join(WORK_DIR, "logs")
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE_NAME)
MANUFACTURERS_FILE_PATH = os.path.join(DATA_DIR, "manufacturers.txt")
MAS_FILE_PATH = os.path.join(DATA_DIR, 'mAs.xlsx')
