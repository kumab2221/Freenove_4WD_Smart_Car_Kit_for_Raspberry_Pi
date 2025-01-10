import time

class AreaJdg:

	def AreaJdg(self,UlsncSig): #cm
		if UlsncSig >= 70:
			AreaJdg = 0 #Area4
		elif UlsncSig >= 40:
			AreaJdg = 1 #Area3
		elif UlsncSig >= 20:
			AreaJdg = 2 #Area2
		else:
			AreaJdg = 3 #Area1	
		return AreaJdg		

if __name__=='__main__':
    A=AreaJdg()
    A0=A.AreaJdg(80)
    time.sleep(3)
    print (A0)
    A1=A.AreaJdg(50)
    time.sleep(3)
    print (A1)
    A2=A.AreaJdg(20)
    time.sleep(3)
    print (A2)
    A3=A.AreaJdg(19.5)  
    time.sleep(3)
    print (A3)
