import unittest
from functions import read_barcodes_from_pdf, read_pdf_content


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # Здесь можно указать путь к вашему PDF-файлу
        # self.file_path = '/Users/bebe/PycharmProjects/pdf_task/test_task.pdf'
        self.file_path = 'example.pdf'

    def test_pdf_content(self):
        pdf_content = read_pdf_content(self.file_path)
        pdf_barcodes = read_barcodes_from_pdf(self.file_path)

        # Добавьте утверждения (assertions) для проверки результата
        self.assertIsNotNone(pdf_content, pdf_barcodes)
        self.assertIsInstance(pdf_content, dict)


if __name__ == '__main__':
    unittest.main()
