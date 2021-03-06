#!/usr/bin/python
import ast
import os
from pydriller import RepositoryMining
#variaveis globais para salvar o nome da func e a lista das funcs desejadas
NomeDeFunc=""
NomeDeClass=""
#variavel para guardar a quantidade de funcoes numa classe
Contador = 0
DicionarioDeNomedeFunc = {}

class MyCustomVisitor(ast.NodeVisitor):
    
    def __init__(self):
        self.counter = 0
        
        global NomeDeFunc
        global Contador
        global NomeDeClass
        global DicionarioDeNomedeFunc
        Contador = 0
        self.commit_message = ''
        self.except_found = False
        NomeDeFunc=""
        NomeDeClass=""
        DicionarioDeNomedeFunc.clear()
        
        
    def visit_FunctionDef(self, node):
        global NomeDeFunc
        global Contador
        global NomeDeClass


        if Contador == 0 :
            NomeDeClass = ""
            NomeDeFunc = ""
        
        if Contador >= 1 :
            Contador -= 1
        
        #Salvando o nome da funcao e seus parametros
        
            
        NomeDeFunc = NomeDeClass + node.name+"("
        for Parametros in node.args.args:
            if Parametros == node.args.args[-1] :
                NomeDeFunc+=Parametros.arg
            else :
                NomeDeFunc+=Parametros.arg+","
        NomeDeFunc+=")" 
                    
            

        #necessario para poder visitar os filhos
        super(MyCustomVisitor, self).generic_visit(node)

       

    def visit_ExceptHandler(self, node):
        global NomeDeFunc
        global NomeDeClass
        global Contador
        global DicionarioDeNomedeFunc

        #caso a lista tenha tamanho 1
        if node.body[0] == node.body[-1] :
            #verifica se o valor eh igual a pass
            if isinstance(node.body[0], ast.Pass):
                #caso seja incrementa o contador em 1
                self.counter = self.counter + 1
                #verifica se a funcao ja esta salva, caso sim incrementa o contador, caso nao adiciona no dic
                if NomeDeFunc not in DicionarioDeNomedeFunc :
                    DicionarioDeNomedeFunc.update({NomeDeFunc : 1})
                else :
                    DicionarioDeNomedeFunc.update({NomeDeFunc : DicionarioDeNomedeFunc[NomeDeFunc]+1})

        
    def visit_ClassDef(self, node) :
        global Contador
        global NomeDeClass
        NomeDeClass = node.name
        Contador = 0
        for x in node.body :
            if isinstance(x, ast.FunctionDef):
                Contador+=1
        super(MyCustomVisitor, self).generic_visit(node)

class RodarAnalise() :
    def __init__ (self) :
        pass

    
if __name__ == "__main__":

    numeroDoComit = 0
    for lista in RepositoryMining('https://github.com/WilliamCDL/Testeinicial', only_modifications_with_file_types=['.py']).traverse_commits():
            
        for arquivos in lista.modifications :

            if arquivos.filename.endswith('.py') :
                try:
                    root = ast.parse(arquivos.source_code)
                except (SyntaxError, ValueError) as e1:
                    #logging.error('{}\n\t{}'.format(e1.msg, e1.text))
                    continue
                except IndentationError as e2:
                    logging.error(e2.print_file_and_line)
                    continue
                visitor = MyCustomVisitor()
                visitor.visit(root)
                if len(DicionarioDeNomedeFunc) > 0 :
                    
                    #tira a estensão .py, para criar um arquivo de mesmo nome porem diferente extensão
                    auxiliarParaNomeArquivo = arquivos.filename
                    auxiliarParaNomeArquivo = auxiliarParaNomeArquivo.replace('.py', '')
                    #caminho para o arquivo onde sera criado/salvo
                    
                    pasta = 'Testes/WilliamCDL/'+lista.project_name+"/"
                    if os.path.isdir(pasta): # vemos de este diretorio ja existe
                        pass
                    else:
                        os.makedirs(pasta) # aqui criamos a pasta caso nao exista


                    nomedotxt = pasta + auxiliarParaNomeArquivo+ ".txt"
                    if os.path.isfile(nomedotxt) :
                    	arq = open(nomedotxt, 'a')
                    	for index,value in DicionarioDeNomedeFunc.items():
                        	arq.write(arquivos.filename)
                        	arq.write(";")
                        	arq.write(index)
                        	arq.write(";")
                        	arq.write(str(value))
                        	arq.write(";")
                        	arq.write(lista.author.name)
                        	arq.write(";")
                        	arq.write(lista.author.email)
                        	arq.write(";")
                        	arq.write(str(lista.author_date))
                        	arq.write(";")
                        	arq.write(lista.hash+"\n")

                    	arq.close()
                    else:
                    	arq = open(nomedotxt, 'w')
                    	arq.write("Filename")
                    	arq.write(";")
                    	arq.write("NomeDeFunc")
                    	arq.write(";")
                    	arq.write("Quantidade")
                    	arq.write(";")
                    	arq.write("Autor")
                    	arq.write(";")
                    	arq.write("Email")
                    	arq.write(";")
                    	arq.write("Data")
                    	arq.write(";")
                    	arq.write("Hash\n")
                    	for index,value in DicionarioDeNomedeFunc.items():
                        	arq.write(arquivos.filename)
                        	arq.write(";")
                        	arq.write(index)
                        	arq.write(";")
                        	arq.write(str(value))
                        	arq.write(";")
                        	arq.write(lista.author.name)
                        	arq.write(";")
                        	arq.write(lista.author.email)
                        	arq.write(";")
                        	arq.write(str(lista.author_date))
                        	arq.write(";")
                        	arq.write(lista.hash+"\n")
                        	
                    	arq.close()
                    
            
        numeroDoComit+=1

   
    
        
       

        
