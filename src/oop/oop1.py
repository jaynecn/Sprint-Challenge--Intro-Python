# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]

class Vehicle:
  def __init__(self, name):
    self.name = name
    self.flight_vehicle = FlightVehicle
    self.starship = Starship
  pass

class GroundVehicle(Vehicle):
  def __init__(self, name):
    super().__init__()
    self.name = name
  pass

class Car(GroundVehicle):
  def __init__(self, name):
    self.name = name
  pass

class Motorcycle(GroundVehicle):
  def __init__(self, name):
    self.name = name
  pass

class FlightVehicle:
  def __init__(self, name):
    self.name = name
  pass

class Airplane(FlightVehicle):
  def __init__(self, name):
    self.name = name
  pass

class Starship:
  def __init__(self, name):
    self.name = name
  pass

#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
