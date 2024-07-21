from spider import Spider
from cat import Cat
from fish import Fish


print("Spider:")
spider = Spider()
spider.walk()
spider.eat()
print()

print("Cat:")
cat = Cat("Garfield")
print(f"Cat's name is {cat.get_name()}")
cat.set_name("Garfield")
print(f"Cat's new name is {cat.get_name()}")
cat.walk()
cat.eat()
cat.play()
print()

print("Fish:")
fish = Fish()
print(f"Fish's name is {fish.get_name()}")
fish.set_name("Nemo")
print(f"Fish's new name is {fish.get_name()}")
fish.walk()
fish.eat()
fish.play()
print()
