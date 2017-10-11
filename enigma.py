# -*- coding: utf-8 -*-  

###############################################################
########################### ENIGMA ############################
###############################################################

tamanhoAlfabeto = 10
import random

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
        self.chaveOriginal = chave
        self.deslocamentoOriginal = deslocamento
        self.rotacionou = False
        return

    def setChave(k):
        self.chave = k
        return
    
    def rotacionarRotor(self):
        self.rotacionou = True
        self.deslocamento = (self.deslocamento + 1) % tamanhoAlfabeto

        # diminuindo 1
        #for i in range(len(self.chave)):
            #self.chave[i] = self.chave[i] - 1
            #if(self.chave[i] < 0):
            #    self.chave[i] = len(self.chave) - 1
        
        return

    def cifrar(self, simbolo, rotacionar=True):
        self.rotacionou = False
        newSymbol = (self.chave[(simbolo + self.deslocamento) % tamanhoAlfabeto] - self.deslocamento) % tamanhoAlfabeto
        # newSymbol = self.chave[(simbolo + self.deslocamento) % tamanhoAlfabeto]
        if (rotacionar):
            self.rotacionarRotor()
        return newSymbol

    def decifrar(self, simbolo, rotacionar=True):
        self.rotacionou = False
        newSymbol = (self.chave.index((simbolo + self.deslocamento) % tamanhoAlfabeto) - self.deslocamento) % tamanhoAlfabeto
        if(rotacionar):
            self.rotacionarRotor()
        return newSymbol

    def fechouCiclo(self):
        return self.rotacionou and self.deslocamento == 0

    def restaurar(self):
        self.deslocamento = self.deslocamentoOriginal
        self.chave = list(self.chaveOriginal)
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

        # Deve ser passado como parametro True ou False ?
        # por algum motivo, essa condicao abaixo tem que ser feita
        rotaciona = False
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


###############################################################
###################### TESTES DO ENIGMA #######################
###############################################################

import unittest

