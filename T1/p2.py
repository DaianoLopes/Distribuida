from bottle import run, get, post, request, redirect

from datetime import datetime
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
    for i in historico:form+= "Usuário <b>"+i[0]+"</b>: Disse: <i>"+i[1]+"</i><br>"	
    return form


@post('/send')
def index2():
    nome = request.forms.get('nome')
    mensagem = request.forms.get('mensagem')
    historico.append([nome, mensagem])
    redirect('/home')
	
run(host='localhost', port=8080)
