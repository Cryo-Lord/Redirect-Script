from urllib.request import *
import pandas as pd
import time

try:
    file = input("Write the file route: \n")
except:
    print("File not found! \n ending script")
if (".xlsx" in file):
    data = pd.read_excel(file).values.tolist()
    experiment = pd.read_excel(file).keys()
elif (".csv" in file):
    data = pd.read_csv(file).values.tolist()
    experiment = pd.read_excel(file).keys()
else:
    raise FileNotFoundError
for row in data:
    url = row[0]
    expected_url = False if type(row[1]) != type("")  else row[1]
    open_page = urlopen(url)
    time.sleep(30)
    if expected_url:
        row[2] = "Redirected" if open_page.url == expected_url else "REDIRECTED TO UNEXPECTED URL"
    elif open_page.url == url:
        row[2] = "Not Redirected"
    else:
        row[2] = "REDIRECTED"
    print("row analyzed")
print("File analyzed, creating new file of the data obtained")
analyzed = pd.DataFrame(data, columns=experiment)
if (".xlsx" in file):
    analyzed.to_excel("./outputs/AnalyzedData.xlsx")
elif (".csv" in file):
    analyzed.to_csv("./outputs/AnalyzedData.csv")
print("File created, file sent into 'outputs' directory \n Have a nice day")