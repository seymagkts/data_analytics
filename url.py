import numpy as np 
import pandas as pd

data = pd.read_excel('devices.xlsx')

def print_url(number):
    data2= data["Stats_Access_Link"][number-1]
    data3 = data2.rstrip("</url>")
    if data3.startswith("<url>https://"):
        print(data3.strip("<url>https://"))
    elif data3.startswith("<url>http://"):
        print(data3.strip("<url>http://"))
        
entry = int(input("1. AXO145 \n2. TRU151 \n3. ZOD231 \n4. YRT326 \n5. LWR245 \nChoose Device Type: "))
print_url(entry)
