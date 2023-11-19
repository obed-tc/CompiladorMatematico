import math  # Importa el módulo math para funciones matemáticas avanzadas
class AnalizadorSintactico:
    def __init__(self, analizador_lexico, analizador_semantico):
        self.analizador_lexico = analizador_lexico
        self.analizador_semantico = analizador_semantico
        self.token_actual = self.analizador_lexico.obtener_siguiente_token()

    def consumir(self, tipo_token):
        if self.token_actual[0] == tipo_token:
            self.token_actual = self.analizador_lexico.obtener_siguiente_token()
        else:
            raise Exception(f"Error de sintaxis. Se esperaba {tipo_token}, se encontró {self.token_actual[0]}")

    def factor(self):
        if self.token_actual[0] == 'NUMERO':
            valor = self.token_actual[1]
            self.consumir('NUMERO')
            return valor
        elif self.token_actual[0] == 'PARENTESIS_IZQ':
            self.consumir('PARENTESIS_IZQ')
            resultado = self.expresion()
            self.consumir('PARENTESIS_DER')
            return resultado
        elif self.token_actual[0] == 'RAIZ':
            self.consumir('RAIZ')
            radicando = self.factor()
            self.analizador_semantico.verificar_raiz_cuadrada(radicando)
            resultado = math.sqrt(radicando)
            return resultado
        elif self.token_actual[0] == 'POTENCIA':
            self.consumir('POTENCIA')
            base = self.factor()
            self.consumir('POTENCIA')
            exponente = self.factor()
            resultado = base ** exponente
            return resultado
        elif self.token_actual[0] in ('SEN', 'COS', 'TAN'):
            return self.funcion_trigonometrica()

    def termino(self):
        resultado = self.factor()
        while self.token_actual[0] in ('POR', 'DIVIDIR'):
            if self.token_actual[0] == 'POR':
                self.consumir('POR')
                resultado *= self.factor()
            elif self.token_actual[0] == 'DIVIDIR':
                self.consumir('DIVIDIR')
                divisor = self.factor()
                self.analizador_semantico.verificar_division_por_cero(divisor)
                resultado /= divisor
        return resultado

    def expresion(self):
        resultado = self.termino()
        while self.token_actual[0] in ('MAS', 'MENOS'):
            if self.token_actual[0] == 'MAS':
                self.consumir('MAS')
                resultado += self.termino()
            elif self.token_actual[0] == 'MENOS':
                self.consumir('MENOS')
                resultado -= self.termino()
        return resultado

    def funcion_trigonometrica(self):
        if self.token_actual[0] in ('SEN', 'COS', 'TAN'):
            funcion = self.token_actual[0]
            self.consumir(funcion)
            self.consumir('PARENTESIS_IZQ')
            argumento = self.expresion()
            self.analizador_semantico.verificar_argumento_trigonometrico(argumento)
            self.consumir('PARENTESIS_DER')

            if funcion == 'SEN':
                return math.sin(argumento)
            elif funcion == 'COS':
                return math.cos(argumento)
            elif funcion == 'TAN':
                return math.tan(argumento)

    def analizar(self):
        return self.expresion()