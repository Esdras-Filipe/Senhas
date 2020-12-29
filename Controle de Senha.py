import os;
import sys
import random

class Chamada:
    SenhasG = [];
    SenhasP = [];

def menu():
 cha = Chamada();
 print(" ");
 print("1 - CADASTRAR NOVA SENHA.");
 print("2 - ADASTRAR NOVA SENHA PREFERNCIAL.");
 print("3 - FINALIZAR ATENDIMENTO.");
 print("4 - FINALIZAR ATENDIMENTO PREFERENCIAL.");
 print("5 - MOSTRAR SENHAS CADASTRADAS.");
 print("6 - MOSTRAR SENHAS PREFERENCIAIS CADASTRADAS.");
 print("7 - MOSTRAR PROXIMA SENHA.");
 print("8 - MOSTRAR PROXIMA SENHA PREFERENCIAL.");
 print("9 - SAIR.");
 opcao = int(input("Informe a opção: "));
 if(opcao == 1):
     cadastro(cha)
 elif(opcao == 2):
     preferencia(cha)
 elif(opcao == 3):
     finaliza(cha)
 elif(opcao == 4):
     finaliza2(cha)
 elif(opcao == 5):
     mostra(cha)
 elif(opcao == 6):
     mostra2(cha)
 elif(opcao == 7):
     proxima(cha)
 elif(opcao == 8):
     proxima2(cha)
 elif(opcao == 9):
     sys.exit(0);
 else:
     print("Opção inválida");
     os.system("cls");
     menu();

def cadastro(cha):
  r="s"
  while(r=="s" or r=="S" or r=="Sim" or r=="SIM" or r=="sim"):
     x = random.sample(range(1000,10000), 1);
     x = str(x);
     cha.SenhasG.append("N" + x);
     print("Senha cadastrada com sucesso!!");
     r = input("Cadastrar uma nova senha? ");
     while(r!="não" and r!="nao" and r!="N" and r!="n" and r!="NÃO" and   r!="Não" and r!="s" and r!="S" and r!="Sim" and r!="SIM" and       r!="sim"):
         print("OPÇÃO INVALIDA!!");
         print("TENTE NOVAMENTE");
         r = input("Cadastrar uma nova senha? ");
     print(cha.SenhasG);
  else:
      menu();


def finaliza(cha):
  if (len(cha.SenhasG)==0):
    print("NÃO HÁ ATENDIMENTOS A SEREM FINALIZADOS!");
    menu();
  del(cha.SenhasG[0]);
  print("ATENDIMENTO FINALIZADO COM SUCESSO!!");
  menu();


def mostra(cha):
  if (len(cha.SenhasG)==0):
    print("NENHUMA SENHA CADASTRADA!!");
    print("CADASTRE UMA SENHA ANTES.");
    menu();
  else:
   print("SENHAS CADASTRADAS: ",cha.SenhasG);
   menu();


def proxima(cha):
  if (len(cha.SenhasG)==0):
    print("NENHUMA SENHA CADASTRADA!!");
    print("CADASTRE UMA SENHA ANTES.");
    menu();
  else:
    if(len(cha.SenhasG) == 1):
      print("NÃO EXISTE PROXIMA SENHA!");
      menu();
    print("A PROXIMA SENHA É : ",cha.SenhasG[1]);
    menu();


def preferencia(cha):
  r="s"
  while(r=="s" or r=="S" or r=="Sim" or r=="SIM" or r=="sim"):
      x=random.sample(range(2000,30000), 1);
      x=str(x);
      cha.SenhasP.append("P"+x);
      print("Senha preferencial cadastrada com sucesso!!");
      r = input("Cadastrar uma nova senha? ");
      while(r!="não" and r!="nao" and r!="N" and r!="n" and r!="NÃO" and  r!="NAO" and r!="Não" and r!="s" and r!="S" and r!="Sim" and r!="SIM" and  r!="sim"):
         print("OPÇÃO INVALIDA!!");
         print("TENTE NOVAMENTE") ;
         r = input("Cadastrar uma nova senha? ");
      print(cha.SenhasP);
  menu()


def finaliza2(cha):
  if (len(cha.SenhasP)==0):
    print("NÃO HÁ ATENDIMENTOS A SEREM FINALIZADOS!");
    menu();
  del(cha.SenhasP[0]);
  print("ATENDIMENTO FINALIZADO COM SUCESSO!!");
  menu();


def mostra2(cha):
  if (len(cha.SenhasP)==0):
    print("NENHUMA SENHA CADASTRADA!!");
    print("CADASTRE UMA SENHA ANTES.");
    menu();
  else:
   print("SENHAS PREFERENCIAIS CADASTRADAS: ",cha.SenhasP);
   menu();

def proxima2(cha):
  if (len(cha.SenhasP)==0):
    print("NENHUMA SENHA CADASTRADA!!");
    print("CADASTRE UMA SENHA ANTES.");
    menu();
  else:
    if(len(cha.SenhasP) == 1):
      print("NÃO EXISTE PROXIMA SENHA!");
      menu();
    else:
      print("A PROXIMA SENHA PREFERENCIAL É : ",cha.SenhasP[1]);
      menu();

menu();