from flask import Flask, jsonify, request

app = Flask(__name__)

# dados fictícios para nossa API
alunos = [
    {"id": 1, "Aluno": "Ana Clara", "Idade": "17 anos", "Cursando": "Programacao com Py"},
    {"id": 2, "Aluno": "Marcos", "Idade": "16 anos", "Cursando": "Programacao com Py"},
    {"id": 3, "Aluno": "Vitor", "Idade": "18 anos", "Cursando": "Programacao com Py"},
    {"id": 4, "Aluno": "Kauã", "Idade": "17 anos", "Cursando": "Programacao com Py"},
    {"id": 5, "Aluno": "Abner", "Idade": "17 anos", "Cursando": "Programacao com Py"},
    {"id": 6, "Aluno": "Julia", "Idade": "17 anos", "Cursando": "Programacao com Py"},
    {"id": 7, "Aluno": "Ana Rita", "Idade": "19 anos", "Cursando": "Programacao com Py"}
]

# rota inicial
@app.route("/")
def home():
    return "🚀 API de Alunos funcionando!"

@app.route("/alunosn", methods=["GET"])
def listar_alunos():
    return jsonify(alunos)

@app.route("/alunosn", methods=["POST"])
def adicionar_aluno():
    novo_aluno = request.get_json()
    alunos.append(novo_aluno)
    return jsonify({"mensagem": "Aluno adicionado com sucesso!", "aluno": novo_aluno})

@app.route("/alunosn/<int:id>", methods=["PUT"])
def atualizar_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            dados = request.get_json()
            aluno.update(dados)
            return jsonify({"mensagem": "Aluno atualizado!", "aluno": aluno})
    return jsonify({"erro": "Aluno não encontrado!"}), 404

@app.route("/alunosn/<int:id>", methods=["DELETE"])
def deletar_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            alunos.remove(aluno)
            return jsonify({"mensagem": "Aluno removido!"})
    return jsonify({"erro": "Aluno não encontrado!"}), 404

if __name__ == "__main__":
    app.run(debug=True)