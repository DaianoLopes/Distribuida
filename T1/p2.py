from bottle import run, get, post, request, redirect

historico = []

@get('/home')
def index():
    form = '''
        <h3>Bem vindo ao Chat, digite seu nome e mensagem a baixo:</h3>
	<form action="/send" method="post">
		Nome:<br><input type="text" name="name"><br>
		Mensagem:<br><input type="text" name="mensagem">
		<input value="Enviar" type="submit"/>
	</form>
	'''
    for i in historico:form+= "Usuário <b>"+i[0]+"</b>: Disse: <i>"+i[1]+"</i><br>"	
    return form


@post('/send')
def index2():
    nome = request.forms.get('name')
    mensagem = request.forms.get('mensagem')
    historico.append([nome, mensagem])
    redirect('/home')
	
run(host='localhost', port=8080)
