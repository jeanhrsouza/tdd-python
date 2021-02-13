from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionado_em_ordem_crescente(self):
        # criando usuários
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')

        # propondo lances
        lance_do_yuri = Lance(yuri, 100.0)
        lance_do_gui = Lance(gui, 150.0)

        # criando leilao
        leilao = Leilao('Celular')

        # adicionando valores de lances no leilao
        leilao.lances.append(lance_do_yuri)
        leilao.lances.append(lance_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)


    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionado_em_ordem_decrescente(self):
        # criando usuários
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')

        # propondo lances
        lance_do_yuri = Lance(yuri, 100.0)
        lance_do_gui = Lance(gui, 150.0)

        # criando leilao
        leilao = Leilao('Celular')

        # adicionando valores de lances no leilao
        leilao.lances.append(lance_do_gui)
        leilao.lances.append(lance_do_yuri)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

