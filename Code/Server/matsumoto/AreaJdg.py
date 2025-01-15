
def AreaJdg(UlsncSig): #cm
    if UlsncSig >= 70:
	AreaJdg = 0 #Area4
    elif UlsncSig >= 40:
	AreaJdg = 1 #Area3
    elif UlsncSig >= 20:
	AreaJdg = 2 #Area2
    else:
	AreaJdg = 3 #Area1	
return AreaJdg		
