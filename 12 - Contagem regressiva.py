import time
import emoji
from time import sleep

print('Contagem regressiva para o ano novo')

for c in range(10, -1, -1):
    print(c,'...')
    sleep(1)
print('FELIZ ANO NOVO!!!!')
print(emoji.emojize(':fireworks:'*40))