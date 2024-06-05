def show_main_menu() -> int:
    print("\n1. Registrar")
    print("2. Autenticar")
    print("3. Parar execucao do programa")
    option = int(input("Escolha uma opção: "))
    return option


def show_authenticated_menu():
    print("\nBem-vindo!")
    print("1. Visualizar carros")
    print("2. Fazer pedido")
    print("3. Visualizar carro por ID")
    print("4. Logout")
    option = int(input("Escolha uma opção: "))
    return option


def show_shopping_cart_menu():
    print("\n1. Adicionar item ao carrinho")
    print("2. Remover item do carrinho")
    print("3. Visualizar carrinho")
    print("4. Visualizar todos os pedidos finalizados")
    print("5. Visualizar o último pedido finalizado")
    print("6. Finalizar compra")
    print("7. Cancelar compra")
    print("8. Voltar ao menu principal")
    option = int(input("Escolha uma opção: "))
    return option


def show_admin_menu():
    print("\n1. Registrar novo carro")
    print("2. Visualizar todos os carros")
    print("3. Visualizar carro por ID")
    print("4. Deletar carro por ID")
    print("5. Editar carro por ID")
    print("6. Sair")
    option = int(input("Escolha uma opção: "))
    return option
