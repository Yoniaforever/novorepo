#Uma escola está organizando sua primeira olimpíada do conhecimento e deseja separar 
# os 100 alunos em dois grupos de 50. Além de testar os conhecimentos dos alunos, 
# querem estimular a formação de novos laços sociais e, por isso, a divisão dos grupos de alunos será feita 
# seguindo um critério

matriculas = int(input("o numero da matricula é?"))

def verificador_de_time(matriculas):
    if matriculas %2 == 0:
        print ("Bem vindo ao time Azul!!")
    else:
        print ("Bem vindo ao time amarelo!!")

verificador_de_time(matriculas)