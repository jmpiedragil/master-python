import clases

persona = clases.Persona()

persona.setNombre("Javier")
persona.setApellidos("Piedragil Gálvez")
persona.setAltura("175 cm")
persona.setEdad("55 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())

print("------------------------------------------------------------")

informatico = clases.Informatico()

informatico.setNombre("Carlos")
informatico.setApellidos("Martínez")

print(f"El informático es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)

print("------------------------------------------------------------")

tecnico = clases.TecnicoRedes()
print(tecnico.auditarRedes, tecnico.getNombre())
