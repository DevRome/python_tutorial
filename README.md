*** Differenze tra le collezioni dati ***
# liste, tuple, set e dictionary

le collezioni di dati possonoo essere:

# ordinate:
una collezione ordinata ha un ordine ben definito e l'aggiunta di elementinon incide sull'ordine stesso:
esempio:
citta = ["milano", "roma", "napoli"]

# indicizzato
possiamo accedere agli elemnti di una lista tramite un indice

# modificabile
possiamo aggiungere, cambiare e rimuovere elementi una volta creata la collezione 

# immutabile
non possiamo aggiungere, cambiare e rimuovere elementi

# permette duplicati
possono esserci più elementi con lo stesso valore

Le collezioni che abbiamo a disposizione in Python sono:
liste, tuple, set, dictionary

# liste
sono collezioni ordinate e modificabili. permettono duplicati

# tuple
sono collezioni ordinate ma immutabili

# set
sono collezioni non ordinate e perciò non indicizzate. Non permettono duplicati; quindi gli elementi non si possono modificare.

# dictionary
sono collezioni rodinate e modificabili (dalla versione 3.7). Non permettono duplicati


*** La cartella __pycache__ ***
When you run a program in Python, the interpreter compiles it to bytecode first (this is an oversimplification) and stores it in the __pycache__ folder. If you look in there you will find a bunch of files sharing the names of the .py files in your project's folder, only their extensions will be either .pyc or .pyo. These are bytecode-compiled and optimized bytecode-compiled versions of your program's files, respectively.

As a programmer, you can largely just ignore it... All it does is make your program start a little faster. When your scripts change, they will be recompiled, and if you delete the files or the whole folder and run your program again, they will reappear (unless you specifically suppress that behavior).

When you're sending your code to other people, the common practice is to delete that folder, but it doesn't really matter whether you do or don't. When you're using version control (git), this folder is typically listed in the ignore file (.gitignore) and thus not included.

If you are using CPython (which is the most common, as it's the reference implementation) and you don't want that folder, then you can suppress it by starting the interpreter with the -B flag, for example

python -B foo.py
Another option, as noted by tcaswell, is to set the environment variable PYTHONDONTWRITEBYTECODE to any value (according to Python's man page, any "non-empty string").