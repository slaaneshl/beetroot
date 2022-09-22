def isalpha(*args):
    for i in args:
        if i.isdigit():
            print('Error')
            exit()


# task 1
def favorite_movie(name):
    print(f'My favorite movie is {name.title()} too')


user_fav_film = input("what's is your favorite films? ")
isalpha(user_fav_film)
favorite_movie(user_fav_film)


# task 2
def make_country(country, capital):
    country_dict = {country: capital}
    print(country_dict)


make_country('U.S.A', 'Los Angeles')
user_country = input('Write Country: ').capitalize()
user_capital = input('Write Capital: ').capitalize()
isalpha(user_capital, user_capital)
make_country(user_country, user_capital)


# task 3
def make_operation(sym, *args):
    result = args[0]
    for n in args[1:]:
        if sym == '+':
            result += n
        if sym == '-':
            result -= n
        if sym == '*':
            result *= n
    print(result)


make_operation('*', 24, 2, 10)
