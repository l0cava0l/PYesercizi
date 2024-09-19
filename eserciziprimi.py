import math  #libreria x facilitare fattoriale senza usare def fattoriale(n):if n == 0 or n == 1: return 1 else:return n * fattoriale(n - 1)

# 1) Raddoppio dei valori nella lista1
lista1 = [1, 2, 3, 4, 5]  
lista2 = [x * 2 for x in lista1]  #raddoppia lista con for
print("Lista originale:", lista1)  
print("Lista con valori raddoppiati:", lista2)

# 2) Calcolo del fattoriale di un numero inserito dall'utente
numero = int(input("Inserisci un numero per calcolare il fattoriale: "))
fattoriale = math.factorial(numero)  # Calcolo il fattoriale con la funzione factorial del modulo math
print(f"Il fattoriale di {numero} è: {fattoriale}") 

# 3) Scambio chiavi e valori in un dizionario
dizionario = {"a": 1, "b": 2, "c": 3}  # Definisco un dizionario con alcune coppie chiave-valore
dizionario_invertito = {v: k for k, v in dizionario.items()}  # scambio chiavi-valori creando un nuovo dizionario
print("Dizionario originale:", dizionario) 
print("Dizionario con chiavi e valori scambiati:", dizionario_invertito) 
