import yaml
stream = open("cofig.yml", 'r’)
dictionary = yaml.load(stream)
print("it works")
