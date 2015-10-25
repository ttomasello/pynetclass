#Exercise 7
import yaml
import json

from pprint import pprint


def output_format(list, str):

	print '\n\n'
	print '#' * 3
	print '#' * 3 + str
	print '#' * 3
	pprint(list)

def main():

	yaml_file = 'test_file.yml'
	json_file = 'jsontest.json'


	with open(yaml_file) as f:
        	yaml_list = yaml.load(f)

	with open(json_file) as f:
        	json.list = json.load(f)

if __name__ == "__main__":
    main()