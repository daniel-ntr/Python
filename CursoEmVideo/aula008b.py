import random

import emoji

num = random.randint(1,10) #Gera números aleatório de 1 à 10
print(num)
print(emoji.emojize('OLá, \033[32mMundo\033[m \033[34m:earth_americas:\033[m !', use_aliases=True))