#Exercise10

from ciscoconfparse import CiscoConfParse

def main():
    		cisco_test_file = 'cisco_ipsec.txt'

    		parse_file = CiscoConfParse(cisco_test_file)
    		crypto_maps = parse_file.find_objects_wo_child(parentspec=r'crypto ipsec transform-set',
                                                 		childspec=r'AES')
    		print "\nCrypto Maps noy using AES:"
    		for entry in crypto_maps:
        		print "  {0}".format(entry.text)
    		print

if __name__ == "__main__":
    		main()
    		