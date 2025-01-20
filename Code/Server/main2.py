# main2.py
import time
from Motor import Motor
from Buzzer import Buzzer
from Ultrasonic import Ultrasonic

from yamagata.DrvCtrl import DrvCtrl
from matsumoto.AreaJdg import AreaJdg
from matsumoto.BuzrCtrl import BuzrCtrl

def main2():
    print("Start")
    motor= Motor()
    buzzer = Buzzer()
    ultra = Ultrasonic()
    try:
        motor.setMotorModel(0,0,0,0)
        buzzer.run("0")
        print("time, ulsnc_sig, area_state, buzzer_out, drv_ctrl_st, fr_drv_out, fl_drv_out, rr_drv_out, rl_drv_out")
        while True:
            start_time = time.time()

            ### (認知)センサ-Start
            ulsnc_sig = ultra.get_distance()
            ### (認知)センサ-End

            ### (判断)制御アプリ-Start
            # エリア判定
            area_state = AreaJdg(ulsnc_sig)
            # 駆動マネージャー
            drv_ctrl_st, fr_drv_out, fl_drv_out, rr_drv_out, rl_drv_out = DrvCtrl(area_state)
            # ブザー判断
            buzzer_out = BuzrCtrl( area_state, drv_ctrl_st)
            ### (判断)制御アプリ-End

            ### (制御)デバイス制御-Start
            # モーター
            motor.setMotorModel(int(fl_drv_out), int(rl_drv_out), int(fr_drv_out), int(rr_drv_out))
            # ブザー
            buzzer.run(str(buzzer_out))
            ### (制御)デバイス制御-End

            # 処理周期を10msに保つ
            elapsed_time = time.time() - start_time
            sleep_time = max(0, 0.1 - elapsed_time) 
            time.sleep(sleep_time)

            # 経過時間測定ログをデバックできるように表示する            
            formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
            milliseconds = int((start_time % 1) * 1000)
            # "time, area_state, drv_ctrl_st, fr_drv_out, fl_drv_out, rr_drv_out, rl_drv_out "
            print(f"{formatted_time}.{milliseconds:03d}, {ulsnc_sig}, {area_state}, {buzzer_out}, {drv_ctrl_st}, {fr_drv_out}, {fl_drv_out}, {rr_drv_out}, {rl_drv_out}")

    except KeyboardInterrupt:
        motor.setMotorModel(0,0,0,0) # モーターを停止する
        buzzer.run("0")
        print("Break Loop")

if __name__ == "__main__":
    main2()
