# Amazon Web Scraper.

## Type the following command to run this:</br>
To Install Scrapy using conda, run 
```
conda install -c conda-forge scrapy
```
Alternatively, if you’re already familiar with installation of Python packages, you can install Scrapy and its dependencies from PyPI with:
```
pip install Scrapy
```
After Installation of Scrapy, run
```
scrapy crawl amzn_mob -o FILNAME.json
```
File will be saved as FILENAME.json containing mobile details in JSON Format.


eg: I have typed the command in my computer ```scrapy crawl amzn_mob -o Mobile_Data.json```
Than the file will be saved as 'Mobile_Data.json'
