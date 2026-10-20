from panol.insumo import Insumo

class HerramientaElectrica(Insumo):
    def __init__(self, codigo, nombre, stock, potencia):
        Insumo.__init__(self, codigo, nombre, stock)
        self.potencia = potencia

    def verificar_consumo(self):
        if self.potencia > 1500:
            print("  -> Alerta: Equipo de alto consumo eléctrico (>1500W).")
        else:
            print("  -> Consumo estándar de taller.")