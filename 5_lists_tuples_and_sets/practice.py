import time
while True:
    print('Hello friend, I\'m Jean a chat-bot!')
    user_name = input("What's your name? ").lower()
    user_age = input(f"Well met, {user_name.title()}!\nHow old are you?(numbers) ")
    try:
        num = int(user_age)
    except ValueError:
        print('Issue with input, try again!')
        time.sleep(1)
        continue
    if 17 < num < 30:
        print('Your taking the best time in your live!')
    if 14 < num < 18:
        print('Dude, your future is in your hands!')
    if 29 < num < 100:
        print(f'Extraordinary, you older than me by {num - 18}!')
    if num < 15:
        print('You too young')
    time.sleep(1)
    topic = input('What we’re gonna talk about?\n1. Our courses\n2. Travel\n3. Food\nType number of topic: ')
    time.sleep(0.5)
    if topic == '1':
        answer_first = input('Do you feel satisfaction while you studying in Beetroot Academy?(yes/no) ').lower()
        time.sleep(0.5)
        if answer_first == 'yes':
            print("Me too! That's awesome, good luck to us in our future)")
        else:
            print("It isn't okay, try to think why it's...")
    if topic == '2':
        answer_two = input('My first journey was in Egypt and I saw Pyramids of Giza! '
                           'But what about your first time? ')
        print('OMG!!! How unusual 0_0')
    if topic == '3':
        answer_three = input("What's is your favorite food? ")
        time.sleep(0.5)
        print(f"Wow, I like {answer_three} too!")
    else:
        print('Issue with input, try again!')
        time.sleep(1)
        continue
    print("Bye mate!")
    time.sleep(3)