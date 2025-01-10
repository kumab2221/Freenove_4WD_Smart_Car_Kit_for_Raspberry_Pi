import time
import Buzzer

class BuzzerCtrl:
    
    flag = False
    
    def BuzzerCtrl(self,AreaJdg,DrvCtrlSt):
        Param_Area3_BuzzerOff = 0.2
        Param_Area3_BuzzerOn = 0.8
        Param_Area2_BuzzerOff = 0.4
        Param_Area2_BuzzerOn = 0.2

        B=Buzzer.Buzzer()
        
        if AreaJdg == 1:
            B.run('1')
            time.sleep(Param_Area3_BuzzerOn)
            B.run('0')
            time.sleep(Param_Area3_BuzzerOff)
        elif AreaJdg == 2:
            B.run('1')
            time.sleep(Param_Area2_BuzzerOn)
            B.run('0')
            time.sleep(Param_Area2_BuzzerOff)
        elif AreaJdg == 3 and DrvCtrlSt == 0 and BuzzerCtrl.flag == False :
            BuzzerCtrl.Flag = True
            B.run('1')
            time.sleep(5)
            B.run('0')
            time.sleep(5)
        elif AreaJdg == 3:
            B.run('1')
        else :
            B.run('0')

            
if __name__=='__main__':
    BC=BuzzerCtrl()
    BC.BuzzerCtrl(0,3)
    print ('area4')
    BC.BuzzerCtrl(0,3)
    BC.BuzzerCtrl(0,3)
    BC.BuzzerCtrl(0,3)
    print ('area3')
    BC.BuzzerCtrl(1,2)
    BC.BuzzerCtrl(1,2)
    BC.BuzzerCtrl(1,2)
    BC.BuzzerCtrl(1,2)
    print ('area2')
    BC.BuzzerCtrl(2,3)
    BC.BuzzerCtrl(2,3)
    BC.BuzzerCtrl(2,3)
    BC.BuzzerCtrl(2,3)
    print ('area1')
    BC.BuzzerCtrl(3,3)
    BC.BuzzerCtrl(3,3)
    BC.BuzzerCtrl(3,3)
    BC.BuzzerCtrl(3,3)
    print ('0kph')
    BC.BuzzerCtrl(3,0)
    BC.BuzzerCtrl(3,0)
    BC.BuzzerCtrl(3,0)
    BC.BuzzerCtrl(3,0)
    BC.BuzzerCtrl(3,0)
    BC.BuzzerCtrl(3,0)
    BC.BuzzerCtrl(3,0)
    BC.BuzzerCtrl(3,0)
    print ('end')
