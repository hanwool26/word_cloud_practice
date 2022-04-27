from openpyxl import load_workbook
import re
import sys

def cleanText(readData):
    p = re.compile("[^0-9]")
    return "".join(p.findall(readData))

def extract_excel(file_path):
    text_path = 'test.txt'
    wb = load_workbook(file_path)

    ws = wb.active
    pre = ws.rows

    with open(text_path, 'w', encoding='UTF-8') as f:
        for r in ws.rows:
            f.write(f'%s\n' % (r[1].value))

    return text_path
