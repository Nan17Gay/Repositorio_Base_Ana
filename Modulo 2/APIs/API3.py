import requests

id = 8
url = f'http://127.0.0.1:5000/alunosn/{id}'

troca = {
    'Aluno': 'Priscila',
    'Idade': '17 anos',
    'Cursando': 'Programacao com Py',
    'id': 8
}

response = requests.put(url, json=troca)
print(response.status_code)

if response.status_code == 200:
    print('Requisição bem-sucedida!')
    print('---------------------------------------------------')
    print(response.json())
    print('---------------------------------------------------')
else:
    print(f"Erro na requisição. Código de status: {response.status_code}")
    print('---------------------------------------------------')