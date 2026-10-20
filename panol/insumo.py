class Insumo:
    def __init__(self, codigo, nombre, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock

    def mostrar_datos(self):
        print("Código:", self.codigo, "| Insumo:", self.nombre, "| Stock:", self.stock)