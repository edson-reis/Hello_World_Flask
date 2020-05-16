from flask  import Flask
app = Flask(__name__)

@app.route("/<param1>", methods=['GET','POST'])
def ola(param1):
    return 'Hello World - Aplicação em Python/Flask - {}'.format(param1)

if __name__=="__main__":
    app.run(debug=True) #usar debug somente em desenvolvimento
