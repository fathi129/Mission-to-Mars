# Mission-to-Mars
A web application is built which will scrape new data whenever the button is clicked using python script.

## Overview of the Analysis
Web scraping is a method of gathering data from different sources quickly instead of visiting each website ourselves and manually extracting the data. To extract the information from active websites, we need Chrome developer tools, which identify the Html components attached to the data we want. The web scraping is automated using Beautiful Soup and Splinter, which automates the web browser and gathers the information we have identified. After extracting the data, the collected data is stored in MongoDB, which is a NO SQL database. It can handle unstructured, messy data without relationships to other data.MongoDB uses the Document model, which means data is stored in JSON data structure. Its fast and efficient. To show off the analytics, we will be using a Web application framework called Flask. We will be using Bootstrap to enhance the web page, a valuable and easy HTML and CSS framework.

## Purpose of the Analysis
In this analysis, we would help Robin, a data analyst who wants to gather data about the mission to mars from all the websites and display it in a central location without spending the time gathering the data manually. She wants to collect the latest news about Mars-like Mars, headings, Mars table information, and images. The collected information is stored in MongoDB, and the information is displayed on a web page using the FLask framework.

## Resources Used
*DataSources*: https://redplanetscience.com, https://spaceimages-mars.com/, https://galaxyfacts-mars.com/, https://marshemispheres.com/ <br>
*Software used*: Visual Studio Code 1.56.0, Jupyter Notebook, Flask 1.1.2, Splinter 1.26.4, Web Drive Manager, Beautiful Soup, Pymongo, MongoDB 4.4.6, Mongo DB Compass, HTML, Bootstrap 3.3.7
*Language*: Python. <br>

## Deliverable 1: Scrape Full-Resolution Mars Hemisphere Images and Titles

For scraping the information, we need to visit the website in our browser; using Dev Tools, we need to inspect the page, and proper HTML elements are extracted to scrape. To extract the image URLs and titles, we need to use Splinter and Beautiful Soup tools, we need to retrieve the URL image and title and add them to the list, and the list contains a dictionary of image URLs and titles. In the module, we have already collected the mars heading, content, featured images, and table information from different websites, which are mentioned below.
|   ***Mars Title and Paragraph***   | ***Mars Featured Images***   |***Mars Facts***   |
|  ----------------------------------|  -----------------------------| ------------------------------------------------------------|
|  <img src = "https://github.com/fathi129/Mission-to-Mars/blob/master/Screenshots%20for%20Mission%20to%20mars/nasatitle.png" width = 350><br >   | <img src = "https://github.com/fathi129/Mission-to-Mars/blob/master/Screenshots%20for%20Mission%20to%20mars/nasaimg.png" width = 350><br> |<img src = "https://github.com/fathi129/Mission-to-Mars/blob/master/Screenshots%20for%20Mission%20to%20mars/mars_facts.png" width = 350><br > | <br>

The mission to Mars, our web page looks like this with the collected information.<br>
<img src = "https://github.com/fathi129/Mission-to-Mars/blob/master/Screenshots%20for%20Mission%20to%20mars/deliverable%201.png" width = 350><br > 
The collected image URLs and title list looks like this. <br>
 <img src = "https://github.com/fathi129/Mission-to-Mars/blob/master/Screenshots%20for%20Mission%20to%20mars/hemisphere_urls.png" width = 700><br >
We collected the images and titles from the source website and stored them on our web page.
              
## Deliverable 2: Update the Web App with Mars’s Hemisphere Images and Titles

UUsing the Python and HTML skills, we will add the code we created previously in our scraping.py file, update our Mongo database, and modify our index.html file, so the webpage contains all the information we collected in the module, as well as the full-resolution image and title for each hemisphere image. The def scrape_all() function in our scraping.py file created a new dictionary in the data dictionary to hold a list of dictionaries with the URL string and title of each hemisphere image. A function will scrape the hemisphere data using our code from deliverable 1. At the end of the function, return the scraped data as a list of dictionaries with each hemisphere image's URL string and title. Run the app.py file in VScode, and check our Mongo database to ensure all the data are retrieved and stored.<br>

