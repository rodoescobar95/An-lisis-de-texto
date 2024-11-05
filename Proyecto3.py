texto = input("Introduce un texto: ")
letras = input("Introduce 3 letras diferentes: ")
textomin = texto.lower()
letrasmin = letras.lower()
letrasmin = list(letrasmin)
print("\n")
print(f"""La letra {letrasmin[0]} aparece {textomin.count(letrasmin[0])} veces
la letra {letrasmin[1]} aparece {textomin.count(letrasmin[1])} veces y
la letra {letrasmin[2]} aparece {textomin.count(letrasmin[2])} veces en el texto""")
textomin = textomin.split(" ")
textomin = list(textomin)
print("\n")
print(f"hay {len(textomin)} palabras en el texto")
print(f"la primera letra del texto es la {textomin[0][0]} y la ultima letra del texto es la {textomin[-1][-1]}")
textomin.reverse()
print("\nEl texto al reves se lee: ")
print(" ".join(textomin))
elpiton = "python" in textomin
dic = {False:"No",True:"Si"}
print("\n")
print(f"Se encuentra 'python' en el texto? {dic[elpiton]}")
