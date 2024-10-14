import requests
from bs4 import BeautifulSoup
import csv

url = "https://harrypotter.fandom.com/wiki/List_of_spells"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

with open('harry_potter_spells.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Spell Name", "Type", "Pronunciation", "Description", "Seen/Mentioned"])

    spells_section = soup.find('div', class_='mw-parser-output')
    
    if spells_section:
        spell_headers = spells_section.find_all(['h3', 'h4'])
        for header in spell_headers:
            spell_name = header.text.strip()
            spell_info = ""
            next_element = header.next_sibling
            while next_element and next_element.name not in ['h3', 'h4']:
                if next_element.name == 'dl':
                    spell_info = next_element
                    break
                next_element = next_element.next_sibling

            # Initialize default values
            spell_type = "N/A"
            pronunciation = "N/A"
            description = "N/A"
            seen_mentioned = "N/A"

            if spell_info:
                for dd in spell_info.find_all('dd'):
                    if 'Type:' in dd.text:
                        spell_type = dd.text.replace('Type:', '').strip()
                    elif 'Pronunciation:' in dd.text:
                        pronunciation = dd.text.replace('Pronunciation:', '').strip()
                    elif 'Description:' in dd.text:
                        description = dd.text.replace('Description:', '').strip()
                    elif 'Seen/Mentioned:' in dd.text:
                        seen_mentioned = dd.text.replace('Seen/Mentioned:', '').strip()

            # Debug prints to check the extracted values
            print(f"Spell Name: {spell_name}")
            print(f"Type: {spell_type}")
            print(f"Pronunciation: {pronunciation}")
            print(f"Description: {description}")
            print(f"Seen/Mentioned: {seen_mentioned}")

            writer.writerow([spell_name, spell_type, pronunciation, description, seen_mentioned])
    else:
        print("Unable to find spells section.")