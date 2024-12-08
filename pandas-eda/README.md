```markdown
# Goodreads and NYT Bestseller Analysis

This repository contains an exploratory data analysis of Goodreads and NYT Bestseller datasets, focusing on various aspects such as ratings, publication trends, prolific authors, genres, and author gender distribution.

## Project Overview
Analyzes the representation, performance, and trends of books in contemporary literature using Goodreads and NYT Bestseller datasets.

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install requirements:
```bash
pip install pandas altair numpy
```

3. Data Requirements:
- Place datasets in the root directory:
  - goodreads_library_export.csv
  - nyt_bestsellers.csv

## Structure
- `eda_notebook.ipynb`: Main analysis notebook
- `README.md`: This file

## Visualizations and Analyses

### Visualization 1: Distribution of Goodreads Ratings
```python
rating_distribution = alt.Chart(goodreads_df).mark_bar().encode(
    alt.X('gr_avg_rating:Q', bin=alt.Bin(maxbins=30), title='Goodreads Average Rating'),
    alt.Y('count()', title='Number of Books')
).properties(
    title='Distribution of Goodreads Ratings'
)
rating_distribution.display()
```
**Analysis**: This chart shows the distribution of average ratings for books on Goodreads. Most books have an average rating between 3.5 and 4.5, indicating that readers generally rate books positively.

### Visualization 2: Number of Books by Publication Year
```python
books_by_year = alt.Chart(goodreads_df).mark_bar().encode(
    alt.X('pub_year:O', title='Publication Year'),
    alt.Y('count()', title='Number of Books')
).properties(
    title='Number of Books by Publication Year'
)
books_by_year.display()
```
**Analysis**: This chart shows the number of books published each year. There is a noticeable increase in the number of books published in recent years, which could be due to the growth of the publishing industry and the rise of self-publishing.

### Visualization 3: Top 10 Authors with Most Books
```python
top_authors = goodreads_df['author'].value_counts().nlargest(10).reset_index()
top_authors.columns = ['author', 'count']

top_authors_chart = alt.Chart(top_authors).mark_bar().encode(
    alt.X('author', sort='-y', title='Author'),
    alt.Y('count', title='Number of Books')
).properties(
    title='Top 10 Authors with Most Books'
)
top_authors_chart.display()
```
**Analysis**: This chart shows the top 10 authors with the most books in the dataset. It highlights the most prolific authors and their contribution to literature.

### Visualization 4: Number of Books by Genre
```python
genre_chart = alt.Chart(genre_count).mark_bar().encode(
    alt.X('genre', sort='-y', title='Genre'),
    alt.Y('count', title='Number of Books')
).properties(
    title='Number of Books by Genre'
)
genre_chart.display()
```
**Analysis**: This chart shows the number of books by genre. It provides insight into the most popular genres in the dataset, with 'na' (not available) being the most common, followed by 'history' and 'fantasy'.

### Visualization 5: Number of Books by Author Gender
```python
gender_chart = alt.Chart(goodreads_df).mark_bar().encode(
    alt.X('author_gender', title='Author Gender'),
    alt.Y('count()', title='Number of Books')
).properties(
    title='Number of Books by Author Gender'
)
gender_chart.display()
```
**Analysis**: This chart shows the number of books by author gender. It reveals the gender distribution of authors in the dataset, with a higher number of male authors compared to female authors.

## Notes
- Uses simple text matching for soccer content identification
- Geographic classification is simplified
- Visualizations created with Altair
```

This README.md provides an overview of the project, setup instructions, and detailed descriptions of the visualizations and analyses included in your notebook. Adjust the column names and data processing steps according to your actual dataset structure.