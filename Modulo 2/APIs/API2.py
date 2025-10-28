import requests

response = requests.get('http://127.0.0.1:5000/alunosn')

print(response.status_code)
print(response.text)
print('---------------------------------------------------')

dados = {
    'Aluno': 'Nan',
    'Idade': '18 anos',
    'Cursando': 'Programacao com Py',
    'id': 8
}

responses = requests.post('http://127.0.0.1:5000/alunosn', json=dados)

print(response.status_code)
print(response.json())
print('---------------------------------------------------')

if response.status_code == 200:
    print('Requisição bem-sucedida!')
    print('---------------------------------------------------')
    print(response.json())
    print('---------------------------------------------------')
else:
    print(f"Erro na requisição. Código de status: {response.status_code}")
    print('---------------------------------------------------')