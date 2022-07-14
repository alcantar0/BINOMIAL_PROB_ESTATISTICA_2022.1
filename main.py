from math import e, factorial, sqrt

def comb(n, r):
	return float(factorial(n)/(factorial(r)*factorial(n-r)))

p = float(input("Digite a probabilidade de sucesso (p): "))

n = int(input("Digite o número da amostra (n): ")) 

total = []
for i in range(0, n+1):
	total.append(comb(n, i)*pow(p, i)*pow(1-p, n-i))


for i in range(0, n+1):
	print("*"*30)
	print(f"A probabilidade de ocorrer X={i}: {total[i]}\nA probabilidade de X<={i}: {sum(total[:i+1])}\nA probabilidade complementar (X>{i}): {1.0000-sum(total[:i+1])}. ")
print("*"*30)
