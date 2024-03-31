from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from pypdf import PdfWriter, PdfReader

def get_file_name(request_prompt: str) -> str:
    """
    Opens a file dialog for choosing PDF files.

    Parameters
    ----------
    request_prompt: str
        Title for dialog box.
    
    Returns
    -------
    str
        File path string.
    """
    filename = askopenfilename(filetypes=[("Pdf files", "*.pdf")], title=request_prompt)
    while not bool(filename):
        answer = input("No File Selected: Enter Q to quit, or ENTER to try again\n-->")
        if answer.upper() == "Q":
            exit()
        else:
            filename = askopenfilename(filetypes=[("Pdf files", "*.pdf")], title=request_prompt)
    return filename


def check_same_num_pages_and_return_length(odd_file_name: str, even_file_name: str) -> int:
    """
    Ensures both PDFs have the same number of pages.
    Quits if pages aren't the same length.

    Parameters
    ----------
    odd_file_name: str
        Front pages of PDF filepath
    even_file_name: str
        Back pages of PDF filepath
    
    Returns
    -------
    int
        Numbers of pages
    """
    odd = open(odd_file_name, "rb")
    even = open(even_file_name, "rb")
    odd_length = len(PdfReader(odd).pages)
    even_length = len(PdfReader(even).pages)
    odd.close()
    even.close()
    if odd_length != even_length:
        print("Unmatched Number of Pages...Exiting")
        exit()
    else:
        return odd_length


def merge_pdfs(odd_name: str, even_name: str, length: int) -> PdfWriter:
    """
    Alternates appending front and back PDF pages to one PdfWriter Object.

    Parameters
    ----------
    odd_name: str
        Front pages of PDF filepath
    even_name: str
        Back pages of PDF filepath
    length: int
        Number of pages in both PDFs
    
    Returns
    -------
    PdfWriter
        Merged PDF File

    """
    odd = open(odd_name, "rb")
    even = open(even_name, "rb")
    merged = PdfWriter()
    for page_no in range(length):
        merged.append(fileobj=odd, pages=(page_no, page_no+1))
        merged.append(fileobj=even, pages=(page_no, page_no+1))
    odd.close()
    even.close()
    return merged


def save_merged_file(merged_pdf: PdfWriter) -> None:
    """
    Opens file dialog to save PDF as.

    Parameters
    ----------
    merged_pdf: PdfWriter
        Merged PDF PdfWriter object
    """
    filename = asksaveasfilename(filetypes=[("Pdf files", "*.pdf")])
    while not bool(filename):
        answer = "No File Selected: Enter Q to quit, or ENTER to try again\n-->"
        if answer.upper() == "Q":
            exit()
        else:
            filename = askopenfilename()
    out = open(filename, "wb")
    merged_pdf.write(out)
    merged_pdf.close()
    out.close()
    


def main():
    Tk().withdraw()
    odd_name = get_file_name("Add Front Pages PDF")
    even_name = get_file_name("Add Back Pages PDF")

    length = check_same_num_pages_and_return_length(odd_name, even_name)
    print(length)
    merged = merge_pdfs(odd_name, even_name, length)
    save_merged_file(merged)


main()