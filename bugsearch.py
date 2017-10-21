import requests as r ; import sys ; import json ; import argparse as arg ; import os as sistema ; import time
sistema.system("cls" if sistema.name == "nt" else "reset")
menu = """
__  __            __                  ______   Recoda nao comedia!              
\ \/ /_  ______  / /_____  __________/ ____/_______ _      __
 \  / / / / __ \/ //_/ _ \/ ___/ ___/ /   / ___/ _ \ | /| / /
 / / /_/ / / / / ,< /  __/ /  (__  ) /___/ /  /  __/ |/ |/ / 
/_/\__,_/_/ /_/_/|_|\___/_/  /____/\____/_/   \___/|__/|__/  
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
 # Bug Search v1
 # Escrito por Supr3m0
 # Contato: www.facebook.com/yunkers01/
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"""
manual = """--cms (-c)           Tipo de CMS
--filtro (-f)        Filtra a pesquisa procurando um tipo de falha.
--salvar (-S)        Salva todos resultados em um arquivo 'yc.txt'."""
parser = arg.ArgumentParser()
parser.add_argument("--cms", "-c", action="store")
parser.add_argument("--filtro", "-f", action="store")
parser.add_argument("--salvar", "-S", action="store_true")
param = parser.parse_args()
api = "http://www.exploitalert.com/api/search-exploit?name={}".format(param.cms)
if len(sys.argv) == 1:
	print(menu) ; print(manual) ; exit()
def inicio():
	print(menu) ; print("[*] Verificando conexão...")
	try: api_req = r.get(api) ; print("    * OK!")
	except Exception as err: print("[x] Site 'www.exploitalert.com' está fora do ar.", err) ; exit("\n")
	print("[*] Decodificando JSON...")
	try: api_decode = json.loads(api_req.text) ; print("    * OK!")
	except: print("[x] Impossivel decodificar o json do site 'www.exploitalert.com'.") ; exit("\n")
	sys.stdout.write("\n[*] Listando exploits") ; sys.stdout.flush()
	for i in range(3):
		time.sleep(0.3)
		sys.stdout.write(".") ; sys.stdout.flush()
	if param.filtro: filtro_api(param.filtro, api_decode)
	else: normal_api(api_decode)
def filtro_api(filtro_usuario, pagina):
	contador = 0
	lista_ = []
	for xpl in pagina:
		if filtro_usuario in xpl["name"]:
			reference = "http://www.exploitalert.com/view-details.html?id={}".format(xpl["id"])
			print("\n* Nome: {} / * Data: {} / * Id: {}\n * POC: {}".format(xpl["name"], xpl["date"], xpl["id"], reference))
			contador +=1
			lista_.append("* Nome: {} / * Data: {} / * Id: {}\n * POC: {}".format(xpl["name"], xpl["date"], xpl["id"], reference))
		else: continue
	print("\n* Total de exploits:",str(contador))
	if param.salvar: salvar_resultados(lista_)
def normal_api(pagina):
	lista_ = []
	for xpl in pagina:
		reference = "http://www.exploitalert.com/view-details.html?id={}".format(xpl["id"])
		print("\n* Nome: {} / * Data: {} / * Id: {}\n * POC: {}".format(xpl["name"], xpl["date"], xpl["id"], reference))
		lista_.append("* Nome: {} / * Data: {} / * Id: {}\n * POC: {}".format(xpl["name"], xpl["date"], xpl["id"], reference))
	print("\n* Total de exploits:",str(len(pagina)))
	if param.salvar: salvar_resultados(lista_)
def salvar_resultados(lista):
	print("\n[*] Salvando resultados...")
	arquivo = open("yc.txt", "w")
	arquivo = [arquivo.write(str(x) + "\n") for x in lista]
try:inicio()
except KeyboardInterrupt: exit("\n")
