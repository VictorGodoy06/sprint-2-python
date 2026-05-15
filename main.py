import os

def limpar_console():
    os.system("cls" if os.name == "nt" else "clear")

# ---------------------------------------------------------
# SPRINT 2: COMPUTATIONAL THINKING WITH PYTHON
# 
# INTEGRANTES:
# - Bruno Marcelo Real e Silva | RM: 569785
# - Luiz Ademario              | RM: 571182
# - Lucas Gaspar               | RM: 568616
# - Gustavo Noleto             | RM: 569592
# - Victor Godoy               | RM: 571454
# ---------------------------------------------------------

def sprint_2_python():
    # Base de dados simulada: Lista de dicionários para armazenar as fotos/matérias[cite: 1]
    biblioteca_estudos = []

    # Mapeamento de integrações (IA que une temas correlatos)[cite: 1, 5]
    integracoes_ia = {
        "JavaScript": "Front-End",
        "Python": "Back-End",
        "Design": "UX/UI",
        "Calculo": "Fisica"
    }

    # Uma limpeza ao iniciar; não limpar no começo de cada volta do while,
    # senão o resultado das opções 2 e 3 some antes de ser lido.
    limpar_console()
    while True:
        print("\n--- SPRINT 2 PYTHON - MENU PRINCIPAL ---")
        print("1. Capturar e Classificar Foto (IA)")
        print("2. Visualizar Galeria Acadêmica")
        print("3. Verificar Integrações de Matérias")
        print("0. Sair")

        opcao = input("Escolha uma funcionalidade: ")
        limpar_console()

        # Validação de entrada: garante que apenas números sejam aceitos[cite: 1]
        if not opcao.isdigit():
            print("\n[ERRO] Por favor, digite apenas números.")
            continue

        match opcao:
            case "1":
                print("\n--- CAPTURA INTELIGENTE ---")
                nome_arquivo = input("Nome do arquivo (ex: aula_01): ").strip()
                limpar_console()
                print("\n--- CAPTURA INTELIGENTE ---")
                materia = input("Qual a matéria desta foto? ").capitalize().strip()
                limpar_console()

                if not nome_arquivo or not materia:
                    print("[ERRO] Nome e matéria são obrigatórios!")
                else:
                    # Lógica de "IA": Sugere pasta baseada na matéria[cite: 1]
                    sugestao = integracoes_ia.get(materia, "Geral")

                    foto = {
                        "arquivo": f"{nome_arquivo}.jpg",
                        "materia": materia,
                        "pasta_ia": sugestao
                    }
                    biblioteca_estudos.append(foto)
                    print(f"\n[IA] Foto '{nome_arquivo}' salva com sucesso!")
                    print(f"Sugerido mover para a pasta: {sugestao}")

            case "2":
                print("\n--- GALERIA ACADÊMICA ---")
                if not biblioteca_estudos:
                    print("A galeria está vazia.")
                else:
                    # Exibição formatada utilizando f-strings[cite: 1, 5]
                    for i, item in enumerate(biblioteca_estudos, 1):
                        print(f"{i}. [{item['materia']}] Arquivo: {item['arquivo']} (Pasta: {item['pasta_ia']})")

            case "3":
                print("\n--- MAPA DE INTEGRAÇÃO DE CONTEÚDOS ---")
                # Extração das matérias para verificação de conexões[cite: 1]
                materias_aluno = [f['materia'] for f in biblioteca_estudos]

                encontrou_conexao = False
                for mat, conexao in integracoes_ia.items():
                    # Regra de negócio: identifica se temas correlatos coexistem
                    if mat in materias_aluno and conexao in materias_aluno:
                        print(f"🔗 IA Detectou: Seus estudos de '{mat}' complementam '{conexao}'!")
                        encontrou_conexao = True

                if not encontrou_conexao:
                    print("A IA ainda não encontrou conexões entre suas matérias atuais.")

            case "0":
                print("Finalizando Sprint 2 Python. Bons estudos!")
                break

            case _:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    sprint_2_python()