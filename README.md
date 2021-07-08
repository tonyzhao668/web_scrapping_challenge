
# Web Scraping - Mission to Mars

By Tony Zhao 10/03/2021 

## Step 1 - Scraping done for the followings!

Complete initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter for the following urls:
Create a Jupyter Notebook file called `web_scrapping.ipynb` and use this to complete all of scraping and analysis tasks. 

### NASA Mars News

#### News Scrapping:

![News](screenshots/news.PNG)

* Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that can reference later.

#### Jupyter Notebook coding:

![Jupyter Notebook](screenshots/news_scrap.png)

### JPL Mars Space Images - Featured Image

#### Picture Scrapping:

![Perseverance](screenshots/pers.PNG)

* Visit the url for JPL Featured Space Image [here](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html).
* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable
* Make sure to find the image url to the full size `.jpg` image.
* Make sure to save a complete url string for this image.

### Mars Facts

#### Table content scrapping:

![Facts](screenshots/facts.PNG)


* Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
* Use Pandas to convert the data to a HTML table string.

### Mars Hemispheres

#### More images scrapping:

![Hemispheres 1](screenshots/hemi1.PNG)
![Hemispheres 1](screenshots/hemi2.PNG)


* Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

## Step 2 - MongoDB, Flask Application and HTML webpage done!

#### App.py and MongoDB coding:

![Flask App](screenshots/app.PNG)

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Start by converting Jupyter notebook into a Python script called `web_scrapping.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.
  * Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.

* Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

## Job done!