from bottle import run, get, post, request, redirect

from datetime import datetime
now = datetime.now()


historico = []

@get('/home')
def index():
    form = '''
	<form action="/send" method="post">
		Nome:<br><input type="text" name="nome"><br>
		Mensagem:<br><input type="text" name="mensagem">
		<input value="Enviar" type="submit"/>
	</form>
	'''
    #now = datetime.now()


    for i in historico:form+= i[0]+"Usuário <b>"+i[1]+"</b>: Disse: <i>"+i[2]+"</i><br>"
    return form

#str(now.hour)+str(now.minute)+ tava antes do "Usuário"

@post('/send')
def index2():
    nome = request.forms.get('nome')
    mensagem = request.forms.get('mensagem')
    hora = str(now.hour)+str(now.minute)
    historico.append([hora,nome, mensagem])
    redirect('/home')
	
run(host='localhost', port=8080)
