window_size = 3
data_buffer = []

def UlsncSigFilt(UlsncSig):
    global window_size,data_buffer
    data_buffer.append(UlsncSig)
    if len(data_buffer) > window_size:
        data_buffer.pop(0)
    DistObj = sum(data_buffer) / len(data_buffer)

    return DistObj


def AreaJdg(UlsncSig): #cm
    # フィルタ機能
    dist_obj = UlsncSigFilt(UlsncSig)
    if dist_obj >= 70:
        area_jdg = 0 #Area4
    elif dist_obj >= 40:
        area_jdg = 1 #Area3
    elif dist_obj >= 20:
        area_jdg = 2 #Area2
    else:
        area_jdg = 3 #Area1	
    return area_jdg, dist_obj		
