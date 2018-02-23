while True:
	while True:
"""
Input da massa do carrinho e conversão para Kg.
"""
		massa = input("Insira a massa do carrinho (g):")
		try:
			massa = float(massa)
			break
		except:
			print("O que inseriu não é válido.")
	massa_Kg = massa * 0.001
"""
Input do comprimento da banda de cor escura e conversão para m.
"""
	while True:
		Picket_fence = input("Insira o comprimento da faixa escura do picket fence (cm):")
		try:
			Picket_fence = float(Picket_fence)
			break
		except:
			print("O que inseriu não é válido.")
	Picket_fence_m = Picket_fence * 0.01
"""
Input do intervalo de tempo que a célula fotovoltaica 1 esteve interrompida (antes da colisão).
"""
	while True:
		Δt_i = input("Insira o primeiro intervalo de tempo (s):")
		try:
			Δt_i = float(Δt_i)
			break
		except:
			print("O que inseriu não é válido.")
"""
Input do intervalo de tempo que a célula fotovoltaica 2 esteve interrompida (depois da colisão).
"""
	while True:
		Δt_f = input("Insira o segundo intervalo de tempo (s):")
		try:
			Δt_f = float(Δt_f)
			break
		except:
			print("O que inseriu não é válido.")
"""
Cálculo das velocidades (Δx/Δt).
"""
	v_i = Picket_fence_m / Δt_i
	v_f = Picket_fence_m / Δt_f
"""
Cálculo do momento linear (m*v).
"""
	p_i = massa_Kg * v_i
	p_f = massa_Kg * v_f
"""
Cálculo da energia cinética ((1/2)*m*v^2).
"""
	E_c_i = 0.5 * massa_Kg * (v_i ** 2)
	E_c_f = 0.5 * massa_Kg * (v_f ** 2)
"""
Cálculo do coeficiente de restituição da velocidade após a colisão com a mola (vf/vi).
"""
	Coef_restituicao = v_f / v_i
"""
Conversão dos floats em strings.
"""
	massa_Kg_str = str(massa_Kg)
	Picket_fence_m_str = str(Picket_fence_m)
	Δt_i_str = str(Δt_i)
	Δt_f_str = str(Δt_f)
"""
Menu de confirmação dos inputs.
"""
	print("\n\nSão estes os valores que pretende usar?\n" + "\nMassa (Kg):" + massa_Kg_str + "\nComprimento da faixa escura (m):" + Picket_fence_m_str + "\n1º intervalo de tempo (s):" + Δt_i_str + "\n2º intervalo de tempo (s):" + Δt_f_str)
	user_decision_1 = input("\n(sim/não):")
"""
Resultados.
"""
	if user_decision_1 == "sim":
		v_i_str = str(v_i)
		v_f_str = str(v_f)
		p_i_str = str(p_i)
		p_f_str = str(p_f)
		E_c_i_str = str(E_c_i)
		E_c_f_str = str(E_c_f)
		Coef_restituicao_str = str(Coef_restituicao)
		print("\nResultados:\n\nVelocidade inicial (v/m):" + v_i_str + "\nVelocidade final (v/m):" + v_f_str + "\nMomento Linear inicial (kg.m/s):" + p_i_str + "\nMomento Linear final (kg.m/s):" + p_f_str + "\nEnergia cinética inicial (J):" + E_c_i_str + "\nEnergia cinética final (J):" + E_c_f_str + "\nCoeficiente de restituição:" + Coef_restituicao_str)
		user_decision_2 = input("\n\nDeseja fazer mais um ensaio?\n(sim/não):")
		if user_decision_2 == "sim":
			continue
		elif user_decision_2 == "não":
			break
		else:
			print("O que introduziu não é válido.")
"""
Substituição dos inputs.
"""
	elif user_decision_1 == "não":
		print("\n")
		continue
	else:
		print("O que intoduziu não é válido.")