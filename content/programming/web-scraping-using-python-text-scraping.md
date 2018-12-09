---
title: "Web Scraping Using Python: Text Scraping"
date: 2018-12-08T21:38:40+01:00
description: "Scraping text data using requests and beautifulsoup"
---

In this part of the web scraping series, we will scrape the list of megacities in our world along with their rankings and the country it belongs to. In addition, we will also scrape the relevant image of the city and store it locally in our system. Before you do this, head over to the `robots.txt` file to read through the rules once to know what Wikipedia allows or disallows.

The link from which we will scrape is a Wikipedia page: [https://en.wikipedia.org/wiki/Megacity](https://en.wikipedia.org/wiki/Megacity)

If you scroll down the page, you can come across a table looking like this:
![alt text](https://images2.imgbox.com/56/fb/1Tx9VmCM_o.png "Megacities")

Every time you request information from a website, a piece of information known as the user agent is sent from your end. Too many requests in a few seconds that is humanly not possible can help the target system know that you are requesting information through a bot. Although this is not required for this scraping task, we will see how to fake this user agent information for every request using the [fake_useragent](https://pypi.org/project/fake-useragent/) library.

```Python
from fake_useragent import UserAgent

for i in range(5):
    ua2 = UserAgent()
    print(ua2.random)
```

Each time you create a new instance of the UserAgent() you will get different values that will be passed while requesting information from a link. It is to be noted that there can be websites with advanced systems in place to detect such cases and block you despite using such libraries.

The result of the above output will looks like:

```
Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36
Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36
Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36
```

Since we will be scraping only one link, we will go ahead with the following block of code:

```Python
from fake_useragent import UserAgent

ua1 = UserAgent()
randomHeader = {'User-Agent':str(ua1.random)}
```

Now, we will mention the link to scrape. To do this, we use the [requests](http://docs.python-requests.org/en/master/) library:

```Python
import requests

scrapeLink = 'https://en.wikipedia.org/wiki/Megacity'
page = requests.get(scrapeLink, randomHeader)
```

Next, we will get the entire content of the page in HTML format using a library called [beautifulsoup4](https://pypi.org/project/beautifulsoup4/). To do so, write:

```Python
from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, 'html.parser')
```

You can notice that the entire source code of the wiki page has been stored inside this `soup` variable. From this point, knowledge of HTML can help in grasping the concept of extracting the target data easily. However, I will try to make it as clear as possible for people without HTML knowledge as well.

Head to the webpage from your browser and locate where your information is in the webpage by checking out the __Page Source__ or __Source Code__ of the webpage. On carefully going through the code, you can notice that our information is located somewhere and looks like the image below.

![alt text](https://images2.imgbox.com/bf/4c/4rv3GRRs_o.png "Source Code")

From this, we can conclude that our information is residing inside the `<table>` tags. However, there can be multiple tables in the source code and we want to extract the table that is relevant to us. To do this, you can go back to the source code and look for `<table`. You will see the number of tables that are there on the webpage. Find out which table from the top is yours. At the time of writing this article, it is the second table which we need.

To find all the tables and get the content of the second table, we will do:

```Python
megaTable = soup.find_all('table')[1]
```

Our `megaTable` variable now has the source code of the table from which we need to extract the rank, city and country. To extract further information, let us inspect which part of this table we need to access. The code below is for the first two cities. We will however do it for all the cities.

```HTML
<table class="sortable wikitable" style="horizontal_align:center; vertical_align:center; text=align:left; background:#FFFFF;">
<tbody><tr>
<th>Rank</th>
<th>Megacity</th>
<th>Image</th>
<th>Country</th>
<th>Continent</th>
<th>Population
</th></tr>
<tr>
<td>1</td>
<td><a href="/wiki/Tokyo" title="Tokyo">Tokyo</a></td>
<td><a class="image" href="/wiki/File:Skyscrapers_of_Shinjuku_2009_January.jpg"><img alt="Skyscrapers of Shinjuku 2009 January.jpg" data-file-height="1364" data-file-width="2560" height="64" src="//upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Skyscrapers_of_Shinjuku_2009_January.jpg/120px-Skyscrapers_of_Shinjuku_2009_January.jpg" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Skyscrapers_of_Shinjuku_2009_January.jpg/180px-Skyscrapers_of_Shinjuku_2009_January.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Skyscrapers_of_Shinjuku_2009_January.jpg/240px-Skyscrapers_of_Shinjuku_2009_January.jpg 2x" width="120"/></a></td>
<td><a href="/wiki/Japan" title="Japan">Japan</a></td>
<td><a href="/wiki/Asia" title="Asia">Asia</a></td>
<td>38,140,000<sup class="reference" id="cite_ref-UN_WUP_2016_6-0"><a href="#cite_note-UN_WUP_2016-6">[6]</a></sup>
</td></tr>
<tr>
<td>2</td>
<td><a href="/wiki/Shanghai" title="Shanghai">Shanghai</a></td>
<td><a class="image" href="/wiki/File:The_bund_shanghai.jpg"><img alt="The bund shanghai.jpg" data-file-height="2832" data-file-width="4256" height="81" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/f4/The_bund_shanghai.jpg/122px-The_bund_shanghai.jpg" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/f4/The_bund_shanghai.jpg/183px-The_bund_shanghai.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/f4/The_bund_shanghai.jpg/244px-The_bund_shanghai.jpg 2x" width="122"/></a></td>
<td><a href="/wiki/China" title="China">China</a></td>
<td><a href="/wiki/Asia" title="Asia">Asia</a></td>
<td>34,000,000<sup class="reference" id="cite_ref-oecd2015_7-0"><a href="#cite_note-oecd2015-7">[7]</a></sup>
</td></tr>
.
.
.
And so on
```

As you can see, all the data that we want to extract is inside the `<td>` tags. So, to extract information from here, we will create an empty list, loop through all the `<td>` tags and extract the text between the opening and closing tags:

```Python
rowValList = []

for i in range(len(megaTable.find_all('td'))):
    rowVal = megaTable.find_all('td')[i].get_text()
    rowValList.append(rowVal)
```

Our rowValList variable will look like:

```Python
['1', 'Tokyo', '', 'Japan', 'Asia', '38,140,000[6]\n', '2', 'Shanghai', '', 'China', 'Asia', '34,000,000[7]\n', .... ]
```

We now have the data that we wanted. From this list, we can write loops to extract the rank, megacity and country and put it in a dataframe to for neater display of the required information.

```Python
rankList = []
for i in range(0, len(rowValList), 6):
    rankList.append(rowValList[i])
    
cityList = []
for i in range(1, len(rowValList), 6):
    cityList.append(rowValList[i])
    
countryList = []
for i in range(3, len(rowValList), 6):
    countryList.append(rowValList[i])
```

We will create a dataframe out of this list using [pandas](https://pandas.pydata.org/):

```Python
import pandas as pd

megaDf = pd.DataFrame()
megaDf['Rank'] = rankList
megaDf['City'] = cityList
megaDf['Country'] = countryList
```

Here is a final look at our scraped data:

![alt text](https://images2.imgbox.com/8a/66/Da6eFmRl_o.png "Final Scraped Data")

In the final part of this series, we will scrape the images of all these cities and save them locally.