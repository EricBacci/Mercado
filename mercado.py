"""
Tenta fazer uma aplicação simples, que tem as entidades Usuário, Compra, Produtos, 
cada usuário tem N compra, que tem X valor e possui X produtos
E o usuário tem o método de fazer compra
Onde cria uma transação nele
"""

class Customer:
    """Modelagem dos clientes"""
    
    def __init__(self, name):
        """Inicializa o cliente com listas e valores vazios e add na lista de controle"""
        self.name = name
        self.purchase_qty = 0
        self.products = []
        self.total_price = 0

        customer_list.append(self.name) # Add em lista de controle

    def describe_customer(self):
        """Funcao para descrever o cliente"""
        print(f"Nome do cliente: {self.name}")
        print(f"Itens comprados: {self.products}")
        print(f"Compras efetuadas: {self.purchase_qty}")
    
    def purchase(self, *args):
        """Funcao para efetuar compras (ate aqui, somente contagem de itens e att lista com itens)"""
        for arg in args:
            self.products.append(arg)
        self.purchase_qty += 1


class Product:
    """Modelagem dos produtos"""

    def __init__(self, product_code, product_name, price):
        """Inicializa o produto e add na lista de controle"""
        self.product_code = product_code
        self.product_name = product_name
        self.price = price

        available_products.append({
            self.product_code: {
                'name': product_name,
                'price': price,
            }
        })


"""Listas iniciais vazias"""
available_products = []
customer_list = []

"""Instanciando alguns produtos"""
product_leite = Product(1001, 'Leite', 4.50)
product_cafe = Product(1002, 'Cafe', 10)
product_banana = Product(1003, 'Banana', 9)

"""Instanciando alguns clientes"""
customer_eric = Customer('Eric')
customer_eduarda = Customer('Eduarda')
customer_otavio = Customer('Otávio')

"""Realizando compras"""
customer_eric.purchase(1001, 1002, 1003)
customer_eric.purchase(1001)
customer_eduarda.purchase(1001)
customer_otavio.purchase(1002, 1003)

"""Mostrando dados finais de cada usuário"""
customer_eric.describe_customer()
customer_eduarda.describe_customer()
customer_otavio.describe_customer()
