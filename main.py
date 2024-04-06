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
            
        # Output/ 폴더가 없으면 새로 생성
        if not os.path.exists(os.path.dirname(output_pdf_path)):
            os.makedirs(os.path.dirname(output_pdf_path))

        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)

# 폴더 또는 파일을 선택하는 함수
def select_file_or_directory(path):
    items = os.listdir(path) # 현재 경로의 폴더 또는 파일 목록을 가져오기    
    
    # 각 항목의 전체 경로를 생성
    items = [os.path.join(path, item) for item in items]
    items.append('..') # 상위 폴더로 이동하기 위한 항목 추가
    
    # 폴더 또는 파일을 선택하는 질문 생성
    questions = [
        inquirer.List('selected_item',
                      message="원본 PDF 파일의 탐색을 위해, 폴더나 파일을 선택하세요.",
                      choices=items),
    ]
    answers = inquirer.prompt(questions)
    selected_item = answers['selected_item']
    
    # 선택된 항목이 .pdf 파일이면 해당 파일의 경로를 반환
    if os.path.isfile(selected_item) and selected_item.endswith('.pdf'):
        return selected_item
    # 선택된 항목이 폴더이면 해당 폴더 내에서 다시 폴더 또는 파일을 선택
    else:
        return select_file_or_directory(selected_item)

if __name__ == "__main__":
    input_pdf_path = select_file_or_directory('./Input/')
    output_pdf_file = input("[?] 저장할 PDF 파일의 이름을 입력하세요: ")

    # 사용자가 입력한 파일 이름에 .pdf 확장자가 없으면 자동으로 추가
    if not output_pdf_file.endswith('.pdf'):
        output_pdf_file += '.pdf'
    
    output_pdf_path = "./Output/" + output_pdf_file

    extract_odd_pages(input_pdf_path, output_pdf_path)