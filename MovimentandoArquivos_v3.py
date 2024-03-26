

import os

#Essa funcao eu fiz para listar os arquivos do diretorio destino depois de mover o arquivo.
def consulta_dir(endereco):
	#Lista os arquivos do destino
	
	#Inicia a contagem no -1 para a variável posicao seguir a indexacao que inicia em 0
	x = -1 # 

	#posição final da string que antecede o "\"
	posicao = 0

	#Passo pela string iterando o x para salvar a posicao do ultimo "\\"
	for i in endereco :
		x += 1
		if(i=="\\"):
			posicao = x
	nova_string = endereco[0:posicao]
	return nova_string

#Recebe origem e destino
origem = input('local de origem: ')
destino = input('local de destino: ')

#Movimenta os arquivos
os.rename(origem, destino)

#Consulta o endereco de Destino para saber se o arquivo foi movido.
resultado = os.listdir(consulta_dir(destino))
print(resultado)
