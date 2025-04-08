from poppler import load_from_file


def load_pdf(pdf_path="test.pdf"):
    pdf_document = load_from_file("test.pdf")
    num_pages = pdf_document.pages
    for page_no in range(num_pages):
        page_1 = pdf_document.create_page(page_no)
        page_1_text = page_1.text()
        print(page_1_text)


load_pdf()
