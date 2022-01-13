#PAME 21.2 - ENTREGA 2 - IANA KAROLINA DA SILVA REIS

global listaOnibus
listaOnibus=[]

global listaParada
listaParada=[]

global listaMotorista
listaMotorista=[]

global listaFiscal
listaFiscal=[]

global lista_auxiliar_2
lista_auxiliar_2=[] #A lista dos motoristas já adicionados

global lista_auxiliar_3
lista_auxiliar_3=[] #A lista dos fiscais já adicionados

global listaRotas
listaRotas=[]

class Onibus:
    def __init__(self,placa,frota,Moto=None,Fis=None, rota=[]):
        self.placa=placa
        self.frota=frota
        self.Moto=Moto
        self.Fis=Fis
        self.rota=[]
        
    @classmethod
    def mostrar(self):
        """Função que mostra todas as informações de todos os ônibus."""
        global listaOnibus
        for onibus in listaOnibus:
                print(f"\n placa={onibus.placa} \
                     \n frota={onibus.frota} \
                     \n motorista={onibus.Moto} \
                     \n fiscal={onibus.Fis} \
                     \n rota={onibus.rota} \
                     \n tarifa={round(1.20+len(onibus.rota)*1.20,2)} reais") #1.2 reais é a tarifa fixa

    def mostrar_rota(self):
        """Função que mostra todas as rotas criadas."""
        global listaOnibus
        for onibus in listaOnibus:
            print(f"{onibus.rota}")
        
    
    @classmethod
    def alterar(self):
        """Função que altera as informações do ônibus."""
        print(f"Informações dos ônibus disponíveis para alteração: \
              \n 1-placa \
              \n 2-frota")
        info=input("Insira o número correspondente à informação que deseja alterar: ")
        global listaOnibus
        lista_auxiliar_placa=[]
        lista_auxiliar_frota=[]
        
        if info=='1':
            placa_antiga=input("Por favor, insira o número da placa que deseja alterar: ")
            self.placa=input("Digite a nova placa: ")
            for i in range(len(listaOnibus)):
                lista_auxiliar_placa.append(listaOnibus[i].placa)

            indica=lista_auxiliar_placa.index(placa_antiga)
            listaOnibus[indica].placa=self.placa
            return listaOnibus
            
        if info=='2':
            frota_antiga=input("Por favor, insira o número da frota que deseja alterar: ")
            self.frota=input("Digite a nova frota: ")
            for i in range(len(listaOnibus)):
                lista_auxiliar_frota.append(listaOnibus[i].frota)

            indica=lista_auxiliar_frota.index(placa_antiga)
            listaOnibus[indica].placa=self.placa
            return listaOnibus
        
      
    @classmethod
    def deletar(self):
        """Função que deleta o ônibus desejado."""
        global listaOnibus
        lista_auxiliar_placa=[]
        placa=input("Insira a placa do ônibus que deseja deletar: ")
        for i in range(len(listaOnibus)):
            lista_auxiliar_placa.append(listaOnibus[i].placa)

        indica=lista_auxiliar_placa.index(placa)
        del listaOnibus[indica]
        return listaOnibus
    
    
    @classmethod
    def assignar_motorista(self):
        """Função que assigna o motorista ao ônibus."""
        global listaOnibus
        global listaMotorista
        lista_auxiliar_moto=[] #A lista dos nomes de todos os motoristas
        global lista_auxiliar_2  #A lista dos motoristas já adicionados
        lista_auxiliar_placa=[] #A lista de todas as placas do onibus
        nomeMoto=input("Insira o nome do motorista: ")
        placa=input("Insira a placa do ônibus ao qual deseja associar o motorista: ")
        
        for i in range(len(listaMotorista)):
            lista_auxiliar_moto.append(listaMotorista[i].nome)

        for i in range(len(listaOnibus)):
            lista_auxiliar_placa.append(listaOnibus[i].placa)

        indice_motorista=lista_auxiliar_moto.index(nomeMoto) #Acho o indice do nome dado pelo usuario na lista de nomes de motorista cadastrada
        self.Moto=listaMotorista[indice_motorista].nome

        indice_placa=lista_auxiliar_placa.index(placa) #Acho o indice da placa do onibus dada pelo usuario na lista de placas de onibus cadastradas

        if listaOnibus[indice_placa].Moto== None: #Se o parametro Moto da classe Onibus for None
            if nomeMoto not in lista_auxiliar_2:
                listaOnibus[indice_placa].Moto = self.Moto #Eu adiciono, na minha classe Onibus.Moto(), no indice da placa, o nome dado pelo usuario
                lista_auxiliar_2.append(nomeMoto)
            else:
                print("Esse motorista já está escalado em outro ônibus. Por favor, escolha outra pessoa.")
        else:
            print("Esse ônibus já possui um motorista!")
        return listaOnibus,listaMotorista
    
    @classmethod
    def assignar_fiscal(self):
        """Função que assigna o fiscal ao ônibus."""
        global listaOnibus
        global listaFiscal
        lista_auxiliar_fis=[] #A lista dos nomes de todos os motoristas
        global lista_auxiliar_3  #A lista dos motoristas já adicionados
        lista_auxiliar_placa=[] #A lista de todas as placas do onibus
        nomeFis=input("Insira o nome do fiscal: ")
        placa=input("Insira a placa do ônibus ao qual deseja associar o motorista: ")
        
        for i in range(len(listaFiscal)):
            lista_auxiliar_fis.append(listaFiscal[i].nome)

        for i in range(len(listaOnibus)):
            lista_auxiliar_placa.append(listaOnibus[i].placa)

        indice_fiscal=lista_auxiliar_fis.index(nomeFis) #Acho o indice do nome dado pelo usuario na lista de nomes de fiscais cadastrada
        self.Fis=listaFiscal[indice_fiscal].nome

        indice_placa=lista_auxiliar_placa.index(placa) #Acho o indice da placa do onibus dada pelo usuario na lista de placas de onibus cadastradas

        if listaOnibus[indice_placa].Fis== None: #Se o parametro Moto da classe Onibus for None
            if nomeFis not in lista_auxiliar_3:
                listaOnibus[indice_placa].Fis = self.Fis #Eu adiciono, na minha classe Onibus.Moto(), no indice da placa, o nome dado pelo usuario
                lista_auxiliar_3.append(nomeFis)
            else:
                print("Esse fiscal já está escalado em outro ônibus. Por favor, escolha outra pessoa.")
        else:
            print("Esse ônibus já possui um fiscal!")
        return listaOnibus,listaMotorista


    def adicionar_parada(self):
        """Função que adiciona ponto de parada ao ônibus."""
        global listaOnibus
        global listaParada
        global listaRotas
        lista_auxiliar_cep=[] #A lista dos ceps de todas as paradas
        lista_auxiliar_placa=[] #A lista de todas as placas do onibus
        
        cep=input("Insira o cep do ponto de parada que deseja adicionar: ")
        placa=input("Insira a placa do ônibus ao qual deseja adicionar o ponto de parada: ")

        #1- Cria lista de todos os ceps dos pontos de parada adicionados no sistema
        for i in range(len(listaParada)): 
            lista_auxiliar_cep.append(listaParada[i].cep)

        #2- Cria lista de todas as placas de todos os onibus adicionados no sistema
        for i in range(len(listaOnibus)): 
            lista_auxiliar_placa.append(listaOnibus[i].placa)


        #3- Acho o indice da placa dada pelo usuario na lista de placas cadastradas no sistema
        indice_placa=lista_auxiliar_placa.index(placa)
        
        #4- Acho o indice do cep dado pelo usuario na lista de ceps cadastrados no sistema
        if cep not in lista_auxiliar_cep:
            print("Esse cep não está cadastrado no sistema. Por favor, tente novamente.")
        else:
            indice_cep=lista_auxiliar_cep.index(cep)
            if cep in listaOnibus[indice_placa].rota:
                print("Esse ônibus já faz parada nesse ponto!")
            else:
                indice_placa=lista_auxiliar_placa.index(placa)
                listaOnibus[indice_placa].rota.append(cep)

        return listaOnibus,listaParada,listaRotas
            

    def alterar_rota(self):
        """Função que altera a rota do ônibus."""
        global listaOnibus
        global listaParada
        lista_auxiliar_rota=[]
        lista_auxiliar_placa=[]
        onibus_antigo=input("Por favor, insira o número da placa do ônibus que deseja alterar a rota: ")
        cep_antigo=input("Digite o cep que deseja alterar: ")
        cep_novo=input("Digite o novo cep: ")

        #cada instância ônibus
        for onibus in listaOnibus:
            lista_auxiliar_placa.append(onibus.placa)

        indica_placa=lista_auxiliar_placa.index(onibus_antigo)#Aqui eu pego o index do onibus inserido pelo usuario
            
        for elementos in listaOnibus[indica_placa].rota: #cep é cada elemento, literalmente, cada cep
            lista_auxiliar_rota.append(elementos)

        indica=lista_auxiliar_rota.index(cep_antigo)
        listaOnibus[indica_placa].rota[indica]=cep_novo
        listaParada[indica].cep=cep_novo
                
        return listaOnibus,listaParada
        

