from flask import Flask, jsonify, request, session, flash
from main import app, db
from models import Receitas, Despesas, Guardar

#=============================EXIBIR RECEITA==========================
@app.route('/receita', methods = ['GET'])
def get_receita():

    receitas = Receitas.query.all()
    receitas_dic = []

    for rece in receitas:
        rece_dic = {
            'id_receitas': rece.id_receitas,
            'nome': rece.nome,
            'valor': rece.valor,
            'data': rece.data
        }
        receitas_dic.append(rece_dic)

    return jsonify(
        mensagem='Lista das Receitas',
        receitas=receitas_dic
    )

#=============================CADASTRAR RECEITA==========================
@app.route('/receita', methods=['POST'])
def post_receita():
    receita = request.json

    nova_receita = Receitas(
        id_receitas=receita.get('id_receitas'),
        nome=receita.get('nome'),
        valor=receita.get('valor'),
        data=receita.get('data')
    )

    db.session.add(nova_receita)
    db.session.commit()

    return jsonify(
        mensagem='Receita Cadastrada com Sucesso',
        receitas={
            'id_receitas': nova_receita.id_receitas,
            'nome': nova_receita.nome,
            'valor': nova_receita.valor,
            'data': nova_receita.data
        }
    )





#=============================EXIBIR DESPESA==========================
@app.route('/despesa', methods = ['GET'])
def get_despesa():

    despesas = Despesas.query.all()
    despesas_dic = []

    for despe in despesas:
        despe_dic = {
            'id_despesas': despe.id_despesas,
            'nome': despe.nome,
            'valor': despe.valor,
            'data': despe.data
        }
        despesas_dic.append(despe_dic)

    return jsonify(
        mensagem='Lista das Despesas',
        despesas=despesas_dic
    )

#=============================CADASTRAR DESPESA=======================
@app.route('/despesa', methods=['POST'])
def post_despesa():
    despesa = request.json

    nova_despesa = Despesas(
        id_despesas=despesa.get('id_despesas'),
        nome=despesa.get('nome'),
        valor=despesa.get('valor'),
        data=despesa.get('data')
    )

    db.session.add(nova_despesa)
    db.session.commit()

    return jsonify(
        mensagem='Despesa Cadastrada com Sucesso',
        despesas={
            'id_despesas': nova_despesa.id_despesas,
            'nome': nova_despesa.nome,
            'valor': nova_despesa.valor,
            'data': nova_despesa.data
        }
    )






#=============================EXIBIR GUARDAR==========================
@app.route('/guardar', methods = ['GET'])
def get_guardar():

    guardar = Guardar.query.all()
    guardar_dic = []

    for guar in guardar:
        guar_dic = {
            'id_guardar': guar.id_guardar,
            'nome': guar.nome,
            'valor': guar.valor,
            'data': guar.data
        }
        guardar_dic.append(guar_dic)

    return jsonify(
        mensagem='Lista de Dinheiro Guardado',
        guardar=guardar_dic
    )

#=============================CADASTRAR GUARDAR=======================
@app.route('/guardar', methods=['POST'])
def post_guardar():
    guardar = request.json

    novo_guardar = Guardar(
        id_guardar=guardar.get('id_guardar'),
        nome=guardar.get('nome'),
        valor=guardar.get('valor'),
        data=guardar.get('data')
    )

    db.session.add(novo_guardar)
    db.session.commit()

    return jsonify(
        mensagem='Dinheiro guardado com Sucesso',
        guardar={
            'id_guardar': novo_guardar.id_guardar,
            'nome': novo_guardar.nome,
            'valor': novo_guardar.valor,
            'data': novo_guardar.data
        }
    )



#========================DELETAR RECEITAS============================
@app.route('/receita/<int:id_receitas>', methods=['DELETE'])
def delete_receita(id_receitas):

    receita = Receitas.query.get(id_receitas)

    if receita:
        # Remove a receita do banco de dados
        db.session.delete(receita)
        db.session.commit()

        return jsonify({'mensagem': 'Receita excluída com sucesso'})
    else:
        return jsonify({'mensagem': 'Receita não encontrada'})




#========================DELETAR DESPESA============================
@app.route('/despesa/<int:id_despesas>', methods=['DELETE'])
def delete_despesa(id_despesas):
    despesa = Despesas.query.get(id_despesas)

    if despesa:
        db.session.delete(despesa)
        db.session.commit()

        return jsonify({'mensagem': 'Despesa excluída com sucesso'})
    else:
        return jsonify({'mensagem': 'Despesa não encontrada'})



#========================DELETAR GUARDAR============================
@app.route('/guardar/<int:id_guardar>', methods=['DELETE'])
def delete_guardar(id_guardar):
    guardar = Guardar.query.get(id_guardar)

    if guardar:
        db.session.delete(guardar)
        db.session.commit()

        return jsonify({'mensagem': 'Dinheiro Guardado excluída com sucesso'})
    else:
        return jsonify({'mensagem': 'Dinheiro Guardado não encontrada'})
