=============================
Game Giveaways_api
=============================


Overview
========

giveaways_api is a Python application for collecting information about current game giveaways from various game stores. 
At this moment, giveaways_api retrieves data from Steam and Epic Games, but since the code is scalable, integrating other game giveaway sources will be a breeze.

Business Logic
==============

The business logic of this API is configured to parse Steam and Epic Games (at the moment of writing this document) using Selenium with the Chrome webdriver.
To ensure the stability of this API, I chose to use selection by HTML tags rather than using XPath.
Selenium extracts the HTML block by tag and provides it to Beautiful Soup.
Additionally, Selenium saves the scraped HTML data to business_logic/parser/data/scrapped_data, with the date as a filename.
However, this feature is designed for users who need to create statistical charts, etc., and is not utilized by the business logic afterward.

Each of the game stores has its own classes, and thanks to the ready-to-use methods for finding the title, game URL, and picture URL in the base parent class, integrating new stores will be straightforward.
If there is a need to modify the flow, you can easily override the parent method.

Then, each store calls the parent class to extract data using Beautiful Soup.
Once the data is ready, the controller classes, named Storename + Main, provide encapsulation and, due to composition, hide the details from the user, providing one method: get_giveaways.
The result is a dictionary in the format of {"store_name_giveaways":[]}.

The Store classes are merged into one Giveaways class, which calls the get_giveaways method for each Store class, updates a local dictionary within it, and then returns the data in accordance with ASGI and pydantic.
The key in the returned dictionary for all endpoints is named 'response'.

Cache
========

Contains the scraped data. The cache is generated once a day, synchronized with USA time.
The API script first checks the data in cache if it's up-to-date, if it is - retrieves it, if not - triggers the parser.

API
===

The API is built on FastAPI.
All endpoints are defined separately in the views folder, and connected to main app as routers.
The API supports Redoc and SwaggerUI, as well it has custom endpoints containing documentation.
All endpoints are protected by an original rate limiting script as a middleware.
This rate-limiting mechanism controls the number of requests from each user. By default, the interval is set to 5 seconds. Users have the flexibility to modify this value by providing a time interval parameter in their requests.
CORS is enabled for wider accessibility.

Testing
=======

The tests are integration,based on returned values, and their types/formats. They are:

- Business logic tests
- API functioning tests

Demo
====

In the root directory you can also find a ui_demo file, which demonstrates a quick visualization of the API response on Streamlit.

Key Components and Workflow
===========================

1. **Caching:**
   - The project employs a cache to store giveaway data for a day (based on USA time), minimizing unnecessary requests to platforms.
   - If cached data is up-to-date, it is used directly; otherwise, fresh data is fetched.

2. **WebDriver Management:**
   - It requires Selenium WebDriver (ChromeDriver) to be downloaded and placed in the correct directory.
   - In the project, a Readme file is provided explaining how to address the Selenium WebDriver incompatibility error, along with a script to automate the download of the driver based on the user's Chrome version.

3. **Data Scraping:**
   - The WebDriver is utilized to extract pertinent HTML blocks containing giveaway information from the target platforms. Users simply need to inherit from the StoreBase class and provide the necessary HTML tags within the required HTML block, including tags for essential data such as game titles, image URLs, and game URLs.
   - The extracted blocks are additionally saved as .html and .txt files for future processing. However, the user needs to decide how they will use the extracted data and must provide the script for handling the processing of these files.

4. **Data Extraction:**
   - Separate classes for each store (Steam, Epic Games) parse the saved HTML blocks to extract specific details (title, image URL, game URL).

5. **Error Handling:**
   - An error handler class is utilized to gracefully manage potential exceptions during scraping, data extraction, and cache operations. The majority of possible errors are handled, providing new and more informative feedback.

6. **Parser Controller:**
   - The `Giveaways` class acts as a central controller, coordinating the interactions with different store classes and returning a unified API response containing giveaway data from all supported platforms.

Additional Insights
===================

- **Modular Structure:** The project's organization into modules enhances code reusability and maintainability.
- **Error Handling:** The attention to error management improves user experience and data reliability.
- **Future Expansion:** The modular design allows for easy addition of new store platforms and features.

Known Issues
============

Two issues are related to Selenium, NotMatchingDriverVersion is handled by the original install-helper script.
Whereas in case of BrowserNotFound you need to download Chrome browser manually.

In case of having None result by the API, instead of game names: the issue may lie in html tags this API uses,
and the website updated its structure. Inspect the website, and change the container tags in the config file.

In the config package are defined all of those variables that may change by time, to enhance user experience.

Technologies Used
=================

FastAPI, Selenium, BeautifulSoup4, etc.
