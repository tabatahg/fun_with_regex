from openpyxl import Workbook
import re
from utils import isNumberRegex

#("(1,1)",1,225,0)	10159	2018-10-29 20:37:31.373861	2018-11-22 19:14:29	\N

wb = Workbook()

dest_filename = 'objects_loc_count_cache_converted.xlsx'

ws = wb.active
ws.title = "objects_loc_count_cache"


def open_file(file_path):
    with open(file_path, "r") as file:
        for index, line in enumerate(file):
            row_index = index
            words = line.split()
            for index2, word in enumerate(words):
                column_index = index2
                converted_word = isNumberRegex(word)
                cellref = ws.cell(row=row_index + 1, column=column_index + 1)
                cellref.value = converted_word
    wb.save(dest_filename)
    print("insertion complete")


if __name__ == "__main__":
    open_file(input("Put file path here:"))
