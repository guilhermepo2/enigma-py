# -*- coding: utf-8 -*-  

###############################################################
########################### ENIGMA ############################
###############################################################

tamanhoAlfabeto = 10

###########################################################################
# Classe Rotor
# Atributos:
#   - chave => descreve a configuração do rotor do enigma
#   - deslocamento => deslocamento do rotor em relação a sua posição original
#   - deslocamentoOriginal => armazena o deslocamento Original
#   - rotacionou => verifica se o rotor executou ou não uma rotação
# Métodos:
#   - init: Inicializa um Rotor
#       - @param chave => inicialização da chave
#       - @param deslocamento => inicialização do deslocamento
#   - setChave: Atribui um valor à chave
#       - @param k => chave a ser atribuida
#   - rotacionarRotor: Aplica a rotação à direita no rotor
#   - cifrar: aplica o processo de ciframento a um simbolo e rotaciona ou não
#       - @param simbolo => simbolo a ser cifrado
#       - @param rotacionar => se deve rotacionar ou não
#   - decifrar: Aplica o processo de deciframento em um simbolo e rotaciona ou não
#      - @param simbolo => simbolo a ser decifrado
#      - @param rotacionar => se deve rotacionar ou não
#   - fechouCiclo: verifica se um rotor girou até retornar ao seu início
#   - restaurar: restaura o deslocamento original do rotor
###########################################################################
class Rotor:
    def __init__(self, chave, deslocamento=0):
        self.chave = chave
        self.deslocamento = deslocamento
        self.deslocamentoOriginal = deslocamento
        self.rotacionou = False
        return

    def setChave(k):
        self.chave = k
        return
        
    def rotacionarRotor(self):
        self.rotacionou = True
        self.deslocamento = (self.deslocamento + 1) % tamanhoAlfabeto
        return

    def cifrar(self, simbolo, rotacionar=True):
        self.rotacionou = False

        indiceChave = (simbolo + self.deslocamento) % tamanhoAlfabeto
        newSymbol = (self.chave[indiceChave] - self.deslocamento) % tamanhoAlfabeto
        
        if (rotacionar):
            self.rotacionarRotor()
        return newSymbol

    def decifrar(self, simbolo, rotacionar=True):
        self.rotacionou = False

        indiceProcurado = (simbolo + self.deslocamento) % tamanhoAlfabeto
        newSymbol = (self.chave.index(indiceProcurado) - self.deslocamento) % tamanhoAlfabeto
        if(rotacionar):
            self.rotacionarRotor()
        return newSymbol

    def fechouCiclo(self):
        return self.rotacionou and self.deslocamento == 0

    def restaurar(self):
        self.deslocamento = self.deslocamentoOriginal
        return
        

###########################################################################
# Classe Enigma
# Atributos:
#   - nRotores => quantidade de Rotores que o enigma tem
#   - rotores  => referência aos rotores
# Métodos:
#   - init: Inicializa a maquina enigma
#       - @param nRotores => quantidade de rotores
#   - pushRotor: Insere um rotor na maquina
#       - @param r        => rotor a ser inserido
#   - cifrar: cifra um simbolo e aplicação a rotação aos rotores
#       - @param s => simbolo a ser cifrado
#    - decifrar: decifra um simbolo e aplica a rotação nos rotores
#       - @param s => símbolo a ser decifrado
#    - restaurar: restaura todos os rotores aos seus deslocamentos originais
###########################################################################
class Enigma:
    def __init__(self, nRotores):
        self.nRotores = nRotores
        self.rotores = []
        return

    def inserirRotor(self, r):
        self.rotores.append(r)
        return
    
    def cifrar(self, s):
        simboloCifrado = ""
        simboloCifrado = self.rotores[0].cifrar(s)
        for i in range(1, len(self.rotores)):
            simboloCifrado = self.rotores[i].cifrar(simboloCifrado, self.rotores[i-1].fechouCiclo())
        return simboloCifrado

    def decifrar(self, s):
        rotaciona = False
        # por algum motivo, essa condicao abaixo tem que ser feita
        if(self.nRotores == 1):
            rotaciona = True
        # # # # # # # # # # # # #
        
        simboloDecifrado = self.rotores[self.nRotores - 1].decifrar(s, rotaciona)
        
        for i in range(self.nRotores - 2, -1, -1):
            simboloDecifrado = self.rotores[i].decifrar(simboloDecifrado, i == 0)
            
        for i in range(1, self.nRotores):
            if(self.rotores[i-1].fechouCiclo()):
                self.rotores[i].rotacionarRotor()
        return simboloDecifrado

    def restaurar(self):
        for i in range(0, self.nRotores):
            self.rotores[i].restaurar()
        return

