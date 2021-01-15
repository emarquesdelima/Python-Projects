

class Converter:

    def volume_cilindrto_litros(self, raio, altura):

        pi = 3.14

        print(f"O raio é: {raio}")
        print(f"A altura é: {altura}")
        
        volume = pi * (raio**2) * altura

        volume_litros = volume * 1000

        print(f"O volume em litros é: {volume_litros}")

        pass

calc = Converter()

calc.volume_cilindrto_litros(0.05,0.16)
