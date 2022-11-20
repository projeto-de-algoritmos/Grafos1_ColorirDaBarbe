# Colorir da Barbe

**Número da Lista**: 26<br>
**Conteúdo da Disciplina**: Grafos 1<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 17/0011267 |  Giovanna Borges Bottino |
| 18/0119818  |  Felipe Boccardi Silva Agustini |

## Sobre 

O jogo seleciona uma imagem aleatoria dentro da pasta assets ao inicializar (as imagem devem conter o tamanho maximo de 300x300 pixels) E então pode-se colorir a imagem com a cor selecionada no colour picker utilizando o algoritimo Breadth First Search (BFS) ou  Depth First Search (DFS). para isso basta alternar entre os dois algoritmos clicando no botão no canto inferior direito.

Após a execução do algoritmo é mostrado o tempo de execução para o preenchimento da area selecionada.

## Screenshots
![imagem 1](/public/screenshot1.PNG)

![imagem 2](/public/screenshot2.PNG)

![imagem 3](/public/screenshot3.PNG)

## Video


https://user-images.githubusercontent.com/23579166/202920349-696f105a-113b-4ef4-b434-c15017245e3d.mp4


## Instalação 
*Linguagem*: Python<br>
*Framework*: pygame<br>

### Crie um ambiente em python 3
```
python3 -m venv env
```

### Ative o ambiente
```
source env/bin/activate
```

### Instale as dependencias
```
pip install -r requirements.txt
```

## Uso 

### Após a instalação rode o jogo executando o comando
```
python src/game.py
```

## Testes 

Para rodar os testes basta executar o comando a baixo.
```
python -m unittest tests/unit/test_graph.py
```

## Outros 
Este trabalho tem como finalidade mostrar os conhecimentos da dupla no uso de algoritimos de busca em grafos e não possui fins comerciais. As imagens contidas neste repositório são uma parodia baseadas na logo da Barbie, e podem ser retirada caso solicitado. 
