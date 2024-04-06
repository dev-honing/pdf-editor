# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader, PdfWriter
import os
import inquirer

# 홀수 페이지만 추출하여 저장하는 함수
def extract_odd_pages(input_pdf_path, output_pdf_path):
    with open(input_pdf_path, 'rb') as file:
        reader = PdfReader(file)
        writer = PdfWriter()

        num_pages = len(reader.pages)  # PDF 파일의 총 페이지 수
        for page_num in range(0, num_pages, 2):  # 홀수 페이지만 추출
            writer.add_page(reader.pages[page_num])

        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)

if __name__ == "__main__":
    files = os.listdir('./Input/')
    questions = [
        inquirer.List('input_pdf_file',
                      message="추출할 PDF 파일을 선택하세요.",
                      choices=files),
        inquirer.Text('output_pdf_file', message="추출된 PDF 파일의 이름을 입력하세요.")
    ]
    answers = inquirer.prompt(questions)

    input_pdf_path = "./Input/" + answers['input_pdf_file']
    output_pdf_path = "./Output/" + answers['output_pdf_file']

    extract_odd_pages(input_pdf_path, output_pdf_path)
