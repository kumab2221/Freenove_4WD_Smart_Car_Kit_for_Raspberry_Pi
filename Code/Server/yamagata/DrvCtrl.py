
def DrvCtrl(AreaJdg, DistObj):
	#AreaJdg
	#0:Area4, start
	#1:Area3
	#2:Area2
	#3:Area0, end

	DrvCtrlSt = 0

	DrvRqJdg = fDrvRqJdg(AreaJdg)
	DrvCtrlSt = DrvRqJdg
	

	#DrvRqJdg, DrvCtrlSt
	#0:oFF
	#1:Normal Drive
	#2:Lo Drive
	#3: Deceleration Drive
	#4: Rmergency Stop
	
	FrDrvRq, FlDrvRq, RrDrvRq, RlDrvRq = DrvRq(DrvRqJdg, DistObj)
	#[-100, 100][%]

	FrDrvOut = FrDrvCtl(FrDrvRq)
	FlDrvOut = FlDrvCtl(FlDrvRq)
	RrDrvOut = RrDrvCtl(RrDrvRq)
	RlDrvOut = RlDrvCtl(RlDrvRq)
	#[-4096, 4096][-]


	return DrvCtrlSt, FrDrvOut, FlDrvOut, RrDrvOut, RlDrvOut



def fDrvRqJdg(AreaJdg):
	#AreaJdg
	#0:Area4, start
	#1:Area3
	#2:Area2
	#3:Area1, end
	DrvRqJdg = 0

	if AreaJdg == 0:
		DrvRqJdg = 1
	elif AreaJdg == 1:
		DrvRqJdg = 1
	elif AreaJdg == 2:
		DrvRqJdg = 2
	elif AreaJdg == 3:
		DrvRqJdg = 3
	else:	
		DrvRqJdg = 0

	#DrvRqJdg, DrvCtrlSt
	#0:oFF
	#1:Normal Drive
	#2:Lo Drive
	#3: Deceleration Drive
	#4: Emergency Stop
	return DrvRqJdg


def linear_function(x):
    # 2点を基に傾きと切片を計算
    x1, y1 = 5, 0
    x2, y2 = 20, 70
    m = (y2 - y1) / (x2 - x1)  # 傾き
    b = y1 - m * x1            # 切片
    # 線形関数
    return m * x + b

def DrvRq(DrvRqJdg, DistObj):
	#DrvRqJdg, DrvCtrlSt
	#0:oFF
	#1:Normal Drive
	#2:Lo Drive
	#3: Deceleration Drive
	#4: Rmergency Stop

	FrDrvRq = 0.0
	FlDrvRq = 0.0
	RrDrvRq = 0.0
	RlDrvRq = 0.0

	if DrvRqJdg == 0:#0:oFF
		FrDrvRq = 0.0
		FlDrvRq = 0.0
		RrDrvRq = 0.0
		RlDrvRq = 0.0

	elif DrvRqJdg == 1:	#1:Normal Drive	
		FrDrvRq = 100.0
		FlDrvRq = 100.0
		RrDrvRq = 100.0
		RlDrvRq = 100.0

	elif DrvRqJdg == 2:	#2:Lo Drive	
		FrDrvRq = 70.0
		FlDrvRq = 70.0
		RrDrvRq = 70.0
		RlDrvRq = 70.0
	
	elif DrvRqJdg == 3:	#3: Deceleration Drive
		trq = linear_function(DistObj)
		FrDrvRq = trq
		FlDrvRq = trq
		RrDrvRq = trq
		RlDrvRq = trq

	elif DrvRqJdg == 4: #4: Rmergency Stop
		FrDrvRq = 0.0
		FlDrvRq = 0.0
		RrDrvRq = 0.0
		RlDrvRq = 0.0



	return 	FrDrvRq, FlDrvRq, RrDrvRq, RlDrvRq


def FrDrvCtl(FrDrvRq):
	duty = 1000.0 #yukkuri

	FrDrvOut = duty * (FrDrvRq /100)

	return FrDrvOut

def FlDrvCtl(FlDrvRq):
	duty = 1000 #yukkuri
	
	FlDrvOut = duty * (FlDrvRq /100)

	return FlDrvOut

def RrDrvCtl(RrDrvRq):
	duty = 1000 #yukkuri
	
	RrDrvOut = duty * (RrDrvRq /100)
	return RrDrvOut

def RlDrvCtl(RlDrvRq):
	duty = 1000 #yukkuri
	
	RlDrvOut = duty * (RlDrvRq /100)

	return RlDrvOut

if __name__ == '__main__':
	#AreaJdg
	#0:Area4, start
	#1:Area3
	#2:Area2
	#3:Area0, end
	AreaJdg = 3
	DrvCtrlSt, FrDrvOut, FlDrvOut, RrDrvOut, RlDrvOut = DrvCtrl(AreaJdg,)

	print(DrvCtrlSt)
	print(FrDrvOut)
	print(FlDrvOut)
	print(RrDrvOut)
	print(RlDrvOut)
