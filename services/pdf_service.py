import fitz

def parse_pdf(pdf_file):
    pdf_content = fitz.open('pdf', pdf_file)
    whole_content = ""

    if pdf_content.page_count > 0:
        for page in range(0,pdf_content.page_count):
            current_page_content = pdf_content[page]
            whole_content += "\n"+current_page_content.get_text()
    
    return whole_content
