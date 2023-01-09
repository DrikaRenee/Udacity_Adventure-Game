import time
import random
import string


def typewriter_simulator(message):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.5)
        time.sleep(.03)
    print('')


def print_pause(statement, delay=0):  # spaces out responses
    print(statement)
    time.sleep(delay)


def valid_input(prompt, options):  # checks for validity
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'I don\'t think Beyonce asked for "{option}", Try again.')


def intro():
    print_pause('Beyonce needs a new publicist and for some reason she'
                ' chose you.\n', 2)
    print_pause(
        'She has a new album coming out and instead of her normal'
        ' surprise drop she decides to do a normal rollout.\n', 2)
    print_pause('Can you survive one day?\n', 2)
    print_pause("Don't get fired!!\n", 2)


def make_choice():
    response = valid_input("You check your email and have two things to "
                           "choose from for the day, a photoshoot and"
                           "a music video shoot\n\n"
                           "You get to choose what Beyonce does for the day, "
                           "what will you choose? Photoshoot or videoshoot?\n",
                           ["photoshoot", "videoshoot"])
    if response == 'photoshoot':
        print_pause("Let's go!", 2)
        photoshoot()
    elif response == 'videoshoot':
        print_pause("Let's go!", 2)
        video_shoot()

    print_pause("\nGood luck, and remember don't get fired!", 2)


def play_againg():
    response = valid_input("Good job on making it!\nGive it another go?"
                           "Answer y or n.\n", ["y", "n"])
    if response == "y":
        make_choice()
    elif response == "n":
        print("Bey loved your choices today, see you tomorrow!")
        exit(0)


def play_againb():
    response = valid_input("Yikes, it looks like you couldn't cut it.\n"
                           "Give it another go? Answer y or n.\n",
                           ["y", "n"])
    if response == "y":
        make_choice()
    elif response == "n":
        print("Bey definitely doesn't hate you despite how she looked."
              " Maybe try again another day.")
        exit(0)


def break_time():
    card = random.choice(["red 1", "blue 5", "green 2", "yellow 7"])
    print_pause(
        "It's been a super long day and Bey needs a break.\n\n"
        "Blue Ivy is nearby and wants to play Uno.\n"
        "Bey agrees and they play until they're both"
        " at the last card in their hands.\n", 1)
    print_pause("\nBeyonce has a red 2 in her hands, Blue has a green 4.\n", 1)
    print_pause("The card at the top of a deck is a red 4.\n", 1)
    print_pause("Beyonce draws a card", 1)
    typewriter_simulator('...')
    print_pause("it is a " + card + "!", 1)
    if card == "red 1":
        print("Bey draws a red 1, she plays the card and since",
              "they're playing house rules she is able to discard"
              "both cards and wins!\n",
              "Blue isn't happy, but losing is part of the game.\n",
              "Congrats! You made it through a day of being Beyonce's"
              "assistant!")
        play_againg()
    elif card == "blue 5":
        print("Bey draws a blue 4, she plays it.\n"
              "Blue draws a Draw 4, she plays that"
              " instead of the blue 4 and calls the color green.\n"
              "Since Bey did not have a draw 4, she had to draw the 4 cards.\n"
              "Blue plays her last card and wins.\n"
              "Beyonce is mad at you because she lost and fires you.")
        play_againb()
    elif card == "green 2":
        print("Bey draws a green 2,"
              "she plays the red 2 in her hands.\n"
              "Blue had to draw a card, a yellow 8.\n"
              "Beyonce draws again and draws a wild card"
              " and calls the color green.\n"
              "Blue did not have a green card so she had to draw again.\n"
              "Bey draws a green 3, since they're playing house rules"
              " she is able to discard both cards and wins!\n"
              "Blue isn't happy, but losing is part of the game.\n"
              "Congrats! You made it through a day of being"
              " Beyonce's assistant!")
        play_againg()
    elif card == "yellow 7":
        print("Bey draws a yellow 7, she plays it.\n"
              "Blue draws a Draw 4, she plays that instead of the blue 4"
              " and calls the color green.\n"
              "Since Bey did not have a draw 4, she had to draw the 4 cards.\n"
              "Blue plays her last card and wins.\n"
              "Beyonce is mad at you because she lost and fires you.")
    play_againb()


