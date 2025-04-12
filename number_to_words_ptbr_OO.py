class NumeroPorExtenso:
    def __init__(self, numero):
        self.numero = float(str(numero).replace(",", "."))
        self.unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
        self.dezenas_simples = ["dez", "onze", "doze", "treze", "quatorze", "quinze",
                                "dezesseis", "dezessete", "dezoito", "dezenove"]
        self.dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta",
                        "sessenta", "setenta", "oitenta", "noventa"]
        self.centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos",
                         "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

    # Adiciona as casas decimais ao número inteiro
    def converter(self):
        if not (0 <= self.numero <= 9999999.99):
            raise ValueError("Número fora do intervalo permitido.")

        inteiro = int(self.numero)
        decimal = int(round((self.numero - inteiro) * 100))

        partes = self._converter_inteiro(inteiro)

        if decimal > 0:
            if decimal < 10:
                partes.append(", vírgula, zero ")
            else:
                partes.append(", vírgula, ")
            partes.append(self._converter_centena(decimal))

        return "".join(partes).capitalize()
    
    # Escreve a parte das centenas
    def _converter_centena(self, numero):
        if numero == 100:
            return "cem"

        c = numero // 100
        d = (numero % 100) // 10
        u = numero % 10

        partes = []
        if c:
            partes.append(self.centenas[c])
        if d == 1:
            partes.append(self.dezenas_simples[u])
        else:
            if d:
                partes.append(self.dezenas[d])
            if u:
                partes.append(self.unidades[u])

        return " e ".join(partes)
    
    # Escreve o número por extenso
    def _converter_inteiro(self, numero):
        milhao = numero // 1_000_000
        milhar = (numero % 1_000_000) // 1_000
        unidades = numero % 1_000

        partes = []

        if milhao:
            partes.append(self._bloco(milhao, "milhão", "milhões"))
        if milhar:
            if milhar == 1:
                partes.append("mil")
            else:
                partes.append(self._converter_centena(milhar) + " mil")
        if unidades or not partes:
            partes.append(self._converter_centena(unidades))

        return self._juntar_com_e(partes)

    # Valida entre milhão e milhões
    def _bloco(self, numero, singular, plural):
        if numero == 1:
            return f"{self._converter_centena(numero)} {singular}"
        else:
            return f"{self._converter_centena(numero)} {plural}"

    def _juntar_com_e(self, partes):
        resultado = []
        for i, parte in enumerate(partes):
            if i > 0:
                resultado.append("e")
            resultado.append(parte)
        return resultado


# Uso do programa
def main():
    while True:
        entrada = input("Digite um número entre 0 e 9999999,99: ").replace(",", ".")
        try:
            valor = float(entrada)
            numero_extenso = NumeroPorExtenso(valor)
            resultado = numero_extenso.converter()
            print("\nNúmero por extenso:")
            print(resultado)
            break
        except ValueError as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()