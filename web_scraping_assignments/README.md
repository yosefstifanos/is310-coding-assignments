# Fandom Web Scraping Assignment

For this assignment, we were required to scrape any fandom of our choosing! For my project, I chose to scrape the Harry Potter fandom page, located at https://harrypotter.fandom.com/wiki/List_of_spells. The wiki page I decided to scrape contains a comprehensive list of spells from the Harry Potter universe.

## Objective

The goal of this project is to extract detailed information about each spell, including the spell name, type, pronunciation, description, and where it was seen or mentioned. This information is then saved into a CSV file for further analysis.

## Robots.txt

The robots.txt file for the Harry Potter fandom can be found here: https://harrypotter.fandom.com/robots.txt. The specific webpage we are scraping falls under the /wiki/Category: page, which is not disallowed.

## Interesting Insights

With this project, I specifically wanted to gather detailed information about the spells used in the Harry Potter universe. This is interesting for researchers and fans because it provides a structured dataset that can be used for various analyses, such as understanding the types of spells, their pronunciations, and their descriptions.

## What You'll Need to Run the `fandom_wiki_scraping.py` File

- Python with `pandas`, `beautifulsoup4`, `requests`, and `csv` installed
- Access to the internet to scrape the webpage
- A love of all things Harry Potter related

## How to Run the Script

1. Ensure you have Python installed on your machine.
2. Install the required libraries using pip:
   ```sh
   pip install pandas beautifulsoup4 requests