import sys
from cx_Freeze import setup, Executable

# --- Opções de Build ---

# Lista de arquivos e pastas para incluir. 
# Adicionamos a pasta 'Imagens' inteira.
arquivos_para_incluir = ['imagens/']

# Lista de bibliotecas que nosso script usa
pacotes_necessarios = ["os", "sys", "time", "pyautogui", "colorama"]

build_exe_options = {
    "packages": pacotes_necessarios,
    "include_files": arquivos_para_incluir,
}

# --- Configuração do Executável ---

# Define a base como "Console" para que nosso terminal apareça
base = "Console" if sys.platform == "win32" else None

# Define o nosso script principal e o ícone
executavel = Executable(
    "wabbaclickerpro.py",
    base=base,
    icon="icon.ico"
)

# --- Execução do Setup ---
setup(
    name="WabbaClicker Pro",
    version="1.1",
    description="Automatomação de Download de Mods pelo Wabbajack e Nexus",
    options={"build_exe": build_exe_options},
    executables=[executavel]
)