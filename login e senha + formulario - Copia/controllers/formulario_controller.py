from models.formulario_model import FormularioModel  

class FormularioController:

    @staticmethod
    def create_formulario(user_id, data):
        nome = data.get('nome')  
        email = data.get('email') 
        data_nascimento = data.get('data_nascimento') 
        cpf = data.get('cpf')  
        genero = data.get('genero')  

        if not nome or not email or not data_nascimento or not cpf or not genero:
            return {"error": "Todos os campos são obrigatórios"}, 400  

        formulario = FormularioModel.create_formulario(user_id, nome, email, data_nascimento, cpf, genero)
        if formulario:
            return {"message": "Formulário criado com sucesso"}, 201
        return {"error": "Erro ao criar formulário"}, 500 

    @staticmethod
    def get_formulario(user_id):
        # Busca o formulário no banco de dados usando o ID do usuário.
        formulario = FormularioModel.find_by_user_id(user_id)
        if formulario:
            return {"id": formulario['id'], "nome": formulario['nome'], "email": formulario['email'], 
                    "data_nascimento": formulario['data_nascimento'], "cpf": formulario['cpf'], 
                    "genero": formulario['genero']}, 200  # Retorna os dados do formulário encontrado.
        return {"error": "Formulário não encontrado"}, 404  # Retorna erro se o formulário não for encontrado.