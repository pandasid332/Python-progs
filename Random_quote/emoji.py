import random
import os
import requests
from time import sleep

filename = 'quotes.txt'
url = 'https://api.quotable.io/random'

def load_quotes():
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

def save_quotes(quote):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(quote + '\n')

def fetch_online_quote(retries=3, delay=5):
    for _ in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return '{}\n-{}'.format(data['content'], data['author'])
            else:
                print('❌ Failed to fetch online quote. Loading offline quote')
                return None
        except requests.exceptions.RequestException as e:
            print(e)
            print(f'❌ No internet. Retrying in {delay} seconds...')
            sleep(delay)
    print('❌ No internet. Loading offline quote')
    return None

def show_random_quote():
    online_quotes = fetch_online_quote()
    if online_quotes:
        print('\n🌏 Online quote of the day: ')
        print(f'📢 "{online_quotes}"')
    else:
        quotes = load_quotes()
        if quotes:
            print('\n📚 Offline quote of the day: ')
            print(f'📢 "{random.choice(quotes)}"')
        else:
            print('❌ No quotes available. Add some quotes to file.')

def add_quote():
    new_quote = input('\n➕ Enter new quote: ').strip()
    if new_quote:
        save_quotes(new_quote)
        print('✅ Quote added successfully.')

def main():
    while True:
        print('\n📌 Quote Generator')
        print('1️⃣  Show random quote')
        print('2️⃣  Add new quote')
        print('3️⃣  Exit')
        choice = input('\nEnter your choice(1-3): ').strip()
        if choice == '1':
            show_random_quote()
        elif choice == '2':
            add_quote()
        elif choice == '3':
            print('👋 Thank you for using the app.')
         
            break
        else:
            print('❌ Invalid choice. Try again.')

if __name__ == '__main__':
    main()