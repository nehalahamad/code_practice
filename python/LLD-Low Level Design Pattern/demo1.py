import icecream


print(list(filter(lambda x:not x.startswith('_'), dir(icecream))))