class Paradas:
    def __init__(self,cep):
        self.cep = cep
        
    @classmethod
    def alterar(self):
        """Função que altera o ponto de parada."""
        global listaParada
        print(f"Informações dos pontos de parada disponíveis para alteração : \
              \n 1-cep")
        info=input("Insira o número correspondente à informação que deseja alterar: ")
        lista_auxiliar_cep=[]
        
        if info=='1':
            cep_antigo=input("Por favor, insira o número do cep que deseja alterar: ")
            self.cep=input("Digite o novo cep: ")
            for i in range(len(listaParada)):
                lista_auxiliar_cep.append(listaParada[i].cep)

            indica=lista_auxiliar_cep.index(cep_antigo)
            listaParada[indica].cep=self.cep
            return listaParada

    @classmethod
    def deletar(self):
        """Função que deleta o ponto de parada desejado."""
        global listaParada
        lista_auxiliar_cep=[]
        cep=input("Insira o cep do ponto de parada que deseja deletar: ")
        for i in range(len(listaParada)):
            lista_auxiliar_cep.append(listaParada[i].cep)

        indica=lista_auxiliar_cep.index(cep)
        del listaParada[indica]
        return listaParada

class Motorista:

    def __init__(self,nome,idade,carteiratrabalho):
        self.nome=nome
        self.idade=idade
        self.carteiratrabalho=carteiratrabalho

    @classmethod
    def mostrar(self):
        """Função que mostra as informações de todos os motoristas
        registrados no sistema."""
        global listaMotorista
        for i in range(len(listaMotorista)):
                print(f"Informações do motorista {i}: \
                     \n nome={listaMotorista[i].nome} \
                     \n idade={listaMotorista[i].idade} \
                     \n carteira de trabalho={listaMotorista[i].carteiratrabalho}")

    @classmethod
    def alterar(self):
        """Função que altera as informações do motorista"""
        print(f"Informações do motorista disponíveis para alteração: \
              \n 1-nome \
              \n 2-idade \
              \n 3-carteira de trabalho")
        info=input("Insira o número correspondente à informação que deseja alterar: ")
        global listaMotorista
        lista_auxiliar_nome=[]
        lista_auxiliar_idade=[]
        lista_auxiliar_carteiratrabalho=[]
        
        if info=='1':
            nome_antigo=input("Por favor, insira o nome anterior: ")
            self.nome=input("Digite o novo nome: ")
            for i in range(len(listaMotorista)):
                lista_auxiliar_nome.append(listaMotorista[i].nome)
            
            indice=lista_auxiliar_nome.index(nome_antigo)
            listaMotorista[indice].nome=self.nome
            return listaMotorista
        
        if info=='2':
            idade_antiga=input("Por favor, insira a idade anterior: ")
            self.idade=input("Digite a nova idade: ")
            for i in range(len(listaMotorista)):
                lista_auxiliar_idade.append(listaMotorista[i].idade)
                
            indice=lista_auxiliar_idade.index(idade_antiga)
            listaMotorista[indice].idade=self.idade
            return listaMotorista

        if info=='3':
            carteira_antiga=input("Por favor, insira o número da carteira de trabalho anterior: ")
            self.carteiratrabalho=input("Digite a nova idade: ")
            for i in range(len(listaMotorista)):
                lista_auxiliar_carteiratrabalho.append(listaMotorista[i].carteiratrabalho)

            indice=lista_auxiliar_carteiratrabalho.index(carteira_antiga)
            listaMotorista[indice].carteiratrabalho=self.carteiratrabalho
            return listaMotorista

    @classmethod
    def deletar(self):
        """Função que deleta o motorista desejado."""
        global listaMotorista
        lista_auxiliar_nome=[]
        nome=input("Insira o nome do motorista que deseja deletar: ")
        for i in range(len(listaMotorista)):
            lista_auxiliar_nome.append(listaMotorista[i].nome)

        indica=lista_auxiliar_nome.index(nome)
        del listaMotorista[indica]
        return listaMotorista
        
        
