# Mission-to-Mars
A web application is built which will scrape new data every time when the button is clicked using python script.

## Overview of the Analysis
Webscraping is a method of gathering data from different sources quickly instead of visiting each website ourself and manually extracting the data.To extract the information from active websites we need Chrome developer tools,which identifies the html components attached to the data we want.The webscraping is automated using Beautiful Soup and Splinter,which automates the web browser and gathers the data we have identified.After extracting the data,the collected data is stored in MongoDB,which is NO SQL database.It can handle unstructures,messy data,data without relationships to other data.MongoDB uses Document model,that means data is stored in JSON data structure.Its fast and efficient.
To show off the analysitcs we will be using Web application framework called Flask.To enhance the webpage we will be using Bootstrap,a useful and easy HTML and CSS framework.

## Purpose of the Analysis
In this analysis,we would help Robin,a data analyst who wants to gather data about the mission to mars from all the websites and display it in central location without spending the time for gathering the data manually.she wants to collect the information about Mars like Mars latest news,headings,Mars table information,Images.The collected information is stored in MongoDB and the information is displayed in a web page using FLask framework.

## Resources Used
*DataSources*: https://redplanetscience.com, https://spaceimages-mars.com/, https://galaxyfacts-mars.com/, https://marshemispheres.com/ <br>
*Softwares used*: Visual Studio Code 1.56.0, Jupyter Notebook , Flask 1.1.2, Splinter 1.26.4, Web Drive Manager, Beautiful Soup, Pymongo, MongoDB 4.4.6, Mongo DB Compass,HTML,Bootstrap 3.3.7
*Language*: Python <br>

## Deliverable 1: Scrape Full-Resolution Mars Hemisphere Images and Titles
For scraping the information we need to visit the website in our browser,using Dev Tools we need to inspect the page and proper HTML elements are extracted to scrape.In order to extract the image URLS and title we need to use Splinter and Beautiful Soup tools,we need to retrieve the url image and title and add to the list and the list contains dictionary of image URLS and titles.In the module,we have already collected the mars heading,content,featured images and table information.

<img src = "https://github.com/fathi129/Surfs_up/blob/master/Screenshots/June_temps.png" width = 200><br>

## Deliverable 2: Update the Web App with Mars’s Hemisphere Images and Titles
## Deliverable 3: Add Bootstrap 3 Components 
se the Bootstrap 3 grid system (Links to an external site.) examples to update your index.html file so your website is mobile-responsive. Use the DevTools to test the responsiveness of your website.
Click on the Toggle Device Toolbar icon to open the UI that enables you to simulate responsiveness.
Choose a device to test your webpage, as shown in the following image:
Styling the "Scrape New Data" button.


Customizing the facts table.
Adding the hemisphere images as thumbnails, like the image below.
