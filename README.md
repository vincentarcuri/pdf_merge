# pdf_merge
Merge front and back pages of scanned PDF files.

## Setup
1. Clone this repository.
2. Create virtual environment, activate, and install PyPdf.
```python -m venv env```
```source env/bin/activate```
```pip install pypdf```
3. Add shebang to the first line of the "pdf_merge.py" file pointing to python in virtual environment.
```#!/path/to/env/bin/python```
4. Make the script executable.
```chmod +x pdf_merge.py```
5. Alias script.
For BASH
```nano ~/.bash_profile```
For ZSH
```nano ~/.zshrc```
At the the bottom of the file add:
```alias pdf_merge="/path/to/pdf_merge.py"```
