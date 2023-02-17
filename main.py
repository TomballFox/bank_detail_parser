import pandas as pd
from PyPDF2 import PdfReader
import regex as re

patterns={
    "tinkoff_ul1":"(\d+)\s(\d{2}.\d{2}.\d{4})\s(\d*)\s(\d*)\s(\d*)(.*?)(\d{10}|0|\d{12}|.?)\s?(\d{2})\s(\d{0,3}\s?\d{0,3}\s?\d{1,3},\d{2})\s(\d{0,3}\s?\d{0,3}\s?\d{1,3},\d{2})(.*?(?=\d+\s\d{2}.\d{2}.\d{4}\s\d*\s\d*\s\d*))",
    "vtb_fl1":"(\d{2}.\d{2}.\d{4}\s\d{2}.\d{2}.\d{2})(\d{2}.\d{2}.\d{4})\s(\d*.?\d*(?=\s.{3}))\s.{3}\s(\d*.?\d*)\s(\d*.?\d*)\s(\d)(.*?(?=\d{2}[.]\d{2}[.]\d{4}\n))",
    
}

def pick_text_from_pdf(filename):
    reader = PdfReader(filename)
    n=len(reader.pages)
    result=""
    for i in range(0,n):
            result+=(reader.pages[i]).extract_text()
    return result

def parse(filename,pattern,re_flags=re.DOTALL):
    #TODO Last Row in table
    return re.findall(pattern,pick_text_from_pdf(filename),re_flags)

def save_to_excel(data,filename):
    (pd.DataFrame(data)).to_excel(filename+".xlsx")
    
def main():
    pattern=patterns["vtb_fl1"]
    filename="VTB.pdf"
    save_to_excel(parse(filename,pattern),filename)
    
main()

