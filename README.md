# WabbaClicker Pro v1.0

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=yellow) [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/) [![GitHub stars](https://img.shields.io/github/stars/vitorgomespro/WabbaClickerPro?style=social)](https://github.com/vitorgomespro/WabbaClickerPro/stargazers)


> 🚀 Automação em Python para downloads de Modlists no Wabbajack e Nexus. Desenvolvido para tornar a instalação de centenas de mods uma tarefa simples e automática.

Se você NÃO possui o Nexus Premium e está com uma Modlist gigante para Skyrim ou outro game, não se preocupe! Aqui está sua solução...

![Demonstração da Interface do WabbaClicker Pro](https://imgur.com/a/hpnumov) 

---

## ✨ Funcionalidades Principais

* **Automação de Cliques:** Procura e clica automaticamente no botão de "Slow download" do nexus.
* **Navegação Inteligente:** Rola a página para baixo usando `PageDown` e, ao detectar o rodapé ou esgotar as tentativas, retorna ao topo com a tecla `Home`.
* **Interface de Console Polida:** Exibe um painel de controle limpo a cada ciclo, com cores, status, contador de mods baixados e barras de progresso animadas.
* **Seguro e Confiável:** Inclui um "Fail-Safe" que para o programa imediatamente se o mouse for movido para um canto da tela.
* **Portátil:** Distribuído como um único arquivo `.zip` na seção de Releases, sem necessidade de instalar Python ou outras dependências.

## 🚀 Como Usar (Para Usuários)

Para usar o programa, siga estes passos:

1.  Vá para a seção de **[Releases](https://github.com/vitorgomespro/WabbaClickerPro/releases)** deste repositório.
2.  Baixe o arquivo `.zip` da versão mais recente (ex: `WabbaClicker-Pro-v1.0.zip`).
3.  Extraia o conteúdo do arquivo `.zip` para uma nova pasta em qualquer lugar do seu computador.
4.  Abra a Pasta que você acabou de extrair.
5.  Execute o `wabbaclickerpro.exe`, posicione a janela do Wabbajack, dê um clique dentro da janela e deixe a automação começar após a contagem regressiva de 10 segundos!
6.  Pronto a automação já vai está baixando seus mods de forma automática AFK. 

## 🛠️ Para Desenvolvedores (Como Rodar do Código-Fonte)

Se você quiser rodar ou modificar o projeto a partir do código-fonte:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/vitorgomespro/WabbaClickerPro.git](https://github.com/vitorgomespro/WabbaClickerPro.git)
    ```
2.  **Navegue até a pasta:**
    ```bash
    cd WabbaClicker-Pro
    ```
3.  **Instale as dependências (recomendado criar um ambiente virtual primeiro):**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Execute o script:**
    ```bash
    python wabbaclickerpro.py
    ```

---
*Desenvolvido por [VitorGomesPro](https://github.com/vitorgomespro).*
