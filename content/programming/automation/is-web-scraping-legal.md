---
title: "Is Web Scraping Legal"
date: 2019-08-28T22:38:40+01:00
description: "Is web scraping legal? This article answers this popular question and discusses what one needs to look into before scraping the web."
image: "img/web-scraping-spider.jpg"
keywords: "web scraping, legal, robots.txt, terms and conditions, crawlers, scrapers, python, beautifulsoup"
---

## Is web scraping legal? 

A lot of people I met asked me this question; some had no idea that they could be breaking some rules if they scrape blindly because they assumed web scraping is *always* legal. However, the answer to this question is: __it depends__. Web scraping is *not* legal always.

You need to go to the website you want to scrape and look at a few things before concluding if you are breaking any rule. It is to be noted that the onus and responsibility lies with the person scraping the data and not anyone else. The choice is entirely yours if you want to scrape or not, and break any rules or not. We will now go through certain things to keep in mind while performing web scraping actions. Later, you will find links to some tutorials to perform web scraping with Python.

### Terms and Conditions Section

Head to the website you want to scrape and check out their terms and conditions section. If there is anything mentioned there along the lines of something like the text below, then the onus is on you if you want to respect their conditions or not. If you do not respect this, you/your IP may be blocked, you may receive warnings and legal notices depending on __what you scraped, how you scraped, how often you scraped and what you did with the data later.__

The following has been quoted from AirBNB:
```
Prohibited Activities

use any robots, spider, crawler, scraper or other automated means or processes to access, collect data or other content from or otherwise interact with for any purpose;
```

The following has been quoted from GitHub:
```
Scraping refers to extracting data from our Website via an automated process, such as a bot or webcrawler. It does not refer to the collection of information through GitHub's API. Please see Section H for our API Terms. You may scrape the website for the following reasons:

Researchers may scrape public, non-personal information from GitHub for research purposes, only if any publications resulting from that research are open access.
Archivists may scrape GitHub for public data for archival purposes.

You may not scrape GitHub for spamming purposes, including for the purposes of selling GitHub users' personal information, such as to recruiters, headhunters, and job boards.
```

While AirBNB prevents us from scraping, GitHub allows scraping by enforcing some restrictions. If there are APIs like GitHub mentions, you must always check out the APIs to see if you can get the necessary information using it.

### Robots.txt File

Locate the `robots.txt` file to see which parts of the website you are allowed to scrape. This file is usually located at:

`https://domain-you-want-to-scrape.com/robots.txt`

You must learn how to read this file to understand what you are allowed or not allowed to scrape. Ethically, you must follow these rules and design your scraper accordingly. Here are a few examples of how to read a robots.txt file.

```Markdown
# Allow Full Access
User-agent: *
Disallow:

# Block Complete Access
User-agent: *
Disallow: /

# Allow Particular File
User-agent: *
Allow: /data.html

# Block Particular Folder
User-agent: *
Disallow: /folder/

# Crawl Only During Stipulated Time Frame
Visit-time: 0200-0600

# Request 1 Page Every 30 Seconds
Request-rate: 1/30
```

### The Grey Area

Another common question is: if the data is public, then what stops you from scraping? This is again debatable. One can employ a team of people to manually copy and save the data. However, this takes time and effort of lot of people, not to forget the money one needs to pay. Scraping is much more easier relatively. You can continue breaking the rules and get a lot of information in a really short period of time at the cost of harming the target system in place compared to a manual human effort.

There have also been cases fought by some major companies against people who scraped the former's data. Check out the links to get a bigger picture of the consequences of scraping without any knowledge. While in some cases you may get away eventually, the question remains, what are the consequences that awaits if caught?

- [LinkedIn Takes Data Scraping Fight to Ninth Circuit](https://www.courthousenews.com/linkedin-takes-data-scraping-fight-to-ninth-circuit/)

- [Microsoft ordered to let third parties scrape LinkedIn data](https://www.theverge.com/2017/8/15/16148250/microsoft-linkedin-third-party-data-access-judge-ruling)

- [OkCupid Study Reveals the Perils of Big-Data Science](https://www.wired.com/2016/05/okcupid-study-reveals-perils-big-data-science/)

- [Someone scraped 40,000 Tinder selfies to make a facial dataset for AI experiments](https://techcrunch.com/2017/04/28/someone-scraped-40000-tinder-selfies-to-make-a-facial-dataset-for-ai-experiments/)

- [Ryanair Files U.S. Lawsuit Against Expedia Over Screen-Scraping](https://skift.com/2018/02/25/ryanair-files-u-s-lawsuit-against-expedia-over-screen-scraping/)

By now, you have an idea of how the world of web scraping is, what responsibilites are on you as a data aggregator and most importantly, is web scraping legal with respect to whatever you plan to scrape. Check out the tutorials below to learn web scraping with Python. 

- [Web scraping with Python | Scraping text data using beautifulsoup library](https://ankuroh.com/programming/automation/web-scraping-using-python-text-scraping/)
- [Web scraping with Python | Scraping images using beautifulsoup librar](https://ankuroh.com/programming/automation/web-scraping-using-python-image-scraping/)