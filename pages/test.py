link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'

def test1(link):
    if (link.find('login') == -1):
        return False
    else:
        return True

assert test1(link), 'fail'
