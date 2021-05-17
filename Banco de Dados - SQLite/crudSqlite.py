from os import path
from sqlite3 import dbapi2 as sqlite
from sqlite3 import Error
from time import sleep

class BancoDeDados:

    def __init__ (self):
        
        self.dataBase = 'bancoAlunos.db'
        self.conexao = sqlite.connect(self.dataBase)
        self.dbCurse = self.conexao.cursor()
        self.create()

         
    def create(self):

        try:
            self.dbCurse.execute ("""
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

    # alterar e otimizar!
    def insert (self):

        try:
            nome = input('Digite o nome do aluno: ')
            matricula = input('Digite a matrícula: ')
            sexo = input('Digite o sexo [ M / F ]: ')
            nascimento = input('Digite a data de nascimento (00/00/0000): ')

            inserir = 'INSERT INTO alunos (nome, matricula, sexo, nascimento) VALUES (?, ?, ?, ?);'
            self.conexao = sqlite.connect(self.dataBase)
            self.dbCurse = self.conexao.cursor()
            self.dbCurse.execute(inserir, [nome, matricula, sexo, nascimento])
            self.conexao.commit()
            

            print('Cadastro realizado com sucesso!')

        except Exception as e:
            print(f'Falha em cadastrar o aluno!\nErro: {e}')

        finally:
            self.dbCurse.close()
            self.conexao.close()
    
    # corrigir e fazer alterações!
    def read (self):

        try:
            matricula = input('Informe a matrícula do aluno: ')

            consulta = 'SELECT * FROM  alunos WHERE matricula = ?;'
            self.conexao = sqlite.connect(self.dataBase)
            self.dbCurse = self.conexao.cursor()
            self.dbCurse.execute(consulta, [matricula])
            dados = self.dbCurse.fetchone()

            print(f'Aluno: {dados[1]},\nMatrícula: {dados[2]},\nSexo: {dados[3]}')

        except:
            print('Matrícula não encontrada no sistema!')

        finally:
            self.dbCurse.close()
            self.conexao.close()

    # corrigir e fazer alterações!
    def update (self):
        
        try:
            nome = input('Digite o nome do aluno: ')
            matricula = input('Digite a matrícula: ')
            sexo = input('Digite o sexo [ M / F ]: ')
            nascimento = input('Digite a data de nascimento (00/00/0000): ')

            atualizando = 'UPDATE alunos SET nome = ?, sexo = ?, nascimento = ? WHERE matricula = ?;'
            self.conexao = sqlite.connect(self.dataBase)
            self.dbCurse = self.conexao.cursor()
            self.dbCurse.execute(atualizando, [nome, sexo, nascimento, matricula])
            self.conexao.commit()
            print('Cadastro atualizado com sucesso!')

        except Exception as e:
            print(f'Não foi possível alterar/atualizar os dados do cadastro.\nErro: {e}')
            print(f'Desfazendo a última ação {e}')
            self.conexao.rollback()

        finally:
            self.dbCurse.close()
            self.conexao.close()

    def delete(self):

        try:
            matricula = input('Informe a matricula: ')

            excluir = 'DELETE FROM alunos WHERE matricula = ?;'
            self.conexao = sqlite.connect(self.dataBase)
            self.dbCurse = self.conexao.cursor()
            self.dbCurse.execute(excluir, [matricula])
            self.conexao.commit()
            print('O cadastro foi excluído com sucesso!')

        except Exception as e:
            print(f'Falha na exclusão do cadastro.\nErro: {e}')
            print(f'Desfazendo a última ação {e}')
            self.conexao.rollback()

        finally:
            self.dbCurse.close()
            self.conexao.close()

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

