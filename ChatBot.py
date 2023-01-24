#ChatBot
import random
import pyjokes
import json
import requests
import BlackJackGame

def recommend_movie(genre):
    url = "https://api.themoviedb.org/3/discover/movie?api_key=<API_KEY>&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres="+str(genre)
    data = json.loads(requests.get(url).text)
    return data['results'][random.randint(0,len(data['results']))]['original_title']


def recommend_music(genre):
    url = "https://api.deezer.com/search?q=genre:"+genre+"&limit=25"
    data = json.loads(requests.get(url).text)
    return data['data'][random.randint(0,len(data['data']))]['title']


def play_game():
    games = ["Rock-paper-scissors", "Guess the number", "Guess the number"]
    return random.choice(games)


def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    while True:
        computer_choice = random.choice(options)
        user_choice = input("What's your choice? (rock, paper, scissors): ").lower()
        while user_choice not in options:
            user_choice = input("Invalid input, please try again. (rock, paper, scissors): ").lower()
        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You win! Rock beats scissors.")
        elif user_choice == "rock" and computer_choice == "paper":
            print("You lose! Paper beats rock.")
        elif user_choice == "paper" and computer_choice == "rock":
            print("You win! Paper beats rock.")
        elif user_choice == "paper" and computer_choice == "scissors":
            print("You lose! Scissors beat paper.")
        elif user_choice == "scissors" and computer_choice == "rock":
            print("You lose! Rock beats scissors.")
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You win! Scissors beat paper.")
        exit_game = input("Do you want to exit the game? (y/n)").lower()
        if exit_game == "y":
            break


def guess_the_number():
    while True:
        target_number = random.randint(1, 100)
        guess = None
        tries = 0
        print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
        while guess != target_number:
            guess = int(input("Your guess: "))
            tries += 1
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
        print(f"Congratulations! You guessed the number in {tries} tries.")
        exit_game = input("Do you want to exit the game? (y/n)").lower()
        if exit_game == "y":
            break


def chatbot():
    while True:
        user_input = input("What would you like to do? (Recommend a movie, recommend music, play a game, tell a joke, or exit): ")
        if user_input.lower() == "recommend a movie":
            genre = input("Which genre do you prefer? (Action, Adventure, Animation, Comedy, Crime, Documentary, Drama, Family, Fantasy, History, Horror, Music, Mystery, Romance, Science Fiction, TV Movie, Thriller, War, Western): ")
            print(recommend_movie(genre))
        elif user_input.lower() == "recommend music":
            genre = input("Which genre do you prefer? (pop, rock, hip hop, metal, country, classical, electronic, folk, jazz, reggae, R&B, soul, funk, blues, latin, gospel, funk, punk, and so on): ")
            print(recommend_music(genre))
        elif user_input.lower() == "play a game":
            game_choice = input("Which game do you want to play? (Guess the number, Rock paper scissors, Blackjack): ")
            if game_choice.lower() == "guess the number":
                guess_the_number()
            elif game_choice.lower() == "rock paper scissors":
                rock_paper_scissors()
            elif game_choice.lower() == "blackjack":
                BlackJackGame.test_game()
        elif user_input.lower() == "tell a joke":
            print(pyjokes.get_joke())
        elif user_input.lower() == "exit":
            break
        else:
            print("Invalid input. Please try again.")

chatbot()
