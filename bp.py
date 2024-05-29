pessoa = {
    'Nome': 'João',
    'Idade': 17,
    'Profissão': 'Estudante',
    'Empresa': 'SENAI',
    'Gênero': 'Masculino',
    'Cidade': 'Samambaia-Sul'
}

# remover chave
del pessoa[input('Informe o nome da chave a ser deletada:')]

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')