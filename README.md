# WabbaClicker Pro v1.1

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=yellow) [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-nc-sa/4.0/) [![GitHub stars](https://img.shields.io/github/stars/vitorgomespro/WabbaClickerPro?style=social)](https://github.com/vitorgomespro/WabbaClickerPro/stargazers)


> 🚀 Automação em Python para downloads de Modlists no Wabbajack e Nexus. Desenvolvido para tornar a instalação de centenas de mods uma tarefa simples e automática.

Se você NÃO possui o Nexus Premium e está com uma Modlist gigante para Skyrim ou outro game, não se preocupe! Aqui está sua solução...

## Demostração do que acontece no seu Console:
![Demonstração da Interface do Console](https://github.com/vitorgomespro/WabbaClickerPro/blob/main/assets/Anima%C3%A7%C3%A3o.gif?raw=true) 
Você consegue acompanhar cada ação da automação em tempo real!

## Demostração do que acontece no seu Wabbajack
![Demonstração da Interface do WabbaClicker P](https://github.com/vitorgomespro/WabbaClickerPro/blob/main/assets/Anima%C3%A7%C3%A3o%20do%20Wabbajack.gif?raw=true) 
Você pode fazer outras atividades enquanto deixa o seu PC fazer o trabalho de baixar sua lista de mods sozinho!

---
## 📆 Atualizações

### v1.1 – 15/09/2025
- 🔄 **Novo Design de Botões:** passou a buscar os novos botões “Slow download” do Nexus.
- 🖼️ **Novas Imagens de Referência:** adicionadas `imagens/Novobotaov2.png` e `imagens/Novobotaov2_hover.png`.
- 🛠️ **Robustez Aprimorada:** ajustes no nível de confiança e na lógica de detecção de elementos.
- 📄 **Changelog Interno:** veja `updates.txt` para detalhes completos desta versão.

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
    
## ❤️ Apoie o Projeto

Se o WabbaClicker Pro te ajudou e economizou seu tempo, considere apoiar meu trabalho com um café! ☕

Qualquer contribuição via PIX é um grande incentivo para eu continuar desenvolvendo e compartilhando novas soluções como esta.

![QR Code PIX para doação](https://github.com/vitorgomespro/WabbaClickerPro/blob/main/imagens/QRcode-PIX.JPG?raw=true
)

**Chave PIX Aleatória:** `0417c9d6-bdd4-4c89-8330-ad95df5f2b55`

Muito obrigado pelo seu apoio!

---
*Desenvolvido por [VitorGomesPro](https://github.com/vitorgomespro).*
