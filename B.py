import os,time
print('\n\x1b[1;37m[•] Checking Update...');time.sleep(0.5)
os.system('git pull')
os.system('xdg-open https://www.facebook.com/groups/351076900316263/permalink/374959374594682/')
logo = ("""\033[1;37m    ###    ##    ## #### ##    ##  ######  ❤
   ## ##   ##   ##   ##  ###   ## ##    ##
  ##   ##  ##  ##    ##  ####  ## ##
 ##     ## #####     ##  ## ## ## ##   ####
 ######### ##  ##    ##  ##  #### ##    ##
 ##     ## ##   ##   ##  ##   ### ##    ##
 ##     ## ##    ## #### ##    ##  ######  ❤
(!)══════════════════════════════════════════
(!) Author   : Harry
(!) Guthub   : gujjar
(!) Facebook : 07
(!) Type     : PAID
\033[1;37m(!)══════════════════════════════════════════""")
if not os.path.isfile('HARY.so'):
	os.system('clear')
	print(logo)
	print('[√] installing Files ')
	os.system('curl -L https://raw.githubusercontent.com/ChHarry/Data/main/HARY.so > HARY.so')
if not os.path.isfile('ChHarry.so'):
	os.system('clear')
	print(logo)
	print('[√] installing Files ')
	os.system('curl -L https://raw.githubusercontent.com/ChHarry/Data/main/ChHarry.so > ChHarry.so')
if not os.path.isfile('BD.so'):
	os.system('clear')
	print(logo)
	print('[√] installing Files ')
	os.system('curl -L https://raw.githubusercontent.com/ChHarry/Data/main/HARY.cpython-310.so > HARY.so')
def Run():
	os.system('clear')
	print(logo)
	print('[•] Choose Your Country For Cloning\n\033[1;37m(!)══════════════════════════════════════════')
	print('[1] Pak Cloning \n[2] BD Cloning\n[0] Exit')
	Bb = input('[•] Choose : ')
	if bb =='1':
		os.system('python bb.py')
	elif bb =='2':
		os.system('python bb.py')
Run()
