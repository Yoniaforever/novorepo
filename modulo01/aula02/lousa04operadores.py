cidade = input("qual sua cidade?")
idade = int(input("qual sua idade?"))

if cidade != "salvador" and idade <=18:
    print("not passed")
if cidade == "salvador" and idade >=18:
    print("passed")