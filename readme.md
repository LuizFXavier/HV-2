Coloque do arquivo txt contendo o código a ser interpretado na pasta "programas".

Ao rodar o main.py, coloque o nome do arquivo .txt como variável de ambiente:

```
arquivo='exemplo.txt' python main.py
```

O programa do arquivo de texto deve estar escrito na linguagem do HV-2, sendo os comandos:
| Comando | Descrição | "Assembler"
0EE | copie valor da gaveta EE (cEE) para AC | AC←cEE |

1EE | copie valor do AC (cAC) para gaveta EE | EE←cAC |
2EE | some cEE ao AC | AC←cAC+cEE |
3EE | subtraia de AC o cEE | AC←cAC−cEE |
4EE | multiplique o cAC por cEE | AC←cAC∗cEE |
5EE | divida o cAC por cEE | AC←cAC/cEE |
6EE | se cAC > 0, vá para EE | se cAC>0, então EPI←EE |
7EE | leia um valor e guarda | na gaveta EE	leia(EE) |
8EE | escreva cEE no dispositivo de saída | escreva(cEE) |
9EE | vá para cEE |	EPI←cEE |
0-N | AC recebe uma constante (truque) | AC←N |
000 | fim do programa | fim |