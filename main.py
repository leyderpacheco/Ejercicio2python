#numero par o impar

def calculo():
    print("Numero Par o Impar")
    numero=int(input("NUmero :"))

    if numero %2 == 0:
        print(f'el NUmero {numero} es par ')
        return "par"
    else :
        print(f'el NUmero {numero} es impar ')
        return "impar"


if __name__ == '__main__':
    calculo()