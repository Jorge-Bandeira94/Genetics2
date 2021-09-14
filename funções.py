# Módulos e pacotes
import os
from time import sleep

# Cabeçalho ------------------------------------------------------------------------------------------------------------
print(50*'-=-')
seq = input('Insira sua sequência de nucleotídeos em formato FASTA: ').strip()
print(50*'-=-')
print('Processando...\n\n')
sleep(1)
print('_ : Stop códon\n(M) : Start códon\n')

# Variáveis utilizadas nas funções -------------------------------------------------------------------------------------
eq = ''.join(seq)
seq = seq.lower()
tamanho = len(seq)
comp = ''
lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []
lista6 = []

# Geranção de fita complementar ----------------------------------------------------------------------------------------
comp = ''
for i in seq:
    if i == 'a':
        comp += 't'
    elif i == 't':
        comp += 'a'
    elif i == 'c':
        comp += 'g'
    else:
        comp += 'c'
with open('Complementar.txt', 'a') as complementar:
    complementar.write(comp)
    complementar.close()


# Criando um arquivo para a sequencia input e gravando num TXT ---------------------------------------------------------
arquivo1 = open(os.path.join('Genetic.txt'),'w')
for palavra in seq:
    arquivo1.write(palavra)
arquivo2 = 'tradução.txt'

# Dicionário para codigo genético --------------------------------------------------------------------------------------
codigogenetico = {'ata':'I', 'aaa':'K', 'atc':'I', 'aat':'N', 'ttt':'F', 'ttc':'F', 'tta':'L', 'ttg': 'L', 'tct':'S',
                  'tcc': 'S', 'tca': 'S', 'tcg': 'S', 'tat': 'Y', 'tac': 'Y','taa': '_\n', 'tag': '_\n', 'tgt': 'C',
                  'tgc':'C','tga': '_\n', 'tgg': 'W', 'ctt': 'L', 'ctc': 'L', 'cta': 'L', 'ctg': 'L', 'cct': 'P',
                  'ccc': 'P', 'cca': 'P', 'ccg': 'P', 'cat': 'H', 'cac': 'H', 'caa':'Q', 'cag': 'Q', 'cgt': 'R',
                  'cgc': 'R', 'cga':'R', 'cgg':'R', 'att': 'I','atg': '(M)', 'act':'T', 'acc': 'T', 'aca': 'T',
                  'acg': 'T','aac': 'N', 'aag':'K', 'agt':'S', 'agc':'S', 'aga':'R', 'agg': 'R', 'gtt':'V', 'gtc':'V',
                  'gta':'V', 'gtg':'V', 'gct':'A', 'gcc':'A', 'gca':'A', 'gcg':'A', 'gat': 'D', 'gac': 'D', 'gaa':'E',
                  'gag':'E', 'ggt':'G', 'ggc': 'G', 'gga': 'G', 'ggg': 'G'}

# Funções --------------------------------------------------------------------------------------------------------------
def codons_Separados_Sense(orf, lista):
    # Função para separa cada 3 caracteres em um elemento distinto numa lista
    count = 0
    s = ''
    for i in seq[orf:]:
        s += i
        count += 1
        if count == 3:
            lista.append(s)
            s = ''
            count = 0

def codons_Separados_AntiSense(orf, lista):
    # Função para separa cada 3 caracteres em um elemento distinto numa lista
    count = 0
    s = ''
    for i in comp[::orf]:
        s += i
        count += 1
        if count == 3:
            lista.append(s)
            s = ''
            count = 0

def traducao(orf, lista):
    # Função para traduzir cada trio de caracteres baseado no dicionário
    texto1 = ''
    for elemento in lista:
        if elemento in codigogenetico:
            for k, v in codigogenetico.items():
                if k == elemento:
                    texto1 += v
    with open('tradução.txt', 'a') as trad:
        trad.write(f'Para o quadro de leitura {orf}: \n>')
        trad.write(texto1)
        trad.write('\n\n')
        trad.close()





# Para cada ORF é preciso que rode uma função com um parâmetro diferente -----------------------------------------------
codons_Separados_Sense(0, lista1)
codons_Separados_Sense(1, lista2)
codons_Separados_Sense(2, lista3)
codons_Separados_AntiSense(-1, lista4)
codons_Separados_AntiSense(-2, lista5)
codons_Separados_AntiSense(-3, lista6)
traducao('+1', lista1)
traducao('+2', lista2)
traducao('+3', lista3)
traducao('-1', lista4)
traducao('-2', lista5)
traducao('-3', lista6)
