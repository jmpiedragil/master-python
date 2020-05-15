"""
Ejemplo 5

  Crear una lista con el contenido de esta tabla:

  ACCION        AVENTURA           DEPORTES
  GTA           ASSASINS           FIFA 21
  COD           CRASH              PRO 21
  PUGB          PRINCE OF PERSIA   MOTO GP 21

  Mostrar esta información ordenada

"""

juegos = [
  [
    {
      "nombre": "GTA",
    },
    {
      "nombre": "COD",
    },
    {
      "nombre": "PUGB",
    }
  ],
  [
    {
      "nombre": "ASSASINS",
    },
    {
      "nombre": "CRASH",
    },
    {
      "nombre": "PRINCE OF PERSIA",
    }
  ],
  [
    {
      "nombre": "FIFA 21",
    },
    {
      "nombre": "PRO 21",
    },
    {
      "nombre": "MOTO GP 21",
    }
  ]
]

for juego in juegos:

  if juegos.index(juego) == 0:
    print("########## Juegos de acción ##########")
  elif juegos.index(juego) == 1:
    print("\n########## Juegos de aventura ##########")
  elif juegos.index(juego) == 2:
    print("\n########## Juegos de deportes ##########")

  for elemento in juego:
    print(f"Nombre: {elemento['nombre']}")
