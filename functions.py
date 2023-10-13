#!/path/to/venv/bin/python
import pdfplumber
from pyzbar.pyzbar import decode
from PIL import Image


def read_pdf_content(pdf_file_path):
    pdf_content = ""

    with pdfplumber.open(pdf_file_path) as pdf:
        for page in pdf.pages:
            pdf_content += page.extract_text()
    key_values = pdf_content.strip().split('\n')
    result = {}

    for k in key_values:
        parts = k.split(':')
        key = parts[0].strip()
        value = parts[1].strip() if len(parts) > 1 else ""
        result[key] = value

    return result


def read_barcodes_from_pdf(pdf_file_path):
    barcodes = []

    with pdfplumber.open(pdf_file_path) as pdf:
        for page in pdf.pages:
            images = page.images
            for img in images:
                image = Image.open(page.to_image().original)
                barcodes.extend(decode(image))

        return barcodes


# Пример использования
# pdf_file_path = '/Users/bebe/PycharmProjects/pdf_task/test_task.pdf'
pdf_file_path = 'example.pdf'   # Укажите путь к вашему PDF-файлу

# Вывод итогового словаря
print(read_pdf_content(pdf_file_path))

# Вывод баркодов
detected_barcodes = read_barcodes_from_pdf(pdf_file_path)

for barcode in detected_barcodes:
    print(f"Barcode Type: {barcode.type}")
    print(f"Data: {barcode.data}")
