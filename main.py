import os

def limpar_console():
    os.system("cls" if os.name == "nt" else "clear")

# ---------------------------------------------------------
# SPRINT 3: COMPUTATIONAL THINKING WITH PYTHON
# 
# INTEGRANTES:
# - Bruno Marcelo Real e Silva | RM: 569785
# - Luiz Ademario              | RM: 571182
# - Lucas Gaspar               | RM: 568616
# - Gustavo Noleto             | RM: 569592
# - Victor Godoy               | RM: 571454
# ---------------------------------------------------------

def exibir_menu():
    """Exibe o menu principal do sistema."""
    print("\n--- SPRINT 3 PYTHON - MENU PRINCIPAL ---")
    print("1. Capturar e Classificar Foto (IA)")
    print("2. Visualizar Galeria Acadêmica")
    print("3. Verificar Integrações de Matérias")
    print("0. Sair")

def capturar_foto(biblioteca_estudos, integracoes_ia):
    """Realiza a captura e classificação inteligente da foto/matéria."""
    print("\n--- CAPTURA INTELIGENTE ---")
    nome_arquivo = input("Nome do arquivo (ex: aula_01): ").strip()
    limpar_console()
    
    print("\n--- CAPTURA INTELIGENTE ---")
    materia = input("Qual a matéria desta foto? ").capitalize().strip()
    limpar_console()

    if not nome_arquivo or not materia:
        print("[ERRO] Nome e matéria são obrigatórios!")
        return

    # Lógica de IA: Sugere pasta baseada na matéria
    sugestao = integracoes_ia.get(materia, "Geral")

    foto = {
        "arquivo": f"{nome_arquivo}.jpg",
        "materia": materia,
        "pasta_ia": sugestao
    }
    
    biblioteca_estudos.append(foto)
    print(f"\n[IA] Foto '{nome_arquivo}' salva com sucesso!")
    print(f"Sugerido mover para a pasta: {sugestao}")

def visualizar_galeria(biblioteca_estudos):
    """Exibe todos os itens armazenados na galeria acadêmica."""
    print("\n--- GALERIA ACADÊMICA ---")
    if not biblioteca_estudos:
        print("A galeria está vazia.")
    else:
        for i, item in enumerate(biblioteca_estudos, 1):
            print(f"{i}. [{item['materia']}] Arquivo: {item['arquivo']} (Pasta: {item['pasta_ia']})")

def verificar_integracoes(biblioteca_estudos, integracoes_ia):
    """Verifica se existem conexões cruzadas entre as matérias estudadas."""
    print("\n--- MAPA DE INTEGRAÇÃO DE CONTEÚDOS ---")
    materias_aluno = [f['materia'] for f in biblioteca_estudos]

    encontrou_conexao = False
    for mat, conexao in integracoes_ia.items():
        if mat in materias_aluno and conexao in materias_aluno:
            print(f"🔗 IA Detectou: Seus estudos de '{mat}' complementam '{conexao}'!")
            encontrou_conexao = True

    if not encontrou_conexao:
        print("A IA ainda não encontrou conexões entre suas matérias atuais.")

def main():
    biblioteca_estudos = []
    
    integracoes_ia = {
        "JavaScript": "Front-End",
        "Python": "Back-End",
        "Design": "UX/UI",
        "Calculo": "Matemática Avançada",
    }

    limpar_console()
    while True:
        exibir_menu()
        opcao = input("Escolha uma funcionalidade: ")
        limpar_console()

        if not opcao.isdigit():
            print("\n[ERRO] Por favor, digite apenas números.")
            continue

        match opcao:
            case "1":
                capturar_foto(biblioteca_estudos, integracoes_ia)
            case "2":
                visualizar_galeria(biblioteca_estudos)
            case "3":
                verificar_integracoes(biblioteca_estudos, integracoes_ia)
            case "0":
                print("Finalizando. Bons estudos!")
                break
            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
