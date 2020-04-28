def create_list(n):
    return [i for i in range(n) if i % 2 == 0]


def country_capital():
    countries_dict = {'Ukraine': 'Kiev', 'Norway': 'Oslo', 'Poland': 'Warsaw'}
    countries_list = ['Ukraine', 'Poland', 'Denmark']
    for country in countries_list:
        if country in countries_dict:
            print(countries_dict[country])


def fizzbizz():
    for i in range(1, 101):
        if i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Bizz')
        elif i % 15 == 0:
            print('FizzBizz')
        else:
            print(i)


def bank(amount, years, percent, capitalization=False):
    if capitalization:
        for i in range(years):
            amount += amount * percent / 100
        return amount
    else:
        return amount + (amount * percent / 100) * years
