from models import Cliente, QuartoSolteiro, QuartoCasal, QuartoSuite, Reserva
from utils import limpar_tela, validar_data

def main():
    clientes = []
    quartos = [
        QuartoSolteiro(101),
        QuartoSolteiro(102),
        QuartoCasal(201),
        QuartoCasal(202),
        QuartoSuite(301)
    ]
    reservas = []
    id_reserva_contador = 1

    while True:
        print("\n=== SISTEMA DE RESERVAS DE HOTEL ===")
        print("1. Cadastrar Cliente")
        print("2. Listar Quartos Disponíveis")
        print("3. Realizar Reserva")
        print("4. Listar Reservas")
        print("5. Cancelar Reserva")
        print("6. Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            limpar_tela()
            print("--- CADASTRAR CLIENTE ---")
            nome = input("Nome completo: ")
            documento = input("CPF/Documento: ")
            contato = input("Telefone/Contato: ")
            
            cliente = Cliente(nome, documento, contato)
            clientes.append(cliente)
            print("\nCliente cadastrado com sucesso!")

        elif opcao == "2":
            limpar_tela()
            print("--- QUARTOS DO HOTEL ---")
            for q in quartos:
                status = "Disponível" if q.disponivel else "Ocupado"
                print(f"Quarto {q.numero} | Tipo: {q.tipo} | R$ {q.preco_base}/dia | Status: {status}")

        elif opcao == "3":
            limpar_tela()
            print("--- REALIZAR RESERVA ---")
            if not clientes:
                print("Erro: Você precisa cadastrar ao menos um cliente primeiro!")
                continue

            print("Clientes cadastrados:")
            for i, c in enumerate(clientes):
                print(f"{i}. {c.nome} (Doc: {c.documento})")
            
            try:
                c_idx = int(input("Escolha o número do cliente: "))
                cliente_escolhido = clientes[c_idx]
            except (ValueError, IndexError):
                print("Cliente inválido!")
                continue

            print("\nQuartos disponíveis:")
            disponiveis = [q for q in quartos if q.disponivel]
            if not disponiveis:
                print("Não há quartos disponíveis no momento.")
                continue

            for q in disponiveis:
                print(f"Quarto {q.numero} - {q.tipo} (R$ {q.preco_base})")

            try:
                num_quarto = int(input("Digite o número do quarto desejado: "))
                quarto_escolhido = next((q for q in disponiveis if q.numero == num_quarto), None)
                if not quarto_escolhido:
                    print("Quarto não encontrado ou indisponível.")
                    continue
            except ValueError:
                print("Entrada inválida!")
                continue

            d_entrada_str = input("Data de entrada (DD/MM/AAAA): ")
            d_saida_str = input("Data de saída (DD/MM/AAAA): ")

            data_entrada = validar_data(d_entrada_str)
            data_saida = validar_data(d_saida_str)

            if not data_entrada or not data_saida:
                print("Erro: Formato de data inválido! Use DD/MM/AAAA.")
                continue

            if data_saida <= data_entrada:
                print("Erro: A data de saída deve ser posterior à data de entrada!")
                continue

            nova_reserva = Reserva(id_reserva_contador, cliente_escolhido, quarto_escolhido, d_entrada_str, d_saida_str)
            reservas.append(nova_reserva)
            quarto_escolhido.disponivel = False
            id_reserva_contador += 1

            print(f"\nReserva #{nova_reserva.id_reserva} realizada com sucesso!")

        elif opcao == "4":
            limpar_tela()
            print("--- RESERVAS ATIVAS ---")
            if not reservas:
                print("Nenhuma reserva cadastrada.")
            else:
                for r in reservas:
                    print(r)

        elif opcao == "5":
            limpar_tela()
            print("--- CANCELAR RESERVA ---")
            if not reservas:
                print("Não há reservas para cancelar.")
                continue

            for r in reservas:
                print(f"ID: {r.id_reserva} | Hóspede: {r.cliente.nome} | Quarto: {r.quarto.numero}")

            try:
                id_canc = int(input("Digite o ID da reserva que deseja cancelar: "))
                reserva_encontrada = next((r for r in reservas if r.id_reserva == id_canc), None)
                
                if reserva_encontrada:
                    reserva_encontrada.quarto.disponivel = True
                    reservas.remove(reserva_encontrada)
                    print(f"Reserva #{id_canc} cancelada com sucesso e quarto liberado!")
                else:
                    print("Reserva não encontrada.")
            except ValueError:
                print("Por favor, digite um número válido.")

        elif opcao == "6":
            print("\nSaindo do sistema... Até mais!")
            break
        else:
            print("\nOpção inválida! Escolha entre 1 e 6.")

if __name__ == "__main__":
    main()
