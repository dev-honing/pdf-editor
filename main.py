# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader, PdfWriter

# 홀수 페이지만 추출하여 저장하는 함수
def extract_odd_pages(input_pdf_path, output_pdf_path):
    with open(input_pdf_path, 'rb') as file:
        reader = PdfReader(file)
        writer = PdfWriter()

        num_pages = len(reader.pages)
        for page_num in range(0, num_pages, 2):  # 0부터 시작하여 홀수 페이지만 추출
            writer.add_page(reader.pages[page_num])

        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)

if __name__ == "__main__":
    input_pdf_path = "S25C-0i24032117380.pdf"  # fixme: 추출할 pdf 파일 경로
    output_pdf_path = "./extracted_odd.pdf"  # fixme: 저장할 pdf 파일 경로
    extract_odd_pages(input_pdf_path, output_pdf_path)
