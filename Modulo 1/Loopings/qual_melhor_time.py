time = input('Digite o nome do melhor time do Brasil: ')

while time != 'Verdão':
    time = input('Qual é o melhor time do Brasil? ')
    if time == 'Verdão':
        print('Você acertou! Vai Palmeiras!')
    elif time == 'Timão':
        print('Credo! Errou feio! Tente novamente!')
    elif time == 'Santos':
        print('Errou, vovô! Tente novamente!')
    elif time == 'Mengão':
        print('Esse também! porém, Tente novamente!')
    elif time == 'Vasco':
        print('Meus pêsames! Tente novamente!')
    else:
        print('Tente novamente!')