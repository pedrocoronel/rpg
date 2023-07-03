import os


def clear():
    os.system("clear")


def espaco():
    return " "


def pergunta():
    print("O que você faz?")
    escolha = input("> ")
    return escolha
