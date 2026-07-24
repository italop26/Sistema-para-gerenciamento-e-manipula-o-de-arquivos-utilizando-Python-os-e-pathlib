from pathlib import Path
import os


def listar_arquivos():
    caminho = Path(input("Informe o caminho da pasta: "))

    if not caminho.exists():
        print("Pasta não encontrada.")
        return
    print(f"\nConteúdo de: {caminho}\n")

    for item in caminho.iterdir():
        if item.is_dir():
            print(f"{item.name}")
        else:
            print(f"{item.name}")

    print()

def criar_arquivo():
    caminho = Path(input("Informe o caminho do arquivo: "))

    if caminho.exists():
        print("Esse arquivo já existe.")
        return

    caminho.touch()
    print("Arquivo criado com sucesso.")

def atualizar_arquivo():
    caminho = Path(input("Informe o caminho do arquivo: "))

    if not caminho.exists():
        print("Arquivo não encontrado.")
        return

    texto = input("Digite o texto para adicionar:")

    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(texto + " ")

    print("Arquivo atualizado.")

def deletar_arquivo():
    caminho = Path(input("Informe o caminho do arquivo: "))

    if not caminho.exists():
        print("Arquivo não encontrado.")
        return

    caminho.unlink()

    print("Arquivo deletado.")

def criar_pasta():
    caminho = Path(input("Nome ou caminho da pasta: "))

    if caminho.exists():
        print("A pasta já existe.")
        return

    caminho.mkdir(parents=True)

    print("Pasta criada.")

def deletar_pasta():
    caminho = Path(input("Informe a pasta: "))

    if not caminho.exists():
        print("Pasta não encontrada.")
        return

    try:
        caminho.rmdir()
        print("Pasta removida.")

    except OSError:
        print("A pasta não está vazia.")

def renomear():
    antigo = Path(input("Arquivo/Pasta atual: "))

    if not antigo.exists():
        print("Caminho não encontrado.")
        return

    novo = antigo.parent / input("Novo nome: ")

    antigo.rename(novo)

    print("Renomeado com sucesso.")

def mostrar_diretorio():
    print("Diretório atual:")
    print(os.getcwd())
    print()


def menu():
    while True:

        print("=" * 40)
        print(" GERENCIADOR DE ARQUIVOS ".center(40))
        print("=" * 40)
        print("1 - Mostrar diretório atual")
        print("2 - Listar arquivos")
        print("3 - Criar arquivo")
        print("4 - Atualizar arquivo")
        print("5 - Deletar arquivo")
        print("6 - Criar pasta")
        print("7 - Deletar pasta")
        print("8 - Renomear")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_diretorio()

        elif opcao == "2":
            listar_arquivos()

        elif opcao == "3":
            criar_arquivo()

        elif opcao == "4":
            atualizar_arquivo()

        elif opcao == "5":
            deletar_arquivo()

        elif opcao == "6":
            criar_pasta()

        elif opcao == "7":
            deletar_pasta()

        elif opcao == "8":
            renomear()

        elif opcao == "0":
            print("\nAté logo!")
            break

        else:
            print(" Opção inválida.")


def main():
    menu()



if __name__ == "__main__":
    main()