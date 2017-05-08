from bottle import run, get, post, request, redirect, view
import requests, bottle, json, threading, time, sys

historico = []
peers = sys.argv[2:]

print(peers)

@get('/home')
def index():
    form = '''
        <h3>Bem vindo ao Chat, digite seu nome e mensagem a baixo:</h3>
	<form action="/send" method="post">
		Nome:<br><input type="text" name="name" required><br>
		Mensagem:<br><input type="text" name="mensagem" required>
		<input value="Enviar" type="submit"/>
	</form>
	'''
    '<h1>Lista com as mensagens enviadas :</h1>'
    for i in historico:form+= "Usuário <b>"+i[0]+"</b>: Disse: <i>"+i[1]+"</i><br>"	
    return form

@post('/send')
def index2():
    nome = request.forms.get('name')
    mensagem = request.forms.get('mensagem')
    historico.append([nome, mensagem])
    redirect('/home')

@get('/peers')
def index():
	return json.dumps(peers)

@get('/historico')
def index():
	return json.dumps(historico)

def clientePeers():
	time.sleep(5)
	while True:
		time.sleep(1)
		np = []
		for p in peers:
			r = requests.get(p + '/peers')
			np = np + json.loads(r.text)
		peers[:] = list(set(np + peers))
		print(peers)
		time.sleep(2)

def clienteMenssages():
	time.sleep(5)
	while True:
		nm = []
		for p in peers:
			m = requests.get(p + '/historico')
			nms = json.loads(m.text)
			for msg in nms:
					if msg not in historico:
						historico.append(msg)
		time.sleep(2)

t1 = threading.Thread(target=clientePeers)
t1.start()

t2 = threading.Thread(target=clienteMenssages)
t2.start()


run(host='localhost', port=int(sys.argv[1]))
