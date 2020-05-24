class Encapsulamiento:
  __privado_atri = "Soy un atributo al que no vas a poder acceder desde fuera de la clase"

  def __privado_met(self):
    print("Soy un método al que no vas a poder acceder desde fuera de la clase")

  def publico_atri(self):
    return self.__privado_atri

  def publico_met(self):
    self.__privado_met()

e = Encapsulamiento()
print(e)

#   File "/home/eduardo-fernandez/source/python-udemy-activities/section-10/encapsulation.py", line 10, in <module>
#     e.____privado_atri
# AttributeError: 'Encapsulamiento' object has no attribute '____privado_atri'
# e.____privado_atri

#   File "/home/eduardo-fernandez/source/python-udemy-activities/section-10/encapsulation.py", line 15, in <module>
#     e.__privado_met
# AttributeError: 'Encapsulamiento' object has no attribute '__privado_met'
# e.__privado_met

print(e.publico_atri())
e.publico_met()