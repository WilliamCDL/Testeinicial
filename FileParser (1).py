#!/usr/bin/python
import ast
import os
from pydriller import RepositoryMining
#variaveis globais para salvar o nome da func e a lista das funcs desejadas
NomeDeFunc=""
NomeDeClass=""
Contador = 0
DicionarioDeNomedeFunc = {}

class MyCustomVisitor(ast.NodeVisitor):
    #variavel para guardar a quantidade de funcoes
    def __init__(self):
        self.counter = 0
        global Contador
        Contador = 0
        
    #apenas para teste do catch
        try:
            1 + 1
        except TypeError:
            print("nao tem pass")
            print("nao tem pass")
        except IndentationError:
            pass
        except IndentationError:
            pass


    def visit_FunctionDef(self, node):
        global NomeDeFunc
        global Contador
        global NomeDeClass


        if Contador == 0 :
            NomeDeClass = ""
            NomeDeFunc = ""
        
        print("Foi declarado uma funcao chamada : " + node.name)
        
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
        
        
            
            

            #print("Found in the Func "+NomeDeFunc)
            
            #comparar = str(node.body[0])
            #if comparar.find("Pass") == -1:
            #    pass
            #else:
            #    if NomeDeFunc not in DicionarioDeNomedeFunc :
            #        DicionarioDeNomedeFunc.update({NomeDeFunc : 1})
            #    else :
            #        DicionarioDeNomedeFunc.update({NomeDeFunc : DicionarioDeNomedeFunc[NomeDeFunc]+1})
            #    print("Found in the Func "+NomeDeFunc)
            #    self.counter = self.counter + 1
        
    def visit_ClassDef(self, node) :
        global Contador
        global NomeDeClass
        NomeDeClass = node.name
        Contador = 0
        for x in node.body :
            if isinstance(x, ast.FunctionDef):
                Contador+=1
        super(MyCustomVisitor, self).generic_visit(node)
def teste(int ):
    try:
        1 + 1
    except TypeError:
        print("nao tem pass")
        print("nao tem pass")
    except IndentationError:
        pass
    except IndentationError:
        pass

if __name__ == "__main__":
    import sys
    try:
        1 + 1
    except TypeError:
        print("nao tem pass")
        print("nao tem pass")
    except IndentationError:
        pass
    except IndentationError:
        pass
    
    if len(sys.argv) == 2 :
        input_path = sys.argv[1]
    else :
        input_path =  __file__

    print("Processing file: " + input_path)

    with open(input_path, "r") as input:

        # reads the content of this file
        file_str  = input.read()
        for lista in RepositoryMining('https://github.com/WilliamCDL/Testeinicial').traverse_commits():
            for arquivos in lista.modifications :
                root = ast.parse(arquivos.source_code)
                visitor = MyCustomVisitor()
                visitor.visit(root)
                print("A total of {0} ExceptHandler just with pass were found in {1}.".format(visitor.counter, arquivos.filename))
        
                print (DicionarioDeNomedeFunc)
                DicionarioDeNomedeFunc.clear()
        # parses the content of this file
        

        # visits the Abstract Syntax Tree
        
        
        
        #for index,value in DicionarioDeNomedeFunc.items():
        #    print(index, ";" , value)
             
        #arq = open('lista.txt', 'w')
        #for index,value in DicionarioDeNomedeFunc.items():
        #    arq.write(index)
        #    arq.write(";")
        #    arq.write(str(value)+'\n')
        
        #arq.close()   

        
