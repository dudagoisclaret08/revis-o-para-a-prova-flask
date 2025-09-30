from flask import Flask, request

app = Flask(__name__) ### chama a funçao Flask 

# Rota de Login
@app.route('/login', methods=['GET', 'POST'])
 
def login():
    if request.method == 'POST': ### quando clica no botao post
        nome = request.form['nome']  ## pega o que a pessoa escreveu 
        idade = request.form['idade'] ###pega o que a pessoa escreveu
        return '''
            <h2>Bem-vindo {}, {} anos, ao sistema!</h2>
            <a href="/login">Voltar</a>
        '''.format(nome, idade)  ### mostra a mensagem escrito bem vindo, junto com idade e nome
    return '''
        <form method="post">
            Nome: <input type="text" name="nome"><br>
            Idade: <input type="number" name="idade"><br>
            <input type="submit" value="Entrar">
        </form>
    ''' ### mostra a mensagem escrito bem vindo, junto com idade e nome 

# Rota da Calculadora
@app.route('/calculadora', methods=['GET', 'POST'])  ### chama a funçao calculadora com GET E POST 

def calculadora(): ### chama a funçao 

    if request.method == 'POST':  #### se apertar a funçao calculadora vai ser pedido os numeros 
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2']) 
            operacao = request.form['operacao']
            resultado = "" #### ve qual operaçao a pessoa escolheu, ou seja, os numeros 

            if operacao == 'soma':
                resultado = "{} + {} = {}".format(num1, num2, num1 + num2) # faz a soma 
            elif operacao == 'subtracao':
                resultado = "{} - {} = {}".format(num1, num2, num1 - num2) # faz a subtraçao
            elif operacao == 'multiplicacao':
                resultado = "{} * {} = {}".format(num1, num2, num1 * num2) # faz a multiplicaçao 
            elif operacao == 'divisao':
                if num2 != 0:
                    resultado = "{} / {} = {}".format(num1, num2, num1 / num2) # faz a divisao 
                else:
                    resultado = "Erro: Divisão por zero!" ## se for dividir por 0 vai dar erro 
            else:
                resultado = "Operação inválida!" # mostra que dividir por 0 vai ser inváçido 

            return '''
                <h2>Resultado: {}</h2>
                <a href="/calculadora">Voltar</a> 
            '''.format(resultado)
        except ValueError: ### mostra o erro 
            return "Erro: Certifique-se de digitar números válidos." #### retorna o valor errado e volta para pagina inicial (<h2>Resultado: {}</h2>)

    return '''
        <form method="post">
            Número 1: <input type="text" name="num1"><br>
            Número 2: <input type="text" name="num2"><br>
            Operação:
            <select name="operacao">
                <option value="soma">Soma</option>
                <option value="subtracao">Subtração</option>
                <option value="multiplicacao">Multiplicação</option>
                <option value="divisao">Divisão</option>
            </select><br>
            <input type="submit" value="Calcular">
        </form>
    ''' ##### retorna a opçao escolhida para fazer a conta 




#aula 
# Rodar o servidor
if __name__ == '__main__':
    app.run(debug=True)




from flask import Flask


app = Flask(__name__)


@app.route('/') # definindo uma rota
def home():
    return 'Seja bem vindo'

# CALCULADORA
@app.route('/calculadora/soma/<int:n1>/<int:n2>') # definindo uma rota
def soma(n1,n2):
    # resultado = n1 + n2
    return f'Somando os valores {n1} e {n2} = {n1 + n2}'

@app.route('/calculadora/divisao/<int:n1>/<int:n2>') # definindo uma rota
def divisao(n1,n2):
    # resultado = n1 + n2
    if n2 == 0:
        return f'Esta invalido'
    else:
        return f'Somando os valores {n1} e {n2} = {n1 / n2}'

@app.route('/calculadora/multiplicacao/<int:n1>/<int:n2>') # definindo uma rota
def multiplicacao(n1,n2):
    # resultado = n1 + n2
    return f'Somando os valores {n1} e {n2} = {n1 * n2}'

@app.route('/calculadora/subtracao/<int:n1>/<int:n2>') # definindo uma rota
def subtracao(n1,n2):
    # resultado = n1 + n2
    return f'Somando os valores {n1} e {n2} = {n1 - n2}'









# PARA DEIXAR O CÓDIGO RODANDO
if __name__ == "__main__":
    app.run(debug=True)
