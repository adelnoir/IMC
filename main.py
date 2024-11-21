import sqlite3

conn = sqlite3.connect('user.db')
cursor = conn.cursor()

def criar_tabela():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    altura REAL NOT NULL,
    peso REAL NOT NULL
        )
    ''')

def inserir_user():
    print("\nInserir um user\n---------------")

    try:
        nome = input("Insira o nome do usuário: ").capitalize()
        idade = int(input("Insira a idade do usuário: "))
        while True:
            try:
                altura = float(input("Insira a altura do usuário (em metros): "))
            
                if altura > 3:
                    print("[Altura inválida. Lembre-se de um inserir um valor inferior a 3 e em metros]")
                else:
                    break
            except ValueError:
                print("[Valor inserido inválido.]")
                continue
        
        while True:
            try:
                peso = float(input("Insira o peso do usuário (em kg): "))
                if peso <= 0:
                    print("[Peso inválido. Insira um valor positivo.]")
                else:
                    break  # Peso válido, sair do loop
            except ValueError:
                print("[Valor inválido. Por favor, insira um número válido para o peso.]")

        cursor.execute('INSERT INTO users (nome, idade, altura, peso) VALUES (?, ?, ?, ?)',
                       (nome, idade, altura, peso))
        conn.commit()
        
        print(f"[Usuário '{nome}' inserido com sucesso!]")

    except ValueError:
        print("[Erro: Insira valores válidos para idade, altura e peso.]")
        

def consultar_user():
    nome = input("\nInsira um nome para consultar e calcular o IMC: ").capitalize()
    cursor.execute('SELECT nome,altura,peso FROM users WHERE nome = ?', (nome,))
    user = cursor.fetchone()
    if user:
        nome, altura, peso = user
        imc = peso / (altura ** 2)
        print(f"\n[Nome: {nome}]\n[Altura: {altura:.2f}m]\n[Peso: {peso:.2f}kg]\n[IMC: {imc:.2f}]")

def limpar_bd():
    cursor.execute('DROP TABLE users')
    criar_tabela()
    conn.commit()

def main():
    criar_tabela()
    while True:
        try:
            inp = int(input("\nO que deseja fazer?\n[1] - Inserir user\n[2] - Consultar com base no nome e calcular IMC\n[3] - Apagar dados\n[0] - Sair\n"))
            
            if inp == 1:
                inserir_user()
            
            elif inp == 2:
                consultar_user()   
            elif inp == 3:
                limpar_bd()
            elif inp == 0:
                inp = int(input(
                    "\nDeseja sair?\n[1] - Sim\n[2] - Não\n"
                ))
            
                if inp == 1:
                    print("[Saindo...]")
                    break  # Encerra o laço para sair do programa
            
                elif inp == 2:
                    continue    
                else:
                    print("[Opção inválida. Tente novamente.]")
        except ValueError:
                print("[Valor inserido inválido. Tente novamente.]")
                continue

main()
