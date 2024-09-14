import urllib.request
import json

def get_random_joke():
    try:
        with urllib.request.urlopen("https://official-joke-api.appspot.com/random_joke") as response:
            joke_data = json.load(response)
            joke_setup = joke_data['setup']
            joke_punchline = joke_data['punchline']
            return f"{joke_setup}\n{joke_punchline}"
    except urllib.error.URLError as e:
        print("Error fetching jokes:", e)
        return None

def main():
    print("Welcome to the Random Joke Generator!")

    while True:
        user_input = input("Press 'Enter' to get a random joke or type 'exit' to quit: ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        joke = get_random_joke()

        if joke:
            print("Random Joke:")
            print(joke)

if __name__ == "__main__":
    main()
