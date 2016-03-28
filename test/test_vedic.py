from vedic import Ops, VedicNumber


def test_addition():
	result = Ops.add([58200, 1136909 + 14567 + 345687000, 45678])
	reg_result = 58200 + 1136909 + 14567 + 345687000 + 45678
	print(result)
	print(reg_result)
	result = VedicNumber(582000000000000) + VedicNumber(967854367898234)
	reg_result = 582000000000000 + 967854367898234
	print(result)
	print(reg_result)
	result = VedicNumber(58) + VedicNumber(56)
	reg_result = 58 + 56
	print(result)
	print(reg_result)
	result = VedicNumber(582) + VedicNumber(390) + VedicNumber(648)
	reg_result = 582 + 390 + 648
	print(result)
	print(reg_result)
	result = Ops.add([15, 19, 11])
	reg_result = 15 + 19 + 11
	print(result)
	print(reg_result)
	result = VedicNumber(99) + VedicNumber(99)
	reg_result = 99 + 99
	print(result)
	print(reg_result)


def test_subtract():
	result = VedicNumber(90008988) - VedicNumber(28200009)
	reg_result = 90008988 - 28200009
	print(result)
	print(reg_result)
	result = VedicNumber(100020000000000) - VedicNumber(9)
	reg_result = 100020000000000 - 9
	print(result)
	print(reg_result)
	result = VedicNumber(947600) - VedicNumber(2586)
	reg_result = 947600 - 2586
	print(result)
	print(reg_result)


def test_multiply():
	print(VedicNumber(100) * VedicNumber(2))
	print(VedicNumber(45786) * VedicNumber(57))
	print(VedicNumber(45) * VedicNumber(57))
	print(VedicNumber(4578) * VedicNumber(57))
	print(VedicNumber(321) * VedicNumber(214))
	print(VedicNumber(3212) * VedicNumber(2141))
	print(VedicNumber(4567) * VedicNumber(2918))
	print(VedicNumber(11111) * VedicNumber(11122))
	print(VedicNumber(45896) * VedicNumber(69582))
	print(VedicNumber(45896) * VedicNumber(6958))
	print(VedicNumber(4589687653456789) * VedicNumber(695875230987))
	print(VedicNumber(3193849956007425054398320743) * VedicNumber(4589687653456789))
	print(VedicNumber(14658773710080787476049501741254440712874227) * VedicNumber(3193849956007425054398320743))
	print(VedicNumber(68629335010652649695338856996888505082799258781159071602280830658069423538482865002531059244901433270522974099404725678) * VedicNumber(4681792376906432202903607601716785597020499902587316420748476976419066198975454254254254278899))
	print(VedicNumber(64668554892204736725073043955364852531553594478280496089759523229447819611855261655127070472292684529256839692403980271491207400740421058447377477994593100296357809917746129838031509651456000000000000000000000000000000002432902008176640000) * VedicNumber(131))


def test_fact():
	fact = Ops.fact(50)
	print(fact)
	# print(len(str(fact)))
	# print(len(str(fact)))
	# print(list(200))
	result = 2
	for i in range(3, 1000 + 1):
		result *= i
	print(len(str(result)))

if __name__ == '__main__':
	test_addition()
	test_subtract()
	test_multiply()
	test_fact()