import numpy as np

class KalmanFilter1D:
    def __init__(self, dt, 
                 process_var_x=1.0, 
                 process_var_v=1.0, 
                 measurement_var=1.0):
        """
        dt               : サンプリング周期 (秒)
        process_var_x    : 状態(位置)に対するプロセスノイズの分散
        process_var_v    : 状態(速度)に対するプロセスノイズの分散
        measurement_var  : センサ(位置測定)ノイズの分散
        """
        self.dt = dt
        
        # 状態ベクトル x = [位置, 速度]^T
        self.x = np.zeros((2, 1))  # 初期値 [x, v]^T

        # 状態推定誤差共分散行列 P
        self.P = np.eye(2) * 1000.0  # 初期化（大きめ）

        # 状態遷移行列 A
        self.A = np.array([[1, self.dt],
                           [0, 1       ]], dtype=float)

        # 観測行列 H
        self.H = np.array([[1, 0]], dtype=float)  # 距離のみ観測

        # プロセスノイズ共分散 Q
        self.Q = np.array([[process_var_x, 0],
                           [0, process_var_v]], dtype=float)

        # 観測ノイズ共分散 R
        self.R = np.array([[measurement_var]], dtype=float)

        # 単位行列 I
        self.I = np.eye(2)

    def predict(self):
        """
        予測ステップ
        """
        self.x = self.A @ self.x
        self.P = self.A @ self.P @ self.A.T + self.Q

    def update(self, z):
        """
        更新ステップ
        z : 観測値（距離, cm単位）
        """
        S = self.H @ self.P @ self.H.T + self.R  # 1x1
        K = self.P @ self.H.T @ np.linalg.inv(S) # 2x1
        y = z - (self.H @ self.x)  # センサ残差
        self.x = self.x + K * y
        self.P = (self.I - K @ self.H) @ self.P

    def get_state(self):
        """
        現在の推定状態を返す
        returns: (位置推定値, 速度推定値)
        """
        return float(self.x[0, 0]), float(self.x[1, 0])

dt = 0.1  # サンプリング周期 100ms (10Hz)
kf = KalmanFilter1D(
    dt=dt,
    process_var_x=0.1,   # 位置方向ノイズ
    process_var_v=0.1,   # 速度方向ノイズ
    measurement_var=4.0  # センサノイズ（仮定: 分散が4cm^2）
)

def AreaJdg(UlsncSig): #cm
    global kf
    # フィルタ機能
    kf.predict()
    kf.update(UlsncSig)
    est_x, est_v = kf.get_state()
    if est_x >= 140:
        area_jdg = 0 #Area4
    elif est_x >= 70:
        area_jdg = 1 #Area3
    elif est_x >= 40:
        area_jdg = 2 #Area2
    else:
        area_jdg = 3 #Area1	
    return area_jdg, est_x		
