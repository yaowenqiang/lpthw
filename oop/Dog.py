class Dog:
    species = 'animinal'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    pass

philo = Dog("philo",5)
mikey = Dog('mikey',6)

print('{} is {} and {} is '.format(philo.name,philo.age,mikey.name,mikey.age))

if philo.species =='animinal':
    print("{0} is {1}!".format(philo.name,philo.species))