class EnigmaTest(unittest.TestCase):

    ##############################################
    # Verifica se o rotor é criado corretamente
    def test_rotor(self):
        r = Rotor([1,2,3,4,5])
        self.assertEqual(False, r.rotacionou)
        self.assertEqual([1,2,3,4,5], r.chave)

    ##############################################
    # Verifica se um rotor consegue cifrar corretamente
    def test_rotor_cypher(self):
        # Caso de Teste 1...
        r = Rotor([4, 2, 8, 0, 6, 5, 3, 1, 7, 9])
        textoCifrado = [4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0]
        textoPlano = [0 for x in range(len(textoCifrado))]
        # O Rotor cifra com sucesso o primeiro caractere?
        self.assertEqual(textoCifrado[0], r.cifrar(textoPlano[0]))
        # E o segundo?
        self.assertEqual(textoCifrado[1], r.cifrar(textoPlano[1]))
        # E o terceiro?
        self.assertEqual(textoCifrado[2], r.cifrar(textoPlano[2]))

        # O rotor consegue cifrar a palavra inteira?
        r.restaurar()
        textoCifrado2 = [r.cifrar(l) for l in textoPlano]
        self.assertEqual(textoCifrado, textoCifrado2)

        # O rotor consegue decifrar a palavra?
        r.restaurar()
        textoPlano2 = [r.decifrar(l) for l in textoCifrado]
        self.assertEqual(textoPlano, textoPlano2)

    ##############################################
    # Verifica se o Enigma é criado corretamente
    def test_enigma(self):
        e = Enigma(1)
        self.assertEqual(1, e.nRotores)
        self.assertEqual([], e.rotores)
        e.inserirRotor(Rotor([4, 2, 8, 0, 6, 5, 3, 1, 7, 9]))
        self.assertEqual([4, 2, 8, 0, 6, 5, 3, 1, 7, 9], e.rotores[0].chave)

    ##############################################
    # Verifica se a Maquina Enigma consegue cifrar corretamente com 1 rotor
    # Exemplo 1
    def test_enigma_cypher(self):
        e = Enigma(1)
        e.inserirRotor(Rotor([4, 2, 8, 0, 6, 5, 3, 1, 7, 9]))
        textoCifrado = [4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0, 4, 1, 6, 7, 2, 0, 7, 4, 9, 0]
        textoPlano = [0 for x in range(len(textoCifrado))]

        # Verifica se a maquina eh capaz de cifrar
        cifrado = [e.cifrar(l) for l in textoPlano]
        self.assertEqual(textoCifrado, cifrado)
        
        # Verifica se a maquina eh capaz de descifrar
        e.restaurar()
        decifrado = [e.decifrar(l) for l in textoCifrado]
        self.assertEqual(textoPlano, decifrado)

    ##############################################
    # Exemplo 2 (3 Enigmas Minimos)
    def test_enigma_minimo(self):
        e1 = Enigma(1)
        e2 = Enigma(1)
        e3 = Enigma(1)
        e1.inserirRotor(Rotor([9, 0, 6, 5, 4, 7, 2, 3, 8, 1], 0))
        e2.inserirRotor(Rotor([3, 2, 5, 0, 4, 6, 9, 7, 8, 1], 3))
        e3.inserirRotor(Rotor([4, 6, 0, 1, 7, 5, 2, 8, 9, 3], 3))
        textoClaro = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        textoClaro2 = [4, 3, 2, 1]

        textoCifrado1 = [9, 9, 4, 2, 0, 2, 6, 6, 0, 2, 9, 9, 4, 2, 0, 2, 6, 6, 0, 2, 9, 9, 4, 2, 0, 2, 6, 6, 0, 2, 9, 9, 4, 2, 0, 2, 6, 6, 0, 2, 9, 9, 4, 2, 0, 2, 6, 6, 0, 2, 9, 9, 4, 2, 0, 2, 6, 6, 0, 2, 9, 9, 4, 2, 0, 2, 6, 6, 0, 2, 9, 9, 4, 2, 0, 2, 6, 6, 0, 2, 9, 9, 4, 2, 0, 2, 6, 6, 0, 2, 9, 9, 4, 2, 0, 2, 6, 6, 0, 2]
        textoCifrado2 = [7, 0, 1, 3, 0, 0, 2, 3, 1, 3, 7, 0, 1, 3, 0, 0, 2, 3, 1, 3, 7, 0, 1, 3, 0, 0, 2, 3, 1, 3, 7, 0, 1, 3, 0, 0, 2, 3, 1, 3, 7, 0, 1, 3, 0, 0, 2, 3, 1, 3, 7, 0, 1, 3, 0, 0, 2, 3, 1, 3, 7, 0, 1, 3, 0, 0, 2, 3, 1, 3, 7, 0, 1, 3, 0, 0, 2, 3, 1, 3, 7, 0, 1, 3, 0, 0, 2, 3, 1, 3, 7, 0, 1, 3, 0, 0, 2, 3, 1, 3]
        textoCifrado3 = [5, 4, 3, 2]

        cifra1 = [e1.cifrar(l) for l in textoClaro]
        cifra2 = [e2.cifrar(l) for l in textoClaro]
        cifra3 = [e3.cifrar(l) for l in textoClaro2]

        self.assertEqual(textoCifrado1, cifra1)
        self.assertEqual(textoCifrado2, cifra2)
        self.assertEqual(textoCifrado3, cifra3)

    ##############################################
    # Verifica se a Maquina Enigma consegue cifrar com 3 rotores
    # Exemplo 3 (3 Rotores)
    def test_enigma_tres_rotores(self):
        textoPlano = [0,1,2,3,4]
        textoCifrado = [7, 3, 0, 6, 2]

        e = Enigma(3)
        e.inserirRotor(Rotor([5, 6, 1, 8, 2, 0, 7, 3, 4, 9], 5))
        e.inserirRotor(Rotor([9, 3, 8, 5, 0, 6, 1, 2, 4, 7], 3))
        e.inserirRotor(Rotor([7, 9, 5, 8, 0, 1, 2, 4, 3, 6], 4))
        cifra = [e.cifrar(l) for l in textoPlano]
        self.assertEqual(cifra, textoCifrado)

        # Testa se a maquina consegue decifrar corretamente com 3 rotores
        e.restaurar()
        decifra = [e.decifrar(l) for l in textoCifrado]
        self.assertEqual(decifra, textoPlano)
        

if __name__ == '__main__':
    unittest.main()
