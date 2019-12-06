import re
# import os
# import shutil
# from random import randint
# dire = ""
# alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v']
# nome = []

# for i in range(9):
#     number = randint(0,9)
#     a = alfabeto.index(alfabeto[number])
#     nome.append(alfabeto[a])
# nome = ''.join(nome)
# dire = "./temp_"+nome

# def createDir():
#     os.makedirs("./temp_"+nome)
    

# def moveDir(arquivo, dire):
    
#     shutil.move(arquivo, dire)
    
# def renameArchives(arquivo):
#     for nome in os.listdir('.'):
#         if(nome == arquivo):
#             print(nome)
            
#OBS: ele pode ler os arquivos especificados por caminhos
with open('arquivo.html', 'r', encoding='UTF-8') as arquivo:
    aux_html = open('aux_html.txt', 'a', encoding='UTF-8')
    for i in arquivo:
        x = re.sub("\n", "", i)        
        add_linha = x
        aux_html.write(add_linha)
    
    campo1 = re.sub("campo1", "testedokaio", aux_html)
    aux_html.write(campo1)
    # re.sub("campo2", "testedokaio", aux_html)
    # re.sub("campo3", "testedokaio", aux_html)
    # re.sub("campo4", "testedokaio", aux_html)
    # re.sub("campo5", "testedokaio", aux_html)
    # re.sub("campo6", "testedokaio", aux_html)

    aux_html.close()


# renameArchives('arquivo.html')
# createDir()
# moveDir('./arquivo.html', dire)