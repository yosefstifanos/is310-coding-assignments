# API Getting Data Assignment

## API Selection: Pokemon API (PokeAPI)

For this assignment, I chose to work with the Pokemon API (PokeAPI) because:
1. Pokemon represents a significant cultural phenomenon that has influenced global popular culture
2. It provides well-structured data about Pokemon characters and their attributes
3. It's free and doesn't require authentication, making it accessible
4. The API has clear documentation and reliable endpoints
5. Pokemon's cultural impact makes it interesting to cross-reference with Europeana's cultural heritage data

## Script Description

The script `getting_culture.py`:
- Fetches data about Pikachu from PokeAPI
- Searches for Pokemon-related cultural items in Europeana
- Combines and saves relevant item data from both APIs
- Handles API keys securely
- Includes error handling and cleanup

## Setup Instructions

1. Install required packages:
```bash
pip install requests python-apikey pyeuropeana
```

2. Get a Europeana API key from: https://pro.europeana.eu/pages/get-api

3. Run the script:
```bash
python getting_culture.py
```

## Note
API keys and sensitive information have been excluded from this repository for security reasons.
