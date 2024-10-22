import requests
import json
import os
import apikey
from pyeuropeana.apis import search

# Set up Europeana API key
def setup_europeana():
    try:
        europeana_api_key = apikey.load("EUROPEANA_API_KEY")
    except:
        europeana_api_key = input("Please enter your Europeana API key: ")
        apikey.save("EUROPEANA_API_KEY", europeana_api_key)
    
    os.environ['EUROPEANA_API_KEY'] = europeana_api_key

# Function to get Pokemon data
def get_pokemon_data(pokemon_name="pikachu"):
    """Get data about a specific Pokemon from PokeAPI"""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        print("\nPokemon API Response:")
        pokemon_data = response.json()
        # Extract just the relevant item data
        pokemon_item = {
            "name": pokemon_data["name"],
            "id": pokemon_data["id"],
            "types": [t["type"]["name"] for t in pokemon_data["types"]],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"]
        }
        print(json.dumps(pokemon_item, indent=2))
        return pokemon_item
    else:
        print(f"Error accessing PokeAPI: {response.status_code}")
        return None

# Function to search Europeana for related content
def search_europeana(query):
    """Search Europeana for items related to the query"""
    try:
        response = search(query=query)
        
        # Remove API key from response for security
        if 'apikey' in response:
            del response['apikey']
        
        print("\nEuropeana Response:")
        
        # Extract just the relevant items data
        if 'items' in response:
            items = []
            for item in response['items']:
                # Extract only essential item information
                cleaned_item = {
                    'title': item.get('title', ['Unknown'])[0],
                    'creator': item.get('dcCreator', ['Unknown'])[0] if 'dcCreator' in item else 'Unknown',
                    'year': item.get('year', ['Unknown'])[0] if 'year' in item else 'Unknown',
                    'type': item.get('type', 'Unknown'),
                    'country': item.get('country', ['Unknown'])[0] if 'country' in item else 'Unknown'
                }
                items.append(cleaned_item)
            print(json.dumps(items, indent=2))
            return items
        return []
    except Exception as e:
        print(f"Error accessing Europeana: {e}")
        return []

# Function to save combined data to JSON
def save_to_json(pokemon_data, europeana_items, filename):
    """Save the combined data to a JSON file"""
    combined_data = {
        'pokemon_item': pokemon_data,
        'europeana_items': europeana_items
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, indent=2, ensure_ascii=False)

def cleanup_api_key():
    """Remove the API key after use"""
    try:
        # No need to delete from apikey module if not supported
        # Only delete from environment variables
        if 'EUROPEANA_API_KEY' in os.environ:
            del os.environ['EUROPEANA_API_KEY']
        print("\nAPI key has been deleted from the environment successfully")
    except Exception as e:
        print(f"\nError deleting API key: {e}")

def main():
    try:
        # Setup Europeana API
        setup_europeana()
        
        # Get Pokemon data
        pokemon_data = get_pokemon_data("pikachu")
        
        if pokemon_data:
            # Search Europeana for related content about Pokemon
            europeana_items = search_europeana("Pokemon game culture")
            
            if europeana_items:
                # Save the combined data
                save_to_json(pokemon_data, europeana_items, 'pokemon_europeana_data.json')
                print("\nData has been saved to pokemon_europeana_data.json")
    
    finally:
        # Always cleanup the API key, even if an error occurs
        cleanup_api_key()

if __name__ == "__main__":
    main()