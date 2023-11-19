class AnalizadorLexico:
    def __init__(self, cadena_entrada):
        self.cadena_entrada = cadena_entrada
        self.posicion = 0
        self.caracter_actual = self.cadena_entrada[self.posicion]

    def avanzar(self):
        self.posicion += 1
        if self.posicion < len(self.cadena_entrada):
            self.caracter_actual = self.cadena_entrada[self.posicion]
        else:
            self.caracter_actual = None

    def omitir_espacios_en_blanco(self):
        while self.caracter_actual is not None and self.caracter_actual.isspace():
            self.avanzar()

    def obtener_siguiente_token(self):
        while self.caracter_actual is not None:
            if self.caracter_actual.isspace():
                self.omitir_espacios_en_blanco()
                continue

            if self.caracter_actual.isdigit():
                return self.obtener_numero()

            if self.caracter_actual == '+':
                self.avanzar()
                return ('MAS', '+')

            if self.caracter_actual == '-':
                self.avanzar()
                return ('MENOS', '-')

            if self.caracter_actual == '*':
                self.avanzar()
                return ('POR', '*')

            if self.caracter_actual == '/':
                self.avanzar()
                return ('DIVIDIR', '/')

            if self.caracter_actual == '(':
                self.avanzar()
                return ('PARENTESIS_IZQ', '(')

            if self.caracter_actual == ')':
                self.avanzar()
                return ('PARENTESIS_DER', ')')

            if self.caracter_actual == '√':
                self.avanzar()
                return ('RAIZ', '√')

            if self.caracter_actual == '^':
                self.avanzar()
                return ('POTENCIA', '^')

            if self.caracter_actual.isalpha():
                return self.obtener_funcion_trigonometrica()

            raise Exception(f"Carácter inesperado: {self.caracter_actual}")

        return ('FIN', None)

    def obtener_numero(self):
        resultado = ''
        while self.caracter_actual is not None and self.caracter_actual.isdigit():
            resultado += self.caracter_actual
            self.avanzar()
        return ('NUMERO', int(resultado))

    def obtener_funcion_trigonometrica(self):
        inicio = self.posicion
        while self.caracter_actual is not None and self.caracter_actual.isalpha():
            self.avanzar()
        funcion = self.cadena_entrada[inicio:self.posicion]
        return (funcion.upper(), funcion)
