
# Analizador semántico: verifica reglas semánticas específicas durante el análisis sintáctico
class AnalizadorSemantico:
    def __init__(self):
        pass

    def verificar_division_por_cero(self, divisor):
        if divisor == 0:
            raise Exception("Error semántico. División por cero.")

    def verificar_raiz_cuadrada(self, radicando):
        if radicando < 0:
            raise Exception("Error semántico. No se puede calcular la raíz cuadrada de un número negativo.")

    def verificar_argumento_trigonometrico(self, argumento):
        # Puedes agregar lógica adicional según tus requisitos para verificar el argumento trigonométrico.
        pass