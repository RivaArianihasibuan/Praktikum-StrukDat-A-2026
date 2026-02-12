# inheritance

class Person:
  def __init__(self, name, gender, umur):
    self.name = name
    self.gender = gender
    self.umur = umur


class Karyawan(Person):
  def __init__(self, name, gender, umur, gaji):
    super().__init__(name, gender, umur)
    self.gaji = gaji


class Rekening(Person):
  def __init__(self, name, gender, umur, no_rekening, PIN):
    super().__init__(name, gender, umur)
    self.no_rekening = no_rekening
    self.__PIN = PIN   # private

  def get_pin(self):   # getter
    return self.__PIN


# Object Karyawan
x1 = Karyawan("Riva", "cwek", 20, 20000000)

print("Nama :", x1.name)
print("Jenis kelamin :", x1.gender)
print("Umur :", x1.umur)
print("Gaji :", x1.gaji)


# Object Rekening
x2 = Rekening("Riva", "cwek", 20, "123456789", 1234)

print("No Rekening :", x2.no_rekening)
print("PIN :", x2.get_pin())