# Função Testar Enigma
#   @param rotores => vetor de rotores a serem inseridas no enigma
#   @param textoPlano => texto a ser cifrado
#
# A função executa o ciframento do texto plano e o deciframento da mensagem gerada
# para verificar se a maquina enigma realmente funciona. Os dois resultados são im-
# pressos na tela.
def testarEnigma(rotores, textoPlano):
    enigma = Enigma(len(rotoresTeste))
    for i in range(len(rotoresTeste)):
        enigma.inserirRotor(rotoresTeste[i])
    
    textoCifrado = [enigma.cifrar(l) for l in textoPlano]
    enigma.restaurar()
    textoDecifrado = [enigma.decifrar(l) for l in textoCifrado]

    print "==================================================="
    print "EXECUÇÃO MÁQUINA ENIGMA"
    print "Quantidade de Rotores: " + str(len(rotores))
    print "Rotor(es): "
    for i in range(len(rotores)):
        print "Rotor " + str(i+1) + ": " + str(rotores[i].chave) + " - Deslocamento: " + str(rotores[i].deslocamento)
    print "Texto Plano"
    print textoPlano
    print "Texto Cifrado pelo Enigma"
    print textoCifrado
    print "Texto Decifrado pelo Enigma"
    print textoDecifrado
    print "==================================================="
    
execfile("./enigma_testes.py")
if __name__ == '__main__':
    # Exemplo 1 (Primeiro Exemplo)
    rotoresTeste = [Rotor([4, 2, 8, 0, 6, 5, 3, 1, 7, 9], 0)]
    textoPlano = [0 for x in range(100)]
    # Chamada da Função que executa o Enigma
    # testarEnigma(rotoresTeste, textoPlano)
    
    # Exemplo 2 (Enigma Minimo 1)
    rotoresTeste = [Rotor([9, 0, 6, 5, 4, 7, 2, 3, 8, 1], 0)]
    textoPlano = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # testarEnigma(rotoresTeste, textoPlano)
    
    # Exemplo 3 (Enigma Minimo 2)
    rotoresTeste = [Rotor([3, 2, 5, 0, 4, 6, 9, 7, 8, 1], 3)]
    textoPlano = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # testarEnigma(rotoresTeste, textoPlano)
    
    # Exemplo 4 (Enigma Minimo 3)
    rotoresTeste = [Rotor([4, 6, 0, 1, 7, 5, 2, 8, 9, 3], 3)]
    textoPlano = [4, 3, 2, 1]
    # testarEnigma(rotoresTeste, textoPlano)

    # Exemplo 5 (Enigma com 3 Rotores)
    rotoresTeste = [Rotor([5, 6, 1, 8, 2, 0, 7, 3, 4, 9], 5), Rotor([9, 3, 8, 5, 0, 6, 1, 2, 4, 7], 3), Rotor([7, 9, 5, 8, 0, 1, 2, 4, 3, 6], 4)]
    textoPlano = [0,1,2,3,4]
    testarEnigma(rotoresTeste, textoPlano)

    # Executar Testes
    print
    print "Executando testes..."
    unittest.main()