def photoshoot():
    response = valid_input("So you chose the photoshoot\n"
                           "Everything was going well"
                           " until the director was away when an"
                           " important decision needed to be made, "
                           "lighting.\nThe theme is neo-disco and the"
                           " lighting must be perfect.\n"
                           "Beyonce asked for your input, purple lighting "
                           "or blue lighting.\n"
                           "What will you choose?: purple or blue?",
                           ['purple', 'blue'])
    if response == "purple":
        print_pause("Good choice! A few test shots were taken under purple"
                    " lighting and Beyonce loved the look!", 4)
        break_time()
    elif response == "blue":
        print("Did Beyonce not tell us to never put a black girl under"
              " blue lights?. Get out.")
        play_againb()


def gift():
    gift = random.choice(['the Formation World Tour DVD',
                          'an early copy of her autobiography',
                          'an invite to every Roc Nation Brunch'
                          'as long as its held',
                          'a sneak peek at the files on the infamous MacBook',
                          'a date with Julius'])
    print_pause(
        f'Heck Yeah! Bey loved your work so much'
        ' today that she decided to slide you a gift.'
        'It\'s {gift}.\nHow does it feel being the'
        'luckiest person on earth?', 2)


def loc_style():
    genre = random.choice(["country", "rock", "disco"])
    print_pause(
        'Beyonce loves to keep us on our toes.'
        ' As she likes to say, "stay ready"'
        "\nThis time she wouldn't tell the team'"
        " what the genre is until she felt like it.\n",
        2)
    print_pause(f"You finally get a text from her with just"
                "one word, {genre}.\n\n", 2)
    if genre == "country":
        country_pick = valid_input(
            "Looks like the genre is country. We already have a style,"
            " but where should we film?, NYC or Houston?",
            ['nyc', 'houston'])
        if country_pick == "NYC":
            print_pause('Uh...ok.')
            play_againb()
        elif country_pick == 'Houston':
            print_pause('Duh, why would Mrs. Third Ward Trill'
                        ' NOT pick her hometown?')
            gift()
            play_againg()

    if genre == "rock":
        rock_pick = valid_input('Don\'t Hurt Yourself WAS the best song on '
                                'Lemonade, so you\'re totally loving the rock '
                                'idea.\nWe know where this video is going to'
                                ' be shot, we just need a hairstyle.\nWe '
                                'can go Bettie Page bang or full out mohawk.\n'
                                '\nWhat\'ll it be? Bettie or mohawk?',
                                ['bettie', 'mohawk'])
        if rock_pick == "bettie":
            print_pause('We already know that Bey loves this hairstyle.'
                        ' Good Job!', 2)
            gift()
            play_againg()

        elif rock_pick == "mohawk":
            print_pause("Cliche. Bleh. Bye", 2)
            play_againb()

    if genre == "disco":
        disco_pick = valid_input(
            "The 70's are back babes. We already have the styling"
            " down, lets find the perfect location.\n"
            "She already mentioned two potential spots,"
            " so it's up to you to choose."
            "Are we going with studio54 or Barclays?",
            ["studio54", "barclays"])
        if disco_pick == 'studio54':
            print_pause('Nice! Definitely on theme!')
            gift()
            play_againg()

        elif disco_pick == 'barclays':
            print_pause('Why? Beyonce fires you personally.')
            play_againb()


def video_shoot():
    print_pause("We're going with the video shoot, eh?\n", 1)
    print_pause(
        "\nYour first task is to choose the video cameo. "
        "You checked around and found that Azealia Banks "
        "and Adele were available today.\n", 1)
    response = input("\nSo who are you calling?, Azealia or Adele?\n")
    if response == "azealia":
        print_pause("Interesting choice.\n", 2)
        print_pause(
            "You FaceTime Azealia and she doesn't answer."
            "You call her publicist and find out that she"
            " flew to Austin at the last minute"
            "to hang out with her friend Grimes and "
            "it is unknown when she will return.\n", 2)
        print_pause(
            "Beyonce really didn't want Azealia to show up,"
            " she was just being nice. "
            "She still needed a good cameo, she's"
            " annoyed and you're fired.\n", 2)
        play_againb()
    elif response == 'adele':
        print_pause("Beyonce ADORES Adele and Adele, Beyonce. "
                    "Their chemistry will lead to a great video shoot!\n", 2)
        print_pause("Now that we have the cameo out the way, "
                    "we need to think about styling and location.\n", 2)
        loc_style()


def main():
    intro()
    make_choice()
    photoshoot()
    video_shoot()
    loc_style()
    play_againg()


main()
