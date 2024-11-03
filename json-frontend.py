# --- JSON ---
# importante per inviare e ricevere dati da frontend 


# --- leggere JSON in python ---
# importo il modulo
# creo un dato JSON di prova
import json
data = '{"nome": "Lorenzo", "cognome":"Raspa", "eta":"37"}'
y = json.loads(data) # loads trasforma JSON in dictionary
print(type(y)) # 
print(y)


# --- da python a JSON ---
# creo un dictionary per prova
data2 = {
        "nome": "Lorenzo", 
        "cognome":"Raspa", 
        "eta":"37",
        "isOnline": True,
        "interessi": ["calcio", "basket"],
        "monetine_in_tasca": 4.56,
        "fidanzata": None
        }
y2 = json.dumps(data2, indent=4) 
# dumps trasforma dictionary in JSON, 
# indent=4 visualizza bene le info del JSON a schermo
print(type(y2))
print(y2)


# sia loads che dumps trasforma in JSON e dictionary anche dati come tuple, liste ecc.
