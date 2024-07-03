#Project overview:
#You are a physics teacher preparing for the upcoming semester.
#You want to provide your students with some functions that will help them calculate some fundamental physical properties.
#
# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

#Write a funtion that takes temp in F and converts it to C
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
#Test function with value of 100 F
f100_in_celsius = f_to_c(100)
# print(f100_in_celsius)

#Write a funtion that takes temp in C and converts it to F
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp
#Test function with value of 0 C
c0_in_fahrenheit = c_to_f(0)
# print(c0_in_fahrenheit)

#Write a function that takes in mass & acceleration and returns product of mass & acceleration
def get_force (mass, acceleration):
  return mass * acceleration
#Test get_force by calling train_mass & train_acceleration
train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

#Write function that takes in mass and c (speed of light)
def get_energy(mass, c = 3*10**8):
  return mass * (c**3)
bomb_energy = get_energy(bomb_mass)
print(bomb_energy)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

#Write function that takes in mass, acceleration, and distance
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
