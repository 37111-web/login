from flask import Blueprint, request, jsonify  
from controllers.user_controller import UserController 

user_bp = Blueprint('users', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    return jsonify(UserController.register_user(request.get_json()))

@user_bp.route('/login', methods=['POST'])
def login():
    return jsonify(UserController.login_user(request.get_json()))


@user_bp.route("/login", methods=["GET"])
def pegar_login():
    return jsonify(listar_login())


# GET POR ID
@user_bp.route("/register/<int:id>", methods=["GET"])
def pegar_register_por_id(id):
    aluno = buscar_register_por_id(id)

    if aluno:
        return jsonify(aluno)

    return jsonify({"mensagem": "Aluno não encontrado"}), 404


# PUT
@user_bp.route("/login/<int:id>", methods=["PUT"])
def editar_aluno(id):
    dados = request.json

    aluno = atualizar_aluno(id, dados)

    if aluno:
        return jsonify({
            "mensagem": "Aluno atualizado com sucesso",
            "aluno": aluno
        })

    return jsonify({"mensagem": "Aluno não encontrado"}), 404

# DELETE
@user_bp.route("/login/<int:id>", methods=["DELETE"])
def deletar_aluno(id):
    excluido = excluir_aluno(id)

    if excluido:
        return jsonify({
            "mensagem": f"Aluno {id} excluído com sucesso"
        })

    return jsonify({
        "mensagem": "Aluno não encontrado"
    }), 404