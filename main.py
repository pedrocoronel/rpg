import os
import time

rpg = """
  _____ _    _____ _   _ ____
 |  _  | |  |  _  | \ | |  __|
 | |_| | |  | | | |   \ |  _|
 |  _  | |__| |_| | |\  | |__
 |_| |_|____|_____|_| \_|____| v1.0

"""

gaiola = """
  _____ _____ _ _____ _    _____
 |  ___|  _  | |  _  | |  |  _  |
 | | __| |_| | | | | | |  | |_| |
 | ||_ |  _  | | |_| | |__|  _  |
 |_____|_| |_|_|_____|____|_| |_|

"""

floresta = """
  ____ _    _____ ____  ____ ____ _______ _____
 |  __| |  |  _  |  _ \|  __| ___|__   __|  _  |
 | |_ | |  | | | | |_) |  _||__ |   | |  | |_| |
 |  _|| |__| |_| |  _ <| |__ __| |  | |  |  _  |
 |_|  |____|_____|_| \_|____|____|  |_|  |_| |_|

"""

def clear():
	os.system("clear")

def espaco():
	return" "

def logo():
	print(rpg)
	time.sleep(1)

def menu():
	clear()
	logo()
	print(espaco() * 7,"-- Bem Vindo --\n")
	print("[1] Jogar.")
	print("[0] Sair.")
	escolha = input("> ")
	return escolha

def pergunta():
	print("O que você faz?")
	escolha = input("> ")
	return escolha

def fase1():
	clear()
	logo()
	print("vc acorda no preso em uma gaiola de metal.")
	print("[1] Não fazer nada.")
	print("[2] Olhar ao redor.")
	print("[3] ")
	pergunta()

def main():
	clear()
	logo()
	menu()
	fase1()

if __name__ == "__main__":
    main()
