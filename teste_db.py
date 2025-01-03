from centraliza import db, Tarefa, Subtarefa, app


with app.app_context():
    db.create_all()

    # Inserir dados
    tarefa1 = Tarefa(nome="Limpar a casa", descricao="Organizar e limpar toda a casa")
    subtarefa1_1 = Subtarefa(sub_nome="Lavar a louça", tarefa=tarefa1)
    subtarefa1_2 = Subtarefa(sub_nome="Varrer o chão", tarefa=tarefa1)

    tarefa2 = Tarefa(
        nome="Se preparar para a semana",
        descricao="As coisas que devo fazer para me preparar para a semana"
    )
    subtarefa2_1 = Subtarefa(sub_nome="Ajustar Alarmes", tarefa=tarefa2)
    subtarefa2_2 = Subtarefa(sub_nome="Comprar Comida", tarefa=tarefa2)

    db.session.add_all([tarefa1, subtarefa1_1, subtarefa1_2, tarefa2, subtarefa2_1, subtarefa2_2])
    db.session.commit()

    print("Banco de dados populado com sucesso!")
#Execute esse arquivo pra criar os exemplos dentro do banco de dados pra conseguir visualizar ele