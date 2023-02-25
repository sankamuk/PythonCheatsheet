
# Web Scrapping

*Web Scraping* is a program that request and parses any data over Web in non-traditional way.

***Important Components***

- Scraping generally means extracting data from single page.
- Crawling means moving from page to page.
- Bots manage automated interactions with Web pages.


## Scrapy

- Get scrapy

```commandline
pip install Scrapy
```

- Validate

```commandline
(scrap_venv) [root@localhost web_scrapping]# scrapy --help
/root/web_scrapping/scrap_venv/lib64/python3.6/site-packages/OpenSSL/_util.py:6: CryptographyDeprecationWarning: Python 3.6 is no longer supported by the Python core team. Therefore, support for it is deprecated in cryptography. The next release of cryptography (40.0) will be the last to support Python 3.6.
  from cryptography.hazmat.bindings.openssl.binding import Binding
Scrapy 2.6.3 - no active project

Usage:
  scrapy <command> [options] [args]

Available commands:
  bench         Run quick benchmark test
  commands
  fetch         Fetch a URL using the Scrapy downloader
  genspider     Generate new spider using pre-defined templates
  runspider     Run a self-contained spider (without creating a project)
  settings      Get settings values
  shell         Interactive scraping console
  startproject  Create new project
  version       Print Scrapy version
  view          Open URL in browser, as seen by Scrapy

  [ more ]      More commands available when run from project directory

Use "scrapy <command> -h" to see more info about a command
```

- Create a Scrapy project

```commandline
(scrap_venv) [root@localhost web_scrapping]# scrapy startproject scraping_project_01
/root/web_scrapping/scrap_venv/lib64/python3.6/site-packages/OpenSSL/_util.py:6: CryptographyDeprecationWarning: Python 3.6 is no longer supported by the Python core team. Therefore, support for it is deprecated in cryptography. The next release of cryptography (40.0) will be the last to support Python 3.6.
  from cryptography.hazmat.bindings.openssl.binding import Binding
New Scrapy project 'scraping_project_01', using template directory '/root/web_scrapping/scrap_venv/lib64/python3.6/site-packages/scrapy/templates/project', created in:
    /root/web_scrapping/scraping_project_01

You can start your first spider with:
    cd scraping_project_01
    scrapy genspider example example.com
```

> At this point you should have a new project folder created named per the project.

- Create first Spider

```commandline
(scrap_venv) [root@localhost web_scrapping]# cd scraping_project_01/scraping_project_01/spiders/
(scrap_venv) [root@localhost spiders]# ls -ltr
total 4
-rw-r--r--. 1 root root 161 Jan 31 15:53 __init__.py
(scrap_venv) [root@localhost spiders]# scrapy genspider realpython olympus.realpython.org
/root/web_scrapping/scrap_venv/lib64/python3.6/site-packages/OpenSSL/_util.py:6: CryptographyDeprecationWarning: Python 3.6 is no longer supported by the Python core team. Therefore, support for it is deprecated in cryptography. The next release of cryptography (40.0) will be the last to support Python 3.6.
  from cryptography.hazmat.bindings.openssl.binding import Binding
Created spider 'realpython' using template 'basic' in module:
  scraping_project_01.spiders.realpython
```

> You will find a new module created under spider with name ***realpython***.
> Update `start_urls` in new module with actual URL of your page.

- Update the Spider

To fetch title we need to update the `parse` function and make use of the request object to fetch content.
Below we fetch title.

```python
    start_urls = ['http://olympus.realpython.org/profiles/aphrodite']

    def parse(self, response):
        # Use response.css to fetch text from CSS
        # Use response.xpath to fetch content from XPath
        title = response.xpath("/html/body/center/h2").get()
        return {"title": title}
```

> Note how we extract XPath locator to extract segment from response. You can fetch XPath from Inspect->Element section of your browser and copy XPath option.

- Run the Spider

```commandline
(scrap_venv) [root@localhost spiders]# scrapy runspider realpython.py

...
2023-01-31 15:57:32 [scrapy.core.scraper] DEBUG: Scraped from <200 http://olympus.realpython.org/profiles/aphrodite>
{'title': '<h2>Name: Aphrodite</h2>'}
...

```

> Detail about XPath can be found in link `https://librarycarpentry.org/lc-webscraping/02-xpath/index.html`


## Crawling with Scrapy


## Scraping a Site Interaction with Scrapy and Selenium





