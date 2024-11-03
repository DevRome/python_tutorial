# --- PIP ---
# pip è il package manager di python (come npm di NodeJS)
# quando abbiamo bisogno di un pacchetto che non è presente built-in in python, allora lo scarivhiamo ed instaliliamo con pip

# installazione pip: python get-pip.py
# controllare versione di pip: pip --version
# installare package: py -m pip install nome_package

# modulo che ho importato tramite pip
import camelcase

c = camelcase.CamelCase()

frase = "ciao, sono lorenzo" 

print(c.hump(frase)) # Ciao, Sono Lorenzo


# rimuovere il pacchetto: pip uninstall nome_pacchetto
# per vedere i pacchetti installati: pip list
 

