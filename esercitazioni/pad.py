
# disegnamo un tastierino telefonico in console

# matrice di tuple 
num_pad = (
    (1,2,3),
    (4,5,6),
    (7,8,9),
    ("*",0,"#")
)

# iteriamo e stampiamo risultato a video
for row in num_pad:
    for col in row:
        print(col, end=" ")
    print()