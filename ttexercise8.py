#Exercise 8

from ciscoconfparse import CiscoConfParse

def main():
		    cisco_test_file = 'cisco_ipsec.txt'

    		parse_file = CiscoConfParse(cisco_test_file)
    		crypto_maps = parse_file.find_objects(r"^crypto map CRYPTO")

    		for c_map in crypto_maps:
        		print
        		print c_map.text
        		for child in c_map.children:
            		print child.text
    		print

if __name__ == "__main__":
    		main()