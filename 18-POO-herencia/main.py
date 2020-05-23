import clases

persona = clases.Persona()

persona.setNombre("Javier")
persona.setApellidos("Piedragil Gálvez")
persona.setAltura("175 cm")
persona.setEdad("55 años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())
