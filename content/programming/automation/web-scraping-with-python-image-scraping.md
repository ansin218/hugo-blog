---
title: "Web Scraping With Python - Image Scraping"
date: 2019-08-30T19:38:46+01:00
description: "This is a tutorial to perform web scraping with Python and beautifulsoup library. The tutorial demonstrates an example by scraping images from Wikipedia."
image: "img/thumbnails/web-scraping-spider-3.jpg"
keywords: "web scraping, image scraping, wikipedia, requests, fake_useragent, crawlers, scrapers, python, beautifulsoup"
url: "/programming/automation/web-scraping-with-python-image-scraping/"
---

In this tutorial, we will be performing web scraping with Python and beautifulsoup. We will be scraping images of all the megacities of our world as of 2016 from this link: [https://en.wikipedia.org/wiki/Megacity](https://en.wikipedia.org/wiki/Megacity)

If you scroll down the page, you should come across a table looking like this:
![alt text](/img/programming/megacities-wikipedia.png "Megacities Wikipedia")

We will be scraping the images from the *Image* column shown in the above picture. To do this, we use the [requests](http://docs.python-requests.org/en/master/) library first like shown in the following block of code:

```Python
import requests

scrapeLink = 'https://en.wikipedia.org/wiki/Megacity'
page = requests.get(scrapeLink)
```

Next, we will get the entire content of the page in HTML format using a library called [beautifulsoup4](https://pypi.org/project/beautifulsoup4/). To do so, write:

```Python
from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, 'html.parser')
```

You can notice that the entire source code of the wiki page has been stored inside this `soup` variable. From this point, knowledge of HTML can help in grasping the concept of extracting the target data easily. However, I will try to make it as clear as possible for people without HTML knowledge as well.

Head to the webpage from your browser and locate where your information is in the webpage by checking out the __Page Source__ or __Source Code__ of the webpage. On carefully going through the code, you can notice that our information is located somewhere and looks like the image below.

![alt text](/img/programming/source-code-wikipedia-article.png "Source Code Wikipedia Article")

From this, we can conclude that our information is residing inside the `<table>` tags. However, there can be multiple tables in the source code and we want to extract the table that is relevant to us. To do this, you can go back to the source code and look for `<table`. You will see the number of tables that are there on the webpage. Find out which table from the top is yours. At the time of writing this article, it is the second table which we need.

To find all the tables and get the content of the second table, we will do:

```Python
megaTable = soup.find_all('table')[1]
```

Our `megaTable` variable now has the source code of the table from which we need to extract the rank, city and country. To extract further information, let us inspect which part of this table we need to access. The code below is for the first two cities. We will however do it for all the cities.

To scrape the images, have a look at the `megaTable` variable from the page. You can find that links of the images are inside `<a>` with the name of the class being `image`. It looks like this:

```HTML
<a class="image" href="/wiki/File:Meieki_from_Heiwa_Park_Aqua_Tower.jpg"><img alt="Meieki from Heiwa Park Aqua Tower.jpg" data-file-height="3840" data-file-width="5900" height="78" src="//upload.wikimedia.org/wikipedia/commons/thumb/2/26/Meieki_from_Heiwa_Park_Aqua_Tower.jpg/120px-Meieki_from_Heiwa_Park_Aqua_Tower.jpg" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/2/26/Meieki_from_Heiwa_Park_Aqua_Tower.jpg/180px-Meieki_from_Heiwa_Park_Aqua_Tower.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/2/26/Meieki_from_Heiwa_Park_Aqua_Tower.jpg/240px-Meieki_from_Heiwa_Park_Aqua_Tower.jpg 2x" width="120"/></a>
```

From each of these `<a>` with class name `image`, we will extract the value of `href` attribute.

```Python
imgLinkList = []

for imgLink in megaTable.find_all('a', {'class': 'image'}):
    partialLink = 'https://en.wikipedia.org/' + imgLink['href']
```

Inside the above loop, we will try to create a new fake user agent every time, perform a request for the content to the link of the image, and try to get the link of the real raw image.

```Python
ua1 = UserAgent()
randomHeader = {'User-Agent': str(ua1.random)}
imgPage = requests.get(partialLink, randomHeader)
imgSoup = BeautifulSoup(imgPage.content, 'html.parser')
```

If you have followed the previous tutorial on how to find the relevant information from source code, by now you must know what to look for and how to get it. However, if you are still lost, what we are trying to do is access the above link to get the raw image link. The raw image link is residing inside a `<div>` tag with the class name `fullImageLink` inside the value from the variable `partialLink` which iterates through the links of all the megacities.

```Python
fullImgDiv = imgSoup.find_all('div', {'class': 'fullImageLink'})
```

The content inside the `fullImgDiv` looks like:

```HTML
<div class="fullImageLink" id="file"><a href="//upload.wikimedia.org/wikipedia/commons/c/c1/PalacioEjecutivodelPeru.jpg"><img alt="File:PalacioEjecutivodelPeru.jpg" data-file-height="2400" data-file-width="3600" height="533" src="//upload.wikimedia.org/wikipedia/commons/thumb/c/c1/PalacioEjecutivodelPeru.jpg/800px-PalacioEjecutivodelPeru.jpg" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/c/c1/PalacioEjecutivodelPeru.jpg/1200px-PalacioEjecutivodelPeru.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/c/c1/PalacioEjecutivodelPeru.jpg/1599px-PalacioEjecutivodelPeru.jpg 2x" width="800"/></a><div class="mw-filepage-resolutioninfo">Size of this preview: <a class="mw-thumbnail-link" href="//upload.wikimedia.org/wikipedia/commons/thumb/c/c1/PalacioEjecutivodelPeru.jpg/800px-PalacioEjecutivodelPeru.jpg">800 × 533 pixels</a>. <span class="mw-filepage-other-resolutions">Other resolutions: <a class="mw-thumbnail-link" href="//upload.wikimedia.org/wikipedia/commons/thumb/c/c1/PalacioEjecutivodelPeru.jpg/320px-PalacioEjecutivodelPeru.jpg">320 × 213 pixels</a> | <a class="mw-thumbnail-link" href="//upload.wikimedia.org/wikipedia/commons/thumb/c/c1/PalacioEjecutivodelPeru.jpg/640px-PalacioEjecutivodelPeru.jpg">640 × 427 pixels</a> | <a class="mw-thumbnail-link" href="//upload.wikimedia.org/wikipedia/commons/thumb/c/c1/PalacioEjecutivodelPeru.jpg/1024px-PalacioEjecutivodelPeru.jpg">1,024 × 683 pixels</a> | <a class="mw-thumbnail-link" href="//upload.wikimedia.org/wikipedia/commons/thumb/c/c1/PalacioEjecutivodelPeru.jpg/1280px-PalacioEjecutivodelPeru.jpg">1,280 × 853 pixels</a> | <a class="mw-thumbnail-link" href="//upload.wikimedia.org/wikipedia/commons/c/c1/PalacioEjecutivodelPeru.jpg">3,600 × 2,400 pixels</a>.</span></div></div>
```

The raw image link is inside the first `<a>` tag within the `href` attribute. We will extract this value next.

```Python
fullImgLink = fullImgDiv[0].find_all('a')[0]
```

We will add the https: value to this link and add the links to the imgLinkList that we created earlier.

```Python
fullImg = 'https:' + fullImgLink['href']
imgLinkList.append(fullImg)
```

As said earlier, the above blocks of codes must be inside the initial loop. Hence, your final block of code must look like:

```Python
for imgLink in megaTable.find_all('a', {'class': 'image'}):
    partialLink = 'https://en.wikipedia.org/' + imgLink['href']
    ua1 = UserAgent()
    randomHeader = {'User-Agent': str(ua1.random)}
    imgPage = requests.get(partialLink, randomHeader)
    imgSoup = BeautifulSoup(imgPage.content, 'html.parser')
    fullImgDiv = imgSoup.find_all('div', {'class': 'fullImageLink'})
    fullImgLink = fullImgDiv[0].find_all('a')[0]
    fullImg = 'https:' + fullImgLink['href']
    imgLinkList.append(fullImg)
```

We now have a list of the links of raw images of all the megacities. We will now scrape them using the [urllib](https://docs.python.org/3/library/urllib.html) library. We will also rename the image with the name of the city.

```Python
from urllib.request import urlopen, Request, urlretrieve
import urllib

for i in range(len(imgLinkList)):
    imgName = cityList[i] + '.jpg'
    try:
        urllib.request.urlretrieve(imgLinkList[i], imgName)
    except:
        print('Image Not Found')
```

You must now have the images of all the megacities stored inside the same folder as your scraping script. Congratulations on scraping images using Python and beautifulsoup. To learn web scraping texts with Python, head over to this article: [Web Scraping With Python - Text Scraping Wikipedia](https://www.ankuroh.com/programming/automation/web-scraping-with-python-text-scraping-wikipedia/)