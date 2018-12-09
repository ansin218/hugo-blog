---
title: "Web Scraping Using Python: Image Scraping"
date: 2018-12-08T19:38:46+01:00
description: "Scraping images using urllib and beautifulsoup"
---

In the last part of the Web Scraping Using Python series, we will scrape the images of all the megacities of our world as of 2016.

To scrape the images, have a look at the `megaTable` variable again. You can find that links of the images are inside `<a>` with the name of the class being `image`. It looks like this:

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

You must now have the images of all the megacities stored inside the same folder as your scraping script. Congratulations on scraping texts and images from the web.