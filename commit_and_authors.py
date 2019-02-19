    
from pydriller import RepositoryMining
from pydriller import GitRepository
import os
DicionarioDeNomedeFunc = {}
#for commit in RepositoryMining('C:/Users/William/Downloads/j').traverse_commits():
#   print('hash {} authored by {}'.format(commit.hash, commit.author.name))
#   print(commit.files)

teste = GitRepository('C:/Users/William/Downloads/j')
contador =0
contador2 =0
for contar in teste.files() :
    print("entrei")
    contador2+=1

#print(teste.total_commits())
#for lista in teste.get_list_commits() :
for lista in RepositoryMining('C:/Users/William/Downloads/j').traverse_commits():
    #print(contador)
    #contador+=1
    for arquivos in lista.modifications :
        
        #print(arquivos.complexity)
        #print(arquivos.new_path)
        if arquivos.filename not in DicionarioDeNomedeFunc :
            contador +=1
            DicionarioDeNomedeFunc.update({arquivos.filename : 1})
        else :
            DicionarioDeNomedeFunc.update({arquivos.filename : DicionarioDeNomedeFunc[arquivos.filename]+1})
print (DicionarioDeNomedeFunc)
print (contador)
print (contador2)        
#for tentativa2 in teste.files():
#    print(tentativa2)
     
    
 #   try:
 #       with open(tentativa2, 'r') as f:
 #           file_str  = f.read()
 #   except IOError:
 #       print ('File does not exist!')
    
        
   
    
