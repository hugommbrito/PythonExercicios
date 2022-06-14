# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

# A forma como eu fiz
"""cidade = str(input('Qual a sua cidade?').strip())
cid_min = cidade.lower()
cid_lista = cid_min.split()
cid_primeira = cid_lista[0]
#print(cid_primeira)
print(cid_primeira == 'santo')"""

# A forma como ele resolve no vídeo
cid = str(input('\033[1mEm que cidade você nasceu?\033[m')).strip()
print(cid[:5].lower() == 'santo')
