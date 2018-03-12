#!/usr/bin/env python3
"""
This code is under Apache License 2.0
Written by B_Gameiro (Bernardo Bernardino Gameiro) e Fran
More in 
  SoloLearn: https://www.sololearn.com/Profile/8198571
  GitHub: https://github.com/BGameiro76
  Repl.it: https://repl.it/@B_Gameiro

Programa para realizar os calculos da atividade laboratorial 1.3 de Física do 12º ano relativa à colisão de um carrinho numa calha de baixo atrito com uma mola.
"""
from sys import exit as end
Sim_expressions = ["Yes", "Y", "y", "yes", "Sim", "sim", "S", "s", "YES", "SIM"]
Nao_expressions = ["No", "no", "N", "n", "NO", "Não", "não", "NÃO", "Nao", "nao", "NAO"]
#Welcome
print("Bem vindo à cálculadora para a A.L. 1.3 (parte 1) de Física de 12º ano.\n\nNesta atividade vamos estudar a colisão entre um carro numa calha de baixo atrito com uma mola na extremidade desta.\nSerá utilizada uma célula fotovoltaica para calcular a velocidade do carro antes e depois da colisão.\nPara efetuar este cálculo deve se dividir a largura de uma banda que interrompa o feixe da célula fotovoltaica pelo intervalo de tempo que este for interrompido.\nDeve considerar-se que a velocidade se mantém constante durante o intervalo de tempo em que o feixe está interrompido, visto este ser tão reduzido.")
while True:
	while True:
#Input da massa do carrinho e conversão para Kg.
		massa = input("\n\nInsira a massa do carrinho (g):")
		try:
			massa = float(massa)
			break
		except:
			print("O que inseriu não é válido.")
	massa_Kg = massa * 0.001
#Input do comprimento da banda de cor escura e conversão para m.
	while True:
		Picket_fence = input("Insira o comprimento da faixa escura do picket fence (cm):")
		try:
			Picket_fence = float(Picket_fence)
			break
		except:
			print("O que inseriu não é válido.")
	Picket_fence_m = Picket_fence * 0.01
#Input do intervalo de tempo que a célula fotovoltaica 1 esteve interrompida (antes da colisão).
	while True:
		Δt_i = input("Insira o primeiro intervalo de tempo (s):")
		try:
			Δt_i = float(Δt_i)
			break
		except:
			print("O que inseriu não é válido.")
#Input do intervalo de tempo que a célula fotovoltaica 2 esteve interrompida (depois da colisão).
	while True:
		Δt_f = input("Insira o segundo intervalo de tempo (s):")
		try:
			Δt_f = float(Δt_f)
			break
		except:
			print("O que inseriu não é válido.")
#Cálculo das velocidades (Δx/Δt).
	v_i = Picket_fence_m / Δt_i
	v_f = Picket_fence_m / Δt_f
#Cálculo do momento linear (m*v).
	p_i = massa_Kg * v_i
	p_f = massa_Kg * v_f
#Cálculo da energia cinética ((1/2)*m*v^2).
	E_c_i = 0.5 * massa_Kg * (v_i ** 2)
	E_c_f = 0.5 * massa_Kg * (v_f ** 2)
#Cálculo do coeficiente de restituição da velocidade após a colisão com a mola (vf/vi).
	Coef_restituicao = v_f / v_i
#Conversão dos floats em strings.
	massa_Kg_str = str(massa_Kg)
	Picket_fence_m_str = str(Picket_fence_m)
	Δt_i_str = str(Δt_i)
	Δt_f_str = str(Δt_f)
#Menu de confirmação dos inputs.
	while True:
		print("\n\nSão estes os valores que pretende usar?\n" + "\nMassa (Kg):" + massa_Kg_str + "\nComprimento da faixa escura (m):" + Picket_fence_m_str + "\n1º intervalo de tempo (s):" + Δt_i_str + "\n2º intervalo de tempo (s):" + Δt_f_str)
		user_decision_1 = input("\n(sim/não):")
#Resultados.
		if user_decision_1 in Sim_expressions:
			v_i_str = str(v_i)
			v_f_str = str(v_f)
			p_i_str = str(p_i)
			p_f_str = str(p_f)
			E_c_i_str = str(E_c_i)
			E_c_f_str = str(E_c_f)
			Coef_restituicao_str = str(Coef_restituicao)
			print("\nResultados:\n\nVelocidade inicial (m/s):" + v_i_str + "\nVelocidade final (m/s):" + v_f_str + "\nMomento Linear inicial (kg.m/s):" + p_i_str + "\nMomento Linear final (kg.m/s):" + p_f_str + "\nEnergia cinética inicial (J):" + E_c_i_str + "\nEnergia cinética final (J):" + E_c_f_str + "\nCoeficiente de restituição:" + Coef_restituicao_str)
			while True:
				user_decision_2 = input("\n\nDeseja fazer mais um ensaio?\n(sim/não):")
				if user_decision_2 in Sim_expressions:
					print("\n")
					break
				elif user_decision_2 in Nao_expressions:
					end("\n\n\nA fechar programa...")
				else:
					print("O que introduziu não é válido.")
			break
#Substituição dos inputs.
		elif user_decision_1 in Nao_expressions:
			print("\n")
			break
		else:
			print("O que introduziu não é válido.")