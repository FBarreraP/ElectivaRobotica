n = "Fabián"
s = "Barrera Prieto"
o = 'PROFESOR'
a = '2024'

print("Primer apellido: %s" %s[:7])
print("Segundo apellido: %s" %s[8:])

c = n.upper()+' '+s+" es "+o.lower()+' en el semestre '+a+"\"2\""
print(c)
print(c[:int(len(c)/2)])