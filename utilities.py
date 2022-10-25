from datetime import date, timedelta
import os
from zipfile import ZipFile
import requests
import pandas as pd 

#Get the Url for Bhavcopy file for a particular date
def getUrl(current_date):
    year=current_date.year
    month=current_date.strftime("%b").upper()
    curr_date=current_date.strftime("%d%b%Y").upper()
    return f"https://archives.nseindia.com/content/historical/EQUITIES/{year}/{month}/cm{curr_date}bhav.csv.zip"


#To get the latest Bhavcopy files for the last 30 days (whose data is accessible)
def makeBhavCopies(path):
    new_folder=os.path.join(path, "Bhavcopies")
    try:
        os.mkdir(new_folder)
    except:
        pass
    os.chdir(new_folder)
    gap=0
    current_date=date.today()
    i=1
    data_dates=[]
    while i<=30:
        dt=current_date-timedelta(days=gap)
        print(dt)
        print(i)
        try:
            url=getUrl(dt)
            response=requests.get(url, timeout=2)   #If no http response within 2s, it timeouts
            data_dates.append(dt)
            file_name=f"bhavcopy{i}.zip"
            open(os.path.join(os.getcwd(), file_name), "wb").write(response.content)
            with ZipFile(os.path.join(os.getcwd(), file_name), 'r') as zip:
                ls=list(zip.infolist())[0].filename
                old_path=os.path.join(os.getcwd(), ls)
                new_name=f"bhavcopy{i}.csv"
                zip.extract(ls)
                new_path=os.path.join(os.getcwd(), new_name)
                os.rename(old_path, new_path)
            os.remove(os.path.join(os.getcwd(), file_name))
            i+=1
        except:
            pass
        gap+=1
    print("Data Used for 30 days is for the following dates:")
    print(data_dates)
    os.chdir(path)
    return data_dates

def latest_BhavCopy():
    return os.path.join("Bhavcopies", "bhavcopy1.csv")


            
    