<img src = "https://github.com/fathi129/Mission-to-Mars/blob/master/Screenshots%20for%20Mission%20to%20mars/scrapingcode.png" width = 500><br >
<img src = "https://github.com/fathi129/Mission-to-Mars/blob/master/Screenshots%20for%20Mission%20to%20mars/mongodb.png" width = 500><br >
We need to modify the index.html file to access our database and retrieve the image URL and title as we loop through the dictionary in the database. We collected the images and titles from the source website and stored on our web page.<br>

|   ***Mars Hemisphere Source WebPage***   | ***Mars Hemispheres***     |
|  ----------------------------------|  ----------------------------- | 
|  <img src = "https://github.com/fathi129/Mission-to-Mars/blob/master/Screenshots%20for%20Mission%20to%20mars/mars_hemp.png" width = 350><br >   | <img src = "https://github.com/fathi129/Mission-to-Mars/blob/master/Screenshots%20for%20Mission%20to%20mars/MarsHemisphere.png" width = 350><br> | <br>

The final web page looks like this.<br> 
<img src = "https://github.com/fathi129/Mission-to-Mars/blob/master/Screenshots%20for%20Mission%20to%20mars/Fullpage.png" width = 600><br> 

## Deliverable 3: Add Bootstrap 3 Components 

When we check the web page using our Bootstrap 3 grid system, the web page is mobile-responsive. Using dev tools, the website's responsiveness is checked; Clicked on the Toggle Device Toolbar icon to open the UI that enables us to simulate responsiveness. Choosen various mobile devices to test the webpage, as shown in the following image:<br>
<img src = "https://github.com/fathi129/Mission-to-Mars/blob/master/Screenshots%20for%20Mission%20to%20mars/Bootsrap_Responsiveness.png" width = 600><br> 
For further adding bootstrap components to the web page, used the following:
- Changed the color of Scrape New Data button to red color.Changed the background color of the container and jumbotron class. 
<img src = "https://github.com/fathi129/Mission-to-Mars/blob/master/Screenshots%20for%20Mission%20to%20mars/background.png" width = 600><br> 
- The tooltip has been added under the button, giving us information about what we must do. Added the page header class, which provides a horizontal line for the text.<br>
<img src = "https://github.com/fathi129/Mission-to-Mars/blob/master/Screenshots%20for%20Mission%20to%20mars/button.png" width = 700><br> 
<img src = "https://github.com/fathi129/Mission-to-Mars/blob/master/Screenshots%20for%20Mission%20to%20mars/bootstrap_Tooltip.png" width = 600><br> 

- Added alert success class with alert dismissible feature which allows us to close the box. Enhanced the features of the table by adding the classes table-striped,table-hover. The Paragraph content has been enhanced by using the class lead.<br>
<img src = "https://github.com/fathi129/Mission-to-Mars/blob/master/Screenshots%20for%20Mission%20to%20mars/lead.png" width = 400><br> 
- The grid layouts have been applied for the images, got four equal-width columns starting at desktops and scaling to large desktops by using `.col-md-3`, which are thumbnailed using the class thumbnail.<br> 
<img src = "https://github.com/fathi129/Mission-to-Mars/blob/master/Screenshots%20for%20Mission%20to%20mars/imggrid.png" width = 600><br> 
<img src = "https://github.com/fathi129/Mission-to-Mars/blob/master/Screenshots%20for%20Mission%20to%20mars/Bootstrap_table.png" width = 400><br> 
<img src = "https://github.com/fathi129/Mission-to-Mars/blob/master/Screenshots%20for%20Mission%20to%20mars/Bootsrap%20grid%20image.png" width = 650><br> 


