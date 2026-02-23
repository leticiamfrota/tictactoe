# Jogo da Velha Inteligente (Minimax AI)

Este repositório contém duas implementações do clássico Jogo da Velha, desenvolvidas em Python. O diferencial deste projeto é a integração do **Algoritmo Minimax**.

## 2. Funcionalidades
* **IA:** Utiliza recursão e lógica Minimax para prever todas as jogadas possíveis.
* **Modo Multiplayer:** Opção de jogar contra um amigo localmente.
* **Duas Versões de Interface:**
    * `tic_tac_toe.py`: Versão clássica para terminal/console.
    * `tic_tac_toe_gui.py`: Versão moderna com janela e botões (Tkinter).

## 3. Tecnologias Utilizadas
* Python 3.x
* Biblioteca `Tkinter` (para a interface gráfica)
* Algoritmo de Árvore de Decisão Minimax

## 4. Como o Minimax Funciona?
O algoritmo explora recursivamente todos os estados possíveis do tabuleiro, atribuindo pontuações:
- **+10** para vitória da IA
- **-10** para vitória do humano
- **0** para empate

A IA escolhe a jogada que maximiza sua pontuação mínima, garantindo que, no pior cenário, o jogo termine em empate.

## 5. Como Executar

### Versão Terminal (CLI)
```bash
python tic_tac_toe.py
