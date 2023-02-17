import pandas as pd
from PyPDF2 import PdfReader
import regex as re

def tinkoff_detail_parse(filename):
    reader = PdfReader(filename)
    n=len(reader.pages)
    with open("text.txt","a") as f:
        for i in range(0,n):
            text=(reader.pages[i]).extract_text()
            f.write(text)
    pattern=r"(\d+)\s(\d{2}.\d{2}.\d{4})\s(\d*)\s(\d*)\s(\d*)(.*?)(\d{10}|0|\d{12}|.?)\s?(\d{2})\s(\d{0,3}\s?\d{0,3}\s?\d{1,3},\d{2})\s(\d{0,3}\s?\d{0,3}\s?\d{1,3},\d{2})(.*?(?=\d+\s\d{2}.\d{2}.\d{4}\s\d*\s\d*\s\d*))"
    with open("text.txt","r") as f:
        text=f.read()
        result = re.findall(pattern,text,flags=re.DOTALL)
        #TODO Last row in table
        df=pd.DataFrame(result)
        df.to_excel("Result.xlsx")
    
