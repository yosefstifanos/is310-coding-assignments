# Soccer Themes in Literature Analysis

This repository contains an exploratory data analysis of soccer-themed literature using the Goodreads Top Novels and NYT Bestsellers datasets.

## Project Overview
Analyzes the representation, performance, and trends of soccer-related books in contemporary literature.

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
- Place datasets in `data/` directory:
  - goodreads_library_export.csv
  - nyt_bestsellers.csv

## Structure
- `SoccerThemesInPopularLiterature.ipynb`: Main analysis notebook
- `data/`: Dataset directory
- `README.md`: This file

## Analysis Features
- Identification of soccer-themed literature
- Rating and performance analysis
- Geographic distribution study
- Temporal trends examination

## Notes
- Uses simple text matching for soccer content identification
- Geographic classification is simplified
- Visualizations created with Altair
