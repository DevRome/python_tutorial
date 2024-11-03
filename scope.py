
y = 200 # variabile scope globale

def funzione():
    x = 400 # variabile scope locale, vive solo nella funzione
    global z # globale
    z = 300 
    print(x)
    return x
# end funzione()

x = funzione()
print(x)