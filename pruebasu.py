class Mayor:
    def __init__(self) -> None:
        pass

    def mayor(self, numero1: int, numero2: int):
        result = None
        if numero1 > numero2:
            result = numero1
        elif numero2 > numero1:
            result = numero2
        return result

#Flask8 para mostrar errores de estilo
#Black para formatear codigo y dejarlo correcto