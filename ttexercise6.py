#Exercise 6
import yaml
import json

def main():

	yaml_file = 'test_file.yml'
	json_file = 'jsontest.json'

	dict = {
		'ip_add': '192.168.1.100',
		'vendor': 'cisco'
	}
	
	list = [
		'week one',
		99,
		18
	]
	
	with open(yaml_file, "w") as f:
        	f.write(yaml.dump(list, default_flow_style=False))

	with open(json_file, "w") as f:
        	json.dump(list, f)

if __name__ == "__main__":
    main()