#!/usr/bin/python
import os
from pydriller import RepositoryMining
   
if __name__ == "__main__":
    from pydriller import GitRepository
    import re
    repo = GitRepository('~/Downloads/wagtail/')
    contador0 = 0
    contador1 = 0
    linhaanterior = 0
    auxiliar=""
    testestring=""
    achou = False
    Salvarlista = []
    auxiliarNumerico = 0
    auxiliarSalvar=""
    jasalvou=False
    #https://github.com/spulec/moto
    #https://github.com/WilliamCDL/Testeinicial
    print("AuthorDate;Message")
    for lista in RepositoryMining('https://github.com/spulec/moto', only_modifications_with_file_types=['.py']).traverse_commits():
        jasalvou=False
        for modification in lista.modifications:
            achou == False
            if modification.filename.endswith('.py') :
                auxiliar=""
                diff = modification.diff
                #print(diff)
                for teste in diff :
                    if (teste == "\n"):
                        if achou or re.search("except.*:.*", testestring):
                        	#print("teste")
                        	if achou == False :
                        		achou=True
                        		testestring=""
                        		break
                        	if testestring[0]=="+" or testestring[0]=="-" :
                        		if testestring=="+":
                        			if testestring.endswith("pass") :
	                        			pasta = 'Testes/spulec/'+lista.project_name+"/"
	                        			if os.path.isdir(pasta): # vemos de este diretorio ja existe
	                        				pass
	                        			else:
	                        				os.makedirs(pasta) # aqui criamos a pasta caso nao exista
	                        			nomedotxt = pasta + lista.project_name+".csv"
	                        			if os.path.isfile(nomedotxt) :
	                        				arq = open(nomedotxt, 'a')
	                        				arq.write(modification.filename)
	                        				arq.write(";")
	                        				arq.write(";")
	                        				arq.write("ADD")
	                        				arq.write(";")
	                        				arq.write(lista.author.name)
	                        				arq.write(";")
	                        				arq.write(lista.author.email)
	                        				arq.write(";")
	                        				arq.write(str(lista.author_date))
	                        				arq.write(";")
	                        				arq.write(lista.hash)
	                        				if jasalvou == False:
	                        					arq.write(";")
	                        					arq.write('"'+lista.msg.replace("\n", " ")+'"'+"\n")
	                        					jasalvou=True
	                        				else:
	                        					arq.write(";")
	                        					arq.write('""'+"\n")
	                        				arq.close()
	                        			else:
	                        				arq = open(nomedotxt, 'w')
	                        				arq.write("Filename")
	                        				arq.write(";")
	                        				arq.write("Linha")
	                        				arq.write(";")
	                        				arq.write("Tipo")
	                        				arq.write(";")
	                        				arq.write("Autor")
	                        				arq.write(";")
	                        				arq.write("Email")
	                        				arq.write(";")
	                        				arq.write("Data")
	                        				arq.write(";")
	                        				arq.write("Hash")
	                        				arq.write(";")
	                        				arq.write("Commit\n")
	                        				arq.write(modification.filename)
	                        				arq.write(";")
	                        				arq.write(";")
	                        				arq.write("ADD")
	                        				arq.write(";")
	                        				arq.write(lista.author.name)
	                        				arq.write(";")
	                        				arq.write(lista.author.email)
	                        				arq.write(";")
	                        				arq.write(str(lista.author_date))
	                        				arq.write(";")
	                        				arq.write(lista.hash)
	                        				arq.write(";")
	                        				arq.write('"'+lista.msg.replace("\n", " ")+'"'+"\n")
	                        				arq.close()
	                        				jasalvou=True
	                        			Salvarlista.append(testestring)
	                        			achou=False;
	                        			testestring=""
                        			else:
                        				achou=False;
                        				testestring=""
                        		else:
                        			if testestring.endswith("pass"):
                        				Salvarlista.append(testestring)
                        				pasta = 'Testes/spulec/'+lista.project_name+"/"
	                        			if os.path.isdir(pasta): # vemos de este diretorio ja existe
	                        				pass
	                        			else:
	                        				os.makedirs(pasta) # aqui criamos a pasta caso nao exista
	                        			nomedotxt = pasta + lista.project_name+".csv"
	                        			if os.path.isfile(nomedotxt) :
	                        				arq = open(nomedotxt, 'a')
	                        				arq.write(modification.filename)
	                        				arq.write(";")
	                        				arq.write(";")
	                        				arq.write("DELETED")
	                        				arq.write(";")
	                        				arq.write(lista.author.name)
	                        				arq.write(";")
	                        				arq.write(lista.author.email)
	                        				arq.write(";")
	                        				arq.write(str(lista.author_date))
	                        				arq.write(";")
	                        				arq.write(lista.hash)
	                        				if jasalvou == False:
	                        					arq.write(";")
	                        					arq.write('"'+lista.msg.replace("\n", " ")+'"'+"\n")
	                        					jasalvou=True
	                        				else:
	                        					arq.write(";")
	                        					arq.write('""'+"\n")
	                        				arq.close()
	                        			else:
	                        				arq = open(nomedotxt, 'w')
	                        				arq.write("Filename")
	                        				arq.write(";")
	                        				arq.write("Linha")
	                        				arq.write(";")
	                        				arq.write("Tipo")
	                        				arq.write(";")
	                        				arq.write("Autor")
	                        				arq.write(";")
	                        				arq.write("Email")
	                        				arq.write(";")
	                        				arq.write("Data")
	                        				arq.write(";")
	                        				arq.write("Hash")
	                        				arq.write(";")
	                        				arq.write("Commit\n")
	                        				arq.write(modification.filename)
	                        				arq.write(";")
	                        				arq.write(";")
	                        				arq.write("DELETED")
	                        				arq.write(";")
	                        				arq.write(lista.author.name)
	                        				arq.write(";")
	                        				arq.write(lista.author.email)
	                        				arq.write(";")
	                        				arq.write(str(lista.author_date))
	                        				arq.write(";")
	                        				arq.write(lista.hash)
	                        				arq.write(";")
	                        				arq.write('"'+lista.msg.replace("\n", " ")+'"'+"\n")
	                        				arq.close()
	                        				jasalvou=True
                        				achou=False;
                        				testestring=""
                        			else:
                        				testestring=""
                        	else:
                        		if len(testestring)>0:
                        			if testestring.endswith("pass"):
                        				achou=False;
                        				testestring=""
                        			else:
                        				if testestring.isspace():
                        					testestring=""
                        				else:
                        					achou=False
                        					testestring=""

                        testestring=""
                    else :
                        testestring+=teste
                    
                #print(modification.filename)            
                if re.search("except.*:.*\n.*pass", diff):
                    parsed_lines = repo.parse_diff(diff)
                    added = parsed_lines['added']
                    

                    

                    for lineNumber, lineStr in added:
                        if re.search("except.*:.*", auxiliar):
                            if lineStr.endswith('pass') :
                                if(lineNumber==linhaanterior+1):
                                    #contador0+=1
                                    #print(contador0)

                                    #auxiliarParaNomeArquivo = modification.filename
                                    #auxiliarParaNomeArquivo = auxiliarParaNomeArquivo.replace('.py', 'csv')
                                    pasta = 'Testes/spulec/'+lista.project_name+"/"
                                    if os.path.isdir(pasta): # vemos de este diretorio ja existe
                                        pass
                                    else:
                                        os.makedirs(pasta) # aqui criamos a pasta caso nao exista
                                    nomedotxt = pasta + lista.project_name+".csv"
                                    if os.path.isfile(nomedotxt) :
                                        arq = open(nomedotxt, 'a')
                                        arq.write(modification.filename)
                                        arq.write(";")
                                        arq.write(str(lineNumber-1))
                                        arq.write(";")
                                        arq.write("ADD")
                                        arq.write(";")
                                        arq.write(lista.author.name)
                                        arq.write(";")
                                        arq.write(lista.author.email)
                                        arq.write(";")
                                        arq.write(str(lista.author_date))
                                        arq.write(";")
                                        arq.write(lista.hash)
                                        if jasalvou == False:
                                        	arq.write(";")
                                        	arq.write('"'+lista.msg.replace("\n", " ")+'"'+"\n")
                                        	jasalvou=True
                                        else:
                                        	arq.write(";")
                                        	arq.write('""'+"\n")

                                        arq.close()
                                    else:
                                        arq = open(nomedotxt, 'w')
                                        arq.write("Filename")
                                        arq.write(";")
                                        arq.write("Linha")
                                        arq.write(";")
                                        arq.write("Tipo")
                                        arq.write(";")
                                        arq.write("Autor")
                                        arq.write(";")
                                        arq.write("Email")
                                        arq.write(";")
                                        arq.write("Data")
                                        arq.write(";")
                                        arq.write("Hash")
                                        arq.write(";")
                                        arq.write("Commit\n")
                                        arq.write(modification.filename)
                                        arq.write(";")
                                        arq.write(str(lineNumber-1))
                                        arq.write(";")
                                        arq.write("ADD")
                                        arq.write(";")
                                        arq.write(lista.author.name)
                                        arq.write(";")
                                        arq.write(lista.author.email)
                                        arq.write(";")
                                        arq.write(str(lista.author_date))
                                        arq.write(";")
                                        arq.write(lista.hash)
                                        arq.write(";")
                                        arq.write('"'+lista.msg.replace("\n", " ")+'"'+"\n")  
                                        arq.close()
                                        jasalvou=True
                        auxiliar=lineStr
                        linhaanterior=lineNumber;

                        #print("Added line {} - {}".format(lineNumber, lineStr))
                    auxiliar=""
                    deleted = parsed_lines['deleted']
                    for lineNumber, lineStr in deleted:
                        if re.search("except.*:.*", auxiliar):
                            if lineStr.endswith('pass') :
                                if(lineNumber==linhaanterior+1):
                                    #contador1+=1
                                    
                                    #print(contador1)

                                    #auxiliarParaNomeArquivo = modification.filename
                                    #auxiliarParaNomeArquivo = auxiliarParaNomeArquivo.replace('.py', 'csv')
                                    pasta = 'Testes/spulec/'+lista.project_name+"/"
                                    if os.path.isdir(pasta): # vemos de este diretorio ja existe
                                        pass
                                    else:
                                        os.makedirs(pasta) # aqui criamos a pasta caso nao exista
                                    nomedotxt = pasta + lista.project_name+".csv"
                                    if os.path.isfile(nomedotxt) :
                                        arq = open(nomedotxt, 'a')
                                        arq.write(modification.filename)
                                        arq.write(";")
                                        arq.write(str(lineNumber-1))
                                        arq.write(";")
                                        arq.write("DELETED")
                                        arq.write(";")
                                        arq.write(lista.author.name)
                                        arq.write(";")
                                        arq.write(lista.author.email)
                                        arq.write(";")
                                        arq.write(str(lista.author_date))
                                        arq.write(";")
                                        arq.write(lista.hash)
                                        if jasalvou == False:
                                        	arq.write(";")
                                        	arq.write('"'+lista.msg.replace("\n", " ")+'"'+"\n")
                                        	jasalvou=True
                                        else:
                                        	arq.write(";")
                                        	arq.write('""'+"\n")

                                        arq.close()
                                    else:
                                        arq = open(nomedotxt, 'w')
                                        arq.write("Filename")
                                        arq.write(";")
                                        arq.write("Linha")
                                        arq.write(";")
                                        arq.write("Tipo")
                                        arq.write(";")
                                        arq.write("Autor")
                                        arq.write(";")
                                        arq.write("Email")
                                        arq.write(";")
                                        arq.write("Data")
                                        arq.write(";")
                                        arq.write("Hash\n")
                                        arq.write(modification.filename)
                                        arq.write(";")
                                        arq.write(str(lineNumber-1))
                                        arq.write(";")
                                        arq.write("DELETED")
                                        arq.write(";")
                                        arq.write(lista.author.name)
                                        arq.write(";")
                                        arq.write(lista.author.email)
                                        arq.write(";")
                                        arq.write(str(lista.author_date))
                                        arq.write(";")
                                        arq.write(lista.hash)
                                        arq.write(";")
                                        arq.write('"'+lista.msg.replace("\n", " ")+'"'+"\n")   
                                        arq.close()
                                        jasalvou=True
                        auxiliar=lineStr
                        linhaanterior=lineNumber;
                       
                        #if re.search("except.*:.*", lineStr):
                            #print("remove"+lista.hash)
                        #print("Deleted line {} - {}".format(lineNumber, lineStr))
    print(Salvarlista)
                
                
