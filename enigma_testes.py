# -*- coding: utf-8 -*-  
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
        
        # Verifica se a maquina eh capaz de decifrar
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
