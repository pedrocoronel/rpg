from mapa import logo, gaiola
from sistema import clear, espaco, pergunta


def menu():
    clear()
    logo()
    print(espaco() * 7, "-- Bem Vindo --\n")
    print("[1] Novo Jogo.")
    print("[2] Sair.")
    escolha = input("> ")
    return escolha


def capitulo1():
    clear()
    gaiola()
    print("Você acorda preso em uma gaiola de metal.")
    print("[1] Não fazer nada.")
    print("[2] Olhar ao redor.")
    pergunta()


def fase1_1():
    clear()
    gaiola()
    print("Você fica um bom tempo sem fazer nada.")
    print("[1] Não fazer nada.")
    print("[2] Olhar ao redor.")
    pergunta()


def main():
    clear()
    logo()
    menu()
    capitulo1()


if __name__ == "__main__":
    main()
