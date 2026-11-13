class Cliente:
    def __init__(self, nome, documento, contato):
        self.nome = nome
        self.documento = documento
        self.contato = contato

    def __str__(self):
        return f"Cliente: {self.nome} | Doc: {self.documento} | Contato: {self.contato}"


class Quarto:
    def __init__(self, numero, tipo, preco_base):
        self.numero = numero
        self.tipo = tipo
        self.preco_base = preco_base
        self.disponivel = True

    def calcular_diaria(self):
        return self.preco_base


class QuartoSolteiro(Quarto):
    def __init__(self, numero):
        super().__init__(numero, "Solteiro", 100.0)


class QuartoCasal(Quarto):
    def __init__(self, numero):
        super().__init__(numero, "Casal", 180.0)


class QuartoSuite(Quarto):
    def __init__(self, numero):
        super().__init__(numero, "Suíte", 300.0)


class Reserva:
    def __init__(self, id_reserva, cliente, quarto, data_entrada, data_saida):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.quarto = quarto
        self.data_entrada = data_entrada
        self.data_saida = data_saida

    def __str__(self):
        return (f"Reserva #{self.id_reserva} | Hóspede: {self.cliente.nome} | "
                f"Quarto: {self.quarto.numero} ({self.quarto.tipo}) | "
                f"Período: {self.data_entrada} até {self.data_saida}")
