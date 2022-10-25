import csv
import os

#Fuction that count csv rows
'''
def sum1forline(filename):
    with open(filename, "r+", encoding="utf8") as f:
        return sum(1 for line in f)
'''

#Get all hashtag_Eleicoes2022_* filename in the current directory and spit the row numbers
CSVFilenames=[]
for  path, currentDirectory, files in os.walk(r"C:\Users\User\OneDrive - Universidade de Aveiro\Desktop\UA\Tese\TwitterScraping"):
    for file in files:
        if file.startswith("hashtag_Eleicoes2022_"):
            #print(sum1forline(file))
            #print(f'{file.split(".")[0]}: {sum1forline(file)}')
            with open(file, 'r+', encoding='utf8') as f:
                print(f'{file.split(".")[0]}: {len(list(csv.reader(f)))-1}')



#C:/Users/User/.conda/envs/scraper/python.exe "c:/Users/User/OneDrive - Universidade de Aveiro/Desktop/UA/Tese/TwitterScraping/CSVRowCounter.py"