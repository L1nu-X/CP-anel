import requests
import re
requests.packages.urllib3.disable_warnings()
from multiprocessing.dummy import Pool


def banner():
		print("""

  ________    __________  ____  __   ____
 / ___/ _ \  /_  __/ __ \/ __ \/ /  / __/
/ /__/ ___/   / / / /_/ / /_/ / /___\ \  
\___/_/      /_/  \____/\____/____/___/  
                                         
    Author : SinonX
    Family Attack Cyber ~ Tatsumi Crew
    Thanks to : KyuRazz                              
		"""+'\n')



def cp(hh):


	if '://' not in hh:
		target = "http://"+hh
	else:
		target = hh

	target = target[:target.rfind('/')]
	try:
		r = requests.get('{}:2083'.format(target), verify=False)
		if r.status_code == 200:
			print(target, '-> CPANEL FOUND!'+'\n')
			if '<a href="/resetpass?start=1"' in r.text:
				print('(+) VULN RESET CPANEL!'+'\n')
				open('cpreset.txt', 'a').write(target+'\n')
			else:
				pass
		else:
			print(target, '-> NOT FOUND!'+'\n')
	except Exception:
		print(target, '-> NOT FOUND!'+'\n')



if __name__ == "__main__":

	banner()

	halo = input('Your Domain List -> ')
	asu = open(halo, 'r', encoding="utf8").read().splitlines()
	p = Pool(50)
	p.map(cp, asu)