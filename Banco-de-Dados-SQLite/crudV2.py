from os import path
from sqlite3 import dbapi2 as sqlite
from sqlite3 import Error
from time import sleep

class BancoDeDados:

    def __init__ (self):
        
        self.dataBase = 'bancoAlunosV2.db'
        self.conexao = sqlite.connect(self.dataBase)
        self.dbCursor = self.conexao.cursor()
        self.create()

         
    def create(self):

        try:
            self.dbCursor.execute ("""
            CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            matricula VARCHAR(20) NOT NULL UNIQUE,
            sexo CHAR(1) NOT NULL,
            nascimento VARCHAR(20)
            );
        """)

        except Exception as e:
            print(f'Não foi possível criar a tabela.\nErro: {e}')
            
        else:
            pass

    def insert (self):

        try:
            nome = input('Digite o nome do aluno: ')
            matricula = input('Digite a matrícula: ')
            sexo = input('Digite o sexo [ M / F ]: ')
            nascimento = input('Digite a data de nascimento (00/00/0000): ')

            self.dbCursor.execute('INSERT INTO alunos (nome, matricula, sexo, nascimento) VALUES (?, ?, ?, ?);', [nome, matricula, sexo, nascimento])
            
        except Exception as e:
            print(f'Falha em cadastrar o aluno!\nErro: {e}\n')
            print(f'Desfazendo a operação')
            self.conexao.rollback()
            
        else:
            self.conexao.commit()
            self.dbCursor.close()
            self.conexao.close()
            print('Cadastro realizado com sucesso!')
           
        
    def read (self):

        try:
            matricula = input('Informe a matrícula do aluno: ')

            self.dbCursor.execute('SELECT * FROM  alunos WHERE matricula = ?;', [matricula])
            dados = self.dbCursor.fetchone()

            print(f'Aluno: {dados[1]},\nMatrícula: {dados[2]},\nSexo: {dados[3]}')

        except Exception as e:
            print(f'Matrícula não encontrada no sistema!')

        else:
            self.dbCursor.close()
            self.conexao.close()
            print('\nConsulta finalizada.')
            

    # corrigir e fazer alterações!
    def update (self):
        
        try:
            nome = input('Digite o nome do aluno: ')
            matricula = input('Digite a matrícula: ')
            sexo = input('Digite o sexo [ M / F ]: ')
            nascimento = input('Digite a data de nascimento (00/00/0000): ')

            self.dbCursor.execute('UPDATE alunos SET nome = ?, sexo = ?, nascimento = ? WHERE matricula = ?;', [nome, sexo, nascimento, matricula])

        except Exception as e:
            print(f'Não foi possível atualizar os dados do cadastro.\nErro: {e}')
            print(f'Desfazendo a última ação {e}')
            self.conexao.rollback()

        else:
            self.conexao.commit()
            self.dbCursor.close()
            self.conexao.close()
            print('Dados do cadastro atualizados com sucesso!')

    # corrigir e fazer alterações!
    def delete(self):

        try:
            matricula = input('Informe a matricula: ')

            self.dbCursor.execute('DELETE FROM alunos WHERE matricula = ?;', [matricula])

        except Exception as e:
            print(f'Falha na exclusão do cadastro.\nErro: {e}')
            print(f'Desfazendo a última ação {e}')
            self.conexao.rollback()

        else:
            self.conexao.commit()
            self.dbCursor.close()
            self.conexao.close()
            print('O cadastro foi excluído com sucesso!')


# Menu
while True:

  dbAlunos = BancoDeDados()

  print('''
      ______________________________________________________________
                            
                            CADASTRO DE ALUNOS
      ______________________________________________________________
           
      ( 1 ) - Inserir os dados do aluno no sistema.
      ( 2 ) - Realizar a busca do aluno no sistema.
      ( 3 ) - Alterar ou atualizar os dados no cadastro do aluno.
      ( 4 ) - Remover o cadastro do aluno no sistema.
      ( 5 ) - Encerrar o programa.
      ''')

  opcao = input("Escolha uma opção: ")

  if opcao == '1':
    dbAlunos.insert()

  elif opcao == '2':
    dbAlunos.read()

  elif opcao == '3':
    dbAlunos.update()

  elif opcao == '4':
    dbAlunos.delete()

  elif opcao == '5':
    print('Encerrando o programa...')
    sleep(2)
    break

  else:
    print('Opção inválida! Use apenas números de 1 a 4.')

print("Programa encerrado.")
