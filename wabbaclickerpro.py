import pyautogui
import time
import sys
import os
from colorama import Fore, Style, init

init(autoreset=True)

# --- Configurações ---
DELAY_INICIAL = 10 
IMAGENS_BOTAO = [
    os.path.join('imagens', 'botao1.png'),
    os.path.join('imagens', 'botao2.png')
]
IMAGEM_RODAPE = os.path.join('imagens', 'rodape.jpg')
INTERVALO_SCROLL = 2
ESPERA_APOS_CLIQUE = 7
ESPERA_FILA_CHEIA = 15
CONFIDENCE_LEVEL = 0.9
MAX_TENTATIVAS_SCROLL = 5 

# --- Função para Barra de Progresso ---
def barra_de_progresso(duracao, mensagem, cor=Fore.YELLOW):
    """
    Exibe uma barra de progresso animada no terminal.
    """
    tamanho_barra = 40 # Largura da barra em caracteres

    for i in range(duracao + 1):
        percentual = i / duracao
        preenchido = int(tamanho_barra * percentual)
        # Cria a barra com caracteres de bloco
        barra = '█' * preenchido + '░' * (tamanho_barra - preenchido)
        # Monta a string de saída
        print(cor + f"{mensagem.ljust(40)} [{barra}] {i}/{duracao}s", end='\r')
        sys.stdout.flush()

        time.sleep(1)
    
    # Limpa a linha no final
    print(" " * (tamanho_barra + 60), end='\r')

# --- Função para Animação de Spinner ---
def animacao_spinner(duracao, mensagem, cor=Fore.CYAN):
    """
    Exibe uma animação de "spinner" por uma determinada duração.
    """
    spinner_chars = ['-', '\\', '|', '/']
    tempo_final = time.time() + duracao
    i = 0
    
    while time.time() < tempo_final:
        char_spinner = spinner_chars[i % len(spinner_chars)]
        print(cor + f"{mensagem} {char_spinner}", end='\r')
        i += 1
        time.sleep(0.1)
        
    print(" " * (len(mensagem) + 5), end='\r')


# --- Função para limpar o Prompt de Comando ---
def limpar_tela():
    _ = os.system('cls')

# --- Lógica Principal ---
try:
    print(Fore.LIGHTBLUE_EX + ">>> Bem-vindo ao WabbaClicker Pro <<<") 
    print(Fore.YELLOW + ">>> PARA PARAR: Pressione CTRL + C no terminal.")
    
    barra_de_progresso(DELAY_INICIAL, "Posicione a janela! Automação iniciando em")
    mods_baixados = 0
    
    print(Fore.GREEN + "\n>>> AUTOMAÇÃO INICIADA! <<<")

    while True:
        limpar_tela()
        print(Fore.MAGENTA + "=============================================================")
        print(Fore.WHITE +   "                  WabbaClicker Pro v1.0")
        print(Fore.CYAN +    "     Desenvolvido e disponibilizado por @vitorgomespro")
        print(Fore.WHITE +   "          >>> Segue no instagram e no GitHub <<<")
        print(Fore.MAGENTA + "=============================================================")
        print(Fore.GREEN + f"\n Status: {mods_baixados} mod(s) baixado(s) até agora.")
        print(Fore.YELLOW +">>> PARA PARAR: Clique no Terminal e Pressione CTRL + C")
        print("\n----------------------------------------------------")
        print("--- Iniciando Download do Mod ---")
        time.sleep(1)

        # Move o mouse para uma posição segura para evitar hover indesejado
        pyautogui.moveTo(1, 1, duration=0.25) 
        
        tentativas_scroll_feitas = 0
        botao_encontrado_neste_ciclo = False

        while tentativas_scroll_feitas < MAX_TENTATIVAS_SCROLL:
            print(Fore.CYAN + f"Tentativa {tentativas_scroll_feitas + 1}/{MAX_TENTATIVAS_SCROLL}: Procurando pelo botão de Download...")
            
            localizacao_botao = None
            # Loop para procurar por cada imagem do botão
            for imagem in IMAGENS_BOTAO:
                try:
                    localizacao_botao = pyautogui.locateOnScreen(imagem, confidence=CONFIDENCE_LEVEL)
                    if localizacao_botao:
                        print(Fore.GREEN + f">>> SUCESSO: Botão encontrado, fazendo download!")
                        break 
                except pyautogui.PyAutoGUIException:
                    pass

            if localizacao_botao:
                ponto_central_botao = pyautogui.center(localizacao_botao)
                pyautogui.click(ponto_central_botao)
                mods_baixados += 1
                barra_de_progresso(ESPERA_APOS_CLIQUE, "Download em Andamento. Próximo Download em")
                botao_encontrado_neste_ciclo = True
                break
            
            else:
                # Se não achou o botão, verifica se o rodapé apareceu
                try:
                    localizacao_rodape = pyautogui.locateOnScreen(IMAGEM_RODAPE, confidence=0.8)
                    if localizacao_rodape:
                        print(Fore.MAGENTA + ">>> Rodapé detectado! Chegamos ao fim da página.")
                        print(Fore.YELLOW + ">>> Estou voltando para o topo da página...")
                        break # Sai do loop de scroll para forçar o reset ao topo
                except pyautogui.PyAutoGUIException:
                    pass # Se falhar a captura, apenas continua

                pyautogui.press('pagedown')
                tentativas_scroll_feitas += 1
                animacao_spinner(INTERVALO_SCROLL, "Processando rolagem...")

        # Se saiu do loop (seja por acabar as tentativas ou por ver o rodapé) e não clicou
        if not botao_encontrado_neste_ciclo:
            print("\n>>> Fila de Download do Wabbajack Cheia! Aguarde um momento...")
            pyautogui.press('home') # Rola para o topo
            barra_de_progresso(ESPERA_FILA_CHEIA, "Pausa longa antes de reiniciar os downloads em")

except KeyboardInterrupt:
    print(Fore.RED + "\n\n>>> Script interrompido pelo usuário. Finalizando.")
    print(Fore.GREEN + f"\n>>> Total de mods baixados: {mods_baixados}")
    print(Fore.CYAN + ">>> Obrigado por usar o WabbaClicker Pro!")
    print(Fore.CYAN + ">>> Para usar novamente basta abrir o executável novamente.")
    print(Fore.WHITE + f"\n para sugestões ou dúvidas, me encontre no Instagram @vitorgomespro")
except pyautogui.FailSafeException:
    print(Fore.RED + "\n\n>>> ERRO: Fail-Safe de segurança ativado (mouse movido para o canto). Finalizando script.")
except FileNotFoundError:
    print(Fore.RED + f"\n\n>>> ERRO CRÍTICO: Verifique se as imagens {IMAGENS_BOTAO} e {IMAGEM_RODAPE} estão na pasta.")
except Exception as e:
    print(Fore.RED + "\n\n>>> OCORREU UM ERRO INESPERADO E CRÍTICO <<<")
    print("="*50)
    print(Fore.RED + f"--- MENSAGEM DO ERRO: {e}")
    print(Fore.RED + f"--- TIPO DO ERRO:    {type(e).__name__}")
    print("="*50)
    print(Fore.RED + ">>> O script foi finalizado.")
    input(Fore.RED + "\nPressione ENTER para fechar a janela...")