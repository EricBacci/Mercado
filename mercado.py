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


class Order:
    """Modelagem dos pedidos"""
    def __init__(self, order_number, order_products=[], available_products=[]):
        """Inicializa o pedido com preço zerado"""
        self.order_number = order_number
        self.order_products = order_products
        self.total_price = 0
        
        for product_code in order_products:
            for product_dict in available_products:
                if product_code in product_dict:
                    self.total_price += product_dict[product_code]['price']
                    break

    def describe_order(self):
        print(f"Numero do pedido: {self.order_number}")
        print(f"Lista de itens: {self.order_products}")
        print(f"Preço do pedido: {self.total_price}")


"""Inicia as listas vazias"""
customer_list = []
available_products = []
order_list = []


"""Instanciando alguns produtos"""
product_leite = Product(1001, 'Leite', 4.50)
product_cafe = Product(1002, 'Cafe', 10)
product_banana = Product(1003, 'Banana', 9)

"""Criando um Order e mostrando o valor total"""
order_1 = Order(1001, [1001, 1002, 1003], available_products)
order_1.describe_order()

order_2 = Order(1002, [1001, 1001, 1001, 1001, 1001, 1001], available_products)
order_2.describe_order()

# """Instanciando alguns clientes"""
# customer_eric = Customer('Eric')
# customer_eduarda = Customer('Eduarda')
# customer_otavio = Customer('Otávio')

# """Realizando compras"""
# customer_eric.purchase(1001, 1002, 1003)
# customer_eric.purchase(1001)
# customer_eduarda.purchase(1001)
# customer_otavio.purchase(1002, 1003)

# """Mostrando dados finais de cada usuário"""
# customer_eric.describe_customer()
# customer_eduarda.describe_customer()
# customer_otavio.describe_customer()

# """Mostrando lista de itens"""
# print(available_products)
