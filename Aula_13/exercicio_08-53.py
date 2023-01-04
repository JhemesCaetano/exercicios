#crie um programa que leia uma frase qualquer e diga se ela é um polindromo.
# desconsiderando os espaços.
import  time
frase = str(input('Digite uma frase:'))
frase1 = frase.replace(' ', '').lower()
frase2 = frase[::-1].replace(' ','').lower()
if frase1 == frase2:
    print(f'a frase "{frase}" é um polindromo')
    time.sleep(1)
    print(f'''-"{frase1}"
-"{frase2}"''')
else:
    print(f'a frase "{frase}" não é um polindromo')
    time.sleep(1)
    print(f'''-"{frase1}"
-"{frase2}"''')

# resposta guanabra com for
# frase = str(input('Digite uma frase')).strip().upper()
# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = ''
# for letra in range(len(junto) - 1, - 1, - 1,):
#     inverso += junto[letra]
# if inverso == junto:
#     print('temos um palíndromo!')
# else:
#     print('A frase digitada não é um palíndromo!')