class Fiscal:

    def __init__(self,nome,idade,carteiratrabalho):
        self.nome=nome
        self.idade=idade
        self.carteiratrabalho=carteiratrabalho
        

    @classmethod
    def mostrar(self):
        """Função que mostra todas as informações dos fiscais
        cadastrados no sistema."""
        global listaFiscal
        for i in range(len(listaFiscal)):
                print(f"Informações do fiscal {i}: \
                     \n nome={listaFiscal[i].nome} \
                     \n idade={listaFiscal[i].idade} \
                     \n carteira de trabalho={listaFiscal[i].carteiratrabalho}")

    @classmethod
    def alterar(self):
        """Função que altera a informação do fiscal desejado."""
        print(f"Informações do fiscal disponíveis para alteração: \
              \n 1-nome \
              \n 2-idade \
              \n 3-carteira de trabalho")
        info=input("Insira o número correspondente à informação que deseja alterar: ")
        global listaFiscal
        lista_auxiliar_nome=[]
        lista_auxiliar_idade=[]
        lista_auxiliar_carteiratrabalho=[]
        
        if info=='1':
            nome_antigo=input("Por favor, insira o nome anterior: ")
            self.nome=input("Digite o novo nome: ")
            for i in range(len(listaFiscal)):
                lista_auxiliar_nome.append(listaFiscal[i].nome)
                

            indice=lista_auxiliar_nome.index(nome_antigo)
            listaFiscal[indice].nome=self.nome
            return listaFiscal
        
        if info=='2':
            idade_antiga=input("Por favor, insira a idade anterior: ")
            self.idade=input("Digite a nova idade: ")
            for i in range(len(listaFiscal)):
                lista_auxiliar_idade.append(listaFiscal[i].idade)
                
            indice=lista_auxiliar_idade.index(idade_antiga)
            listaFiscal[indice].idade=self.idade
            return listaFiscal

        if info=='3':
            carteira_antiga=input("Por favor, insira o número da carteira de trabalho anterior: ")
            self.carteiratrabalho=input("Digite a nova idade: ")
            for i in range(len(listaFiscal)):
                lista_auxiliar_carteiratrabalho.append(listaFiscal[i].carteiratrabalho)
                
            indice=lista_auxiliar_carteiratrabalho.index(carteira_antiga)
            listaFiscal[indice].carteiratrabalho=self.carteiratrabalho
            return listaFiscal

    @classmethod
    def deletar(self):
        """Função que deleta o fiscal desejado."""
        global listaFiscal
        lista_auxiliar_nome=[]
        nome=input("Insira o nome do fiscal que deseja deletar: ")
        for i in range(len(listaFiscal)):
            lista_auxiliar_nome.append(listaFiscal[i].nome)

        indica=lista_auxiliar_nome.index(nome)
        del listaFiscal[indica]
        return listaFiscal
   

