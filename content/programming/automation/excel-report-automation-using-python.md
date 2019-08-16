---
title: "Excel Report Automation Using Python"
date: 2018-11-29T10:11:20+01:00
description: "End-To-End Excel Report Automation Using Python"
image: "https://images2.imgbox.com/75/d8/befrNwoK_o.jpg"
---

People working as data analysts/scientists stumble upon requests for reports from different people. While ad-hoc reports are one time thing, reports that need to be sent periodically, be it daily or weekly or monthly, can take quite a lot of time if done manually. Hence, this tutorial will focus on how to automate the process of creating and sending reports periodically.

In this tutorial, I will perform an excel report automation the way as illustrated in the diagram below completely using Python.

![alt text](https://images2.imgbox.com/4d/2d/gUCkYJcB_o.png "Report Automation Pipeline")

### Query Latest Data From Oracle

Let us import the necessary libraries and establish a connection to our database with the necessary username and password. This can be done using the following block of code:

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

### Replace Latest Data Source Of Excel Report

We have the result of our query in a `pandas` dataframe currently. We will save this data to a CSV file with the name `latest_raw_data.csv`.  

```Python
file_name = 'H:/periodic-analysis/latest_raw_data.csv'
df.to_csv(file_name, sep = '|', index = False)
```

It is to be noted that this CSV file acts as the data source for the excel report. This tutorial assumes that you have already created a connection from your excel file to this raw data file.

### Copy Last Excel Report File

Imagine you have the last excel report file that you had sent X days back to someone. You will typically create a copy of this file and then do the necessary changes. We will automate this step using Python as well.

This is a two step process: get the latest file in the directory and create a copy of the latest file in the same directory.

To get the latest modified file from the directory:

```Python
import glob
import os

list_of_files = glob.glob('H:/periodic-reports/final-reports/*')
latest_file = max(list_of_files, key = os.path.getctime)
latest_file = latest_file.split('2018', 1)
latest_file = '2018' + latest_file[1]
```

To create a copy of this latest file with current date appended to the name of the file:

```Python
from shutil import copyfile
import datetime

today_date = datetime.datetime.today().strftime('%Y%m%d')
src = 'H:/periodic-reports/final-reports/' + latest_file
new_file = today_date + '_latest_periodic_report.xlsx'
dst = 'H:/periodic-reports/final-reports/' + new_file
copyfile(src, dst)
```

### Refresh Excel File

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

### Send E-Mail Notification

The report is now ready. However, there is an additional step. We want to notify the concerned people that the report is ready and is stored in XYZ shared location. In this case, the shared location is a Windows drive `H:`. This can vary depending on how the shared network at your end looks like. You can send emails using Python by writing the following block of code:

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

### Schedule Job

This is the last step of this tutorial where you will schedule the entire process until now to run, update and send the email by itself. There are many ways to schedule tasks depending on which environment you are in. However, I will demonstrate a Pythonic way using a Python library called [schedule by Dan Bader](https://github.com/dbader/schedule).

A simple block of code to schedule a job looks like:

```Python
import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at('10:30').do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at('13:15').do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

The above block of code will print, `I'm working...` every 10 minutes, one hour, every day at 10:30 AM, every Monday, and every Wednesday at 13:15 PM respectively. 

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

Save the entire code in a file and run it from a Python terminal. You have now learnt how to automate the process of generating a simple excel report completely using Python on a defined periodic basis.
