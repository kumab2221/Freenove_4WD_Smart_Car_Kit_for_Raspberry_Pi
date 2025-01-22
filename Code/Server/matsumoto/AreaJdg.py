
def AreaJdg(UlsncSig): #cm
    dist_obj = UlsncSig
    # フィルタ機能
    

    if dist_obj >= 70:
        area_jdg = 0 #Area4
    elif dist_obj >= 40:
        area_jdg = 1 #Area3
    elif dist_obj >= 20:
        area_jdg = 2 #Area2
    else:
        area_jdg = 3 #Area1	
    return area_jdg, dist_obj		
