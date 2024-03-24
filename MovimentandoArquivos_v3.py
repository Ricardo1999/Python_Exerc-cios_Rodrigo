

import os

#Essa funcao eu fiz para listar os arquivos do diretorio destino depois de mover o arquivo.
def consulta_dir(endereco):
	#Lista os arquivos do destino
	x = -1
	posicao = 0

	#Passo pela string iterando o x para salvar a posicao do ultimo "\\"
	for i in endereco :
		#print(i)
		x += 1
		if(i=="\\"):
			posicao = x
			#letradaposicao = i
	nova_string = endereco[0:posicao]
	return nova_string

#Recebe origem e destino
origem = input('local de origem: ')
destino = input('local de destino: ')
#destino_consulta = input('local de destino para consulta: ')

#Movimenta os arquivos
os.rename(origem, destino)


resultado = os.listdir(consulta_dir(destino))
print(resultado)
