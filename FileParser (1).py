#!/usr/bin/python
import ast
import os
NomeDeFunc=""
DicionarioDeNomedeFunc = {}

class MyCustomVisitor(ast.NodeVisitor):
    
    def __init__(self):
        self.counter = 0
    try:
        1 + 1
    except TypeError:
        print("nao tem pass")
        print("nao tem pass")
    except IndentationError:
        pass
    except IndentationError:
        pass

    '''
    # Aux function
    def get_call_name(self, node):
        if isinstance(node.func, ast.Name):
            return node.func.id
        elif isinstance(node.func, ast.Attribute):
            return node.func.attr
        else:
            raise NotImplementedError("Could not extract call-name from node: " + str(node))
    '''
    
    def visit_FunctionDef(self, node):
        global NomeDeFunc
        NomeDeFunc = node.name
        print("Foi declarado uma funcao chamada : " + NomeDeFunc)
        super(MyCustomVisitor, self).generic_visit(node)

    '''
    def visit_Call(self, node):
        call_name = self.get_call_name(node)
        print(str("\t\t'{0}' was called.").format(call_name))
        super(MyCustomVisitor, self).generic_visit(node)
    '''
    '''
    def visit_Try(self , node):
        
        print("Try")
        contador = 0
        while (node.handlers[0].body[contador] != node.handlers[0].body[-1]) :     
            contador = contador + 1
        
        if  ast.Pass() == node.handlers[0].body[-1] :
            print("Funcao vazia")
        print(node.handlers[0].body[-1])
        print(ast.Pass())
        
        super(MyCustomVisitor, self).generic_visit(node)
    '''        

    def visit_ExceptHandler(self, node):
        global NomeDeFunc
        global DicionarioDeNomedeFunc


        if node.body[0] == node.body[-1] :
            comparar = str(node.body[0])
            if comparar.find("Pass") == -1:
                pass
            else:
                if NomeDeFunc not in DicionarioDeNomedeFunc :
                    DicionarioDeNomedeFunc.update({NomeDeFunc : 1})
                else :
                    DicionarioDeNomedeFunc.update({NomeDeFunc : DicionarioDeNomedeFunc[NomeDeFunc]+1})
                print("Found in the Func "+NomeDeFunc)
                self.counter = self.counter + 1
        
        
        

if __name__ == "__main__":
    import sys
    try:
        1 + 1
    except TypeError:
        print("nao tem pass")
        print("nao tem pass")
    except IndentationError:
        print("nao tem pass")
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

        # parses the content of this file
        root = ast.parse(file_str)

        # visits the Abstract Syntax Tree
        visitor = MyCustomVisitor()
        visitor.visit(root)
        print("A total of {0} ExceptHandler just with pass were found in {1}.".format(visitor.counter, input_path))
        
        print (DicionarioDeNomedeFunc)
