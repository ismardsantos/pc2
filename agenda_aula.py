class Menu():
    #opcao -> atributo
    #mostrar o menu -> metodo
    def __init__(self):
        self._opcao = None #atributo

    def getOpcao(self): #pega/retornar o valor do atributo
        return self._opcao

    def setOpcao(self, opcao): # atribuir um valor ao atributo
        self._opcao = opcao

    def mostrar(self):
        agenda = Agenda()
        while self.getOpcao() != "6":
            print("Selecione uma opção abaixo:")
            print("1 - Incluir contato")
            print("2 - Buscar contato")
            print("3 - Editar contato")
            print("4 - Excluir contato")
            print("5 - Listar contatos")
            print("6 - Sair do programa")

            self.setOpcao(input("Opção desejada: ")) #faca opcao = input do usuário

            if self.getOpcao() == "1": # qual é o valor de opcao?
                agenda.incluir()
            elif self.getOpcao() == "2":
                agenda.buscar()
            elif self.getOpcao() == "3":
                agenda.editar()
            elif self.getOpcao() == "4":
                agenda.excluir()
            elif self.getOpcao() == "5":
                agenda.listar()
            elif self.getOpcao() == "6":
                print("Bye bye :(")
            else:
                print("Opção inválida. Tente novamente!")

class Contato():
    def __init__(self, nome, email, telefone):
        self._nome = nome
        self._email = email
        self._telefone = telefone
    
    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    def getTelefone(self):
        return self._telefone

    def setTelefone(self, telefone):
        self._telefone = telefone

class Agenda():
    def __init__(self):
        self._agenda = [] #lista

    def getAgenda(self):
        return self._agenda

    def setAgenda(self, agenda):
        self._agenda = agenda

    def incluir(self):
        nome = input("Digite o NOME: ")
        email = input("Digite o EMAIL: ")
        telefone = input("Digite o TELEFONE: ")

        contato = Contato(nome, email, telefone)

        self.getAgenda().append(contato)

    def buscar(self):
        termoBusca = input("Digite o que você quer buscar: ")
        for i, contato in enumerate(self.getAgenda()):
            #find(str) -> retorna a posição de str ou -1 caso não ache
            #Fabricio
            #.find("fabricio")

            #nome = "Fabricio Araujo"
            #posicao = nome.find(almeida)
            #posicao = 2
            #posicao = -1

            #nome = -1
            #email = -1
            #telefone = -1
            #total = -3

            total = contato.getNome().find(termoBusca) 
            total = total + contato.getEmail().find(termoBusca) 
            total += contato.getTelefone().find(termoBusca)

            #-3, -2, -1, 0 .......

            if total > -3:
                print("Contato ", i)
                print("Nome: "+contato.getNome())
                print("Email: "+contato.getEmail())
                print("Telefone: "+contato.getTelefone())

    def editar(self):
        print("Escolha um dos contatos da agenda para editar:")
        self.listar()
        i_contato = int(input("ID do contato: "))
        novoNome = input("Digite o NOVO NOME: ")
        novoEmail = input("Digite o NOVO EMAIL: ")
        novoTelefone = input("Digite o NOVO TELEFONE: ")

        if novoNome != "":
            self.getAgenda()[i_contato].setNome(novoNome)

        if novoEmail != "":
            self.getAgenda()[i_contato].setEmail(novoEmail)

        if novoTelefone != "":
            self.getAgenda()[i_contato].setTelefone(novoTelefone)

    def excluir(self):
        print("Escolha um dos contatos da agenda para excluir:")
        self.listar()
        i_contato = int(input("ID do contato: "))

        del self.getAgenda()[i_contato]
        #frutas = ["pera", "uva", "banana"]
        #del frutas[1]
        #frutas = ["pera", "banana"]

    def listar(self):
        #for key, value in d.items(): dicionario
        for i, contato in enumerate(self.getAgenda()): #lista
            print("Contato ", i)
            print("Nome: "+contato.getNome())
            print("Email: "+contato.getEmail())
            print("Telefone: "+contato.getTelefone())

#Execução
menuAplicacao = Menu() #criando um objeto da classe menu
menuAplicacao.mostrar() #chamando o metodo mostrar da classe