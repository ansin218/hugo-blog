---
title: "Automate Excel Reports Using Python"
date: 2019-08-21T10:11:20+01:00
description: "This tutorial shows how to automate excel reports using Python. It shows how to automate the task from getting the data to refreshing the Excel report."
image: "img/thumbnails/excel-report-1.jpg"
url: "/programming/automation/excel-report-automation-using-python/"
---

People working as data analysts/scientists stumble upon requests for reports from different people. While ad-hoc reports are one time thing, reports that need to be sent periodically, be it daily or weekly or monthly, can take quite a lot of time if done manually. Hence, nn this tutorial, I will show how to automate excel reports using Python. The diagram below illustrates a typical excel report automation workflow.

![alt text](/img/programming/excel-report-automation-pipeline.png "Report Automation Pipeline")

## Get Data From Oracle Using Python

Let us import the necessary libraries and establish a connection to our database with the necessary username and password. This can be done using the following block of code in the case of Oracle database.:

```Python
import cx_Oracle

host = 'your-host-name'
port = 'your-port-number-as-integer-without-quotes'
sid = 'your-sid'
tns = cx_Oracle.makedsn(host, port, sid)
db = cx_Oracle.connect('your-username', 'your-password', tns)
```

Now that we have established a connection with the database, we will run the query using the `pandas` library from a file and save it as a CSV file.

```Python
import pandas as pd
from pathlib import Path

query = Path('H:/periodic-analysis/analysis-query.sql').read_text()
df = pd.read_sql(query, db)
```

If you have CSV or Excel file with your data already, you can also directly do:

```Python
import pandas as pd

df = pd.read_csv('path/file.csv')

## or

df = pd.read_excel('path/file.xlsx')
```

## Replace Latest Data Source Of Excel Report

We have the data from our query or CSV/Excel file in a `pandas` dataframe currently. We will save this data to a CSV file with the name `latest_raw_data.csv`.  

```Python
file_name = 'H:/periodic-analysis/latest_raw_data.csv'
df.to_csv(file_name, sep = '|', index = False)
```

It is to be noted that this CSV file acts as the data source for the excel report. This tutorial assumes that you have already created a connection from your excel file to this raw data file.

## Copy Last Excel Report File

Imagine you have the last excel report file that you had sent X days back to someone. You will typically create a copy of this file and then do the necessary changes. We will automate this step using Python as well.

This is a two step process: get the latest file in the directory and create a copy of the latest file in the same directory.

### Get Latest File From Folder Using Python:

```Python
import glob
import os

list_of_files = glob.glob('H:/periodic-reports/final-reports/*')
latest_file = max(list_of_files, key = os.path.getctime)
latest_file = latest_file.split('2018', 1)
latest_file = '2018' + latest_file[1]
```

### Create Copy Of Latest File Using Python:

```Python
from shutil import copyfile
import datetime

today_date = datetime.datetime.today().strftime('%Y%m%d')
src = 'H:/periodic-reports/final-reports/' + latest_file
new_file = today_date + '_latest_periodic_report.xlsx'
dst = 'H:/periodic-reports/final-reports/' + new_file
copyfile(src, dst)
```

## Refresh Excel File Using Python

Let us assume you already had a report being sent often that is computed out of this raw CSV data file that we have generated earlier. Many people I have met think, at this step, they must open Excel, click the refresh button, and save the file. What if I tell you that even this step can be automated?

Let us the take the new file we created out of the old file and refresh it using Python itself.

```Python
import win32com.client
import time

SourcePathName = 'H:/periodic-reports/final-reports/' + new_file
Application = win32com.client.DispatchEx('Excel.Application')
Application.DisplayAlerts = False
Application.Visible = 1
Workbook = Application.Workbooks.open(SourcePathName)
Workbook.RefreshAll()
time.sleep(20)
Workbook.Save()
Workbook.Close()
Application.Quit()
```

## Send E-Mail Using Python

The report is now ready. However, there is an additional step. We may want to notify the concerned people that the report is ready and is stored in XYZ shared location. In this case, the shared location is a Windows drive `H:`. This can vary depending on how the shared network at your end looks like. You can send emails using Python by writing the following block of code:

```Python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = 'from@whatever.com'
toaddr = 'to@whatever.com'
body = 'The ABC analysis report has been updated and saved in XYZ location'

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Periodic Analysis Report'
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp-name', 'port-number-without-quotes')
server.starttls()
server.login(fromaddr, 'password')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
```

## Schedule Job Using Python

This can be considered the last step of this tutorial where you will schedule the entire process until now to run, update and send the email by itself. There are many ways to schedule tasks depending on which environment you are in. However, I will demonstrate a Pythonic way to schedule tasks using a Python library called [schedule by Dan Bader](https://github.com/dbader/schedule).

Let us now assume that we need to send our Excel report every Monday at 12 PM. The block of code will look like:

```Python
import schedule
import time

def generate_weekly_report():
    # The block of code from querying until sending email notification

schedule.every().monday.at('12:00').do(generate_weekly_report)

while True:
    schedule.run_pending()
    time.sleep(1)
```

Save the entire code in a file and run it from a Python terminal. You have now learnt how to refresh an Excel report by automating it using Python.