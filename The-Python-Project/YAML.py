
import yaml

stream = open("config.yaml", 'r')
dictionary = yaml.load(stream, Loader=yaml.FullLoader)
print("it works")