def menu():
    """Função que contém o chamado para todas as outras
    funções do programa."""
    print(f"Olá, seja bem-vindx ao sistema de gerenciamento FluxoManager! Seguem as funcionalidades do nosso sistema: \
          \n 1- Criar ônibus \
          \n 2- Criar ponto de parada \
          \n 3- Criar motorista \
          \n 4- Criar fiscal \
          \n 5- Mostrar ônibus \
          \n 6- Mostrar rotas \
          \n 7- Mostrar motoristas \
          \n 8- Mostrar fiscais \
          \n 9- Assignar motorista ao ônibus \
          \n 10- Assignar fiscal ao ônibus \
          \n 11- Adicionar ponto de parada ao ônibus \
          \n 12- Alterar dados do ônibus \
          \n 13- Alterar dados da parada \
          \n 14- Alterar dados do motorista \
          \n 15- Alterar dados do fiscal \
          \n 16- Alterar rota do ônibus \
          \n 17- Deletar ônibus \
          \n 18- Deletar ponto de parada \
          \n 19- Deletar motorista \
          \n 20- Deletar fiscal \
          \n 21- Sair do programa")
    cont='s'
    
    while cont=='s':
        ans=input(f"\nPor favor, insira o número correspondente à funcionalidade desejada: ")
        if ans=='1':
            placa=input("Digite o numero da placa: ")
            frota=input("Digite o numero da frota: ")
            oni=Onibus(placa,frota)
            listaOnibus.append(oni)
            
        if ans=='2':
            cep=input("Insira o cep do ponto de parada: ")
            Parada=Paradas(cep)
            listaParada.append(Parada)
            
        if ans=='3':
            nome=input("Insira o nome do motorista: ")
            idade=input("Insira a idade do motorista: ")
            carteiradetrabalho=input("Insira o número da carteira de trabalho do motorista: ")
            Moto=Motorista(nome,idade,carteiradetrabalho)
            listaMotorista.append(Moto)
            
        if ans=='4':
            nome=input("Insira o nome do fiscal: ")
            idade=input("Insira a idade do fiscal: ")
            carteiradetrabalho=input("Insira o número da carteira de trabalho do fiscal: ")
            Fis=Fiscal(nome,idade,carteiradetrabalho)
            listaFiscal.append(Fis)
            
        if ans=='5': #MOSTRAR ONIBUS
            Onibus.mostrar()
            
        if ans=='6': #MOSTRAR ROTAS
            oni.mostrar_rota()
            
        if ans=='7': #MOSTRAR MOTORISTAS
            Motorista.mostrar()
            
        if ans=='8': #MOSTRAR FISCAIS
            Fiscal.mostrar()
        
        if ans=='9': #ASSIGNAR MOTORISTA AO ONIBUS
            Onibus.assignar_motorista()
            
        if ans=='10': #ASSIGNAR FISCAL AO ONIBUS
            Onibus.assignar_fiscal()
        
        if ans=='11': #ADICIONAR PONTO DE PARADA AO ONIBUS
            oni.adicionar_parada()
    
        if ans=='12': #ALTERAR DADOS DO ONIBUS
            Onibus.alterar()
            
        if ans=='13': #ALTERAR DADOS DA PARADA
            Parada.alterar()

        if ans=='14': #ALTERAR DADOS DO MOTORISTA
            Motorista.alterar()

        if ans=='15': #ALTERAR DADOS DO FISCAL 
            Fiscal.alterar()

        if ans=='16': #ALTERAR ROTA DO ONIBUS 
            oni.alterar_rota()   

        if ans=='17': #DELETAR ONIBUS
            if listaOnibus==[]:
                print("Não há mais ônibus registrados no sistema.")
            else:
                Onibus.deletar()    

        if ans=='18': #DELETAR PONTO DE PARADA
            if listaParada==[]:
                print("Não há mais pontos de paradas registrados no sistema.")
            else:
                Parada.deletar()  

        if ans=='19': #DELETAR MOTORISTA
            if listaMotorista==[]:
                print("Não há mais motoristas registrados no sistema.")
            else:
                Motorista.deletar() 

        if ans=='20': #DELETAR FISCAL
            if listaFiscal==[]:
                print("Não há mais fiscais registrados no sistema.")
            else:
                Fiscal.deletar() 

        if ans=='21': #SAIR DO PROGRAMA
            break

        cont=input(f"\nDeseja escolher outra funcionalidade?s/n ")

menu() 


