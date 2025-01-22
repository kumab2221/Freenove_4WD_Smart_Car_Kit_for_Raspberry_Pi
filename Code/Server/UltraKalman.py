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

# デモ用コード例
if __name__ == "__main__":
    dt = 0.1  # サンプリング周期 100ms (10Hz)
    kf = KalmanFilter1D(
        dt=dt,
        process_var_x=0.1,   # 位置方向ノイズ
        process_var_v=0.1,   # 速度方向ノイズ
        measurement_var=4.0  # センサノイズ（仮定: 分散が4cm^2）
    )

    import random
    true_x = 0.0
    true_v = 100.0  # 真の速度 100 cm/s
    time_steps = int(10 / dt)
    
    for k in range(time_steps):
        true_x += true_v * dt  # 真の位置更新
        
        # ノイズ付きセンサ測定値 (距離)
        if random.random() < 0.05:
            z = true_x + random.gauss(0, 20.0)  # 外れ値
        else:
            z = true_x + random.gauss(0, 2.0)   # 通常ノイズ
        
        kf.predict()
        kf.update(z)
        est_x, est_v = kf.get_state()
        print(f"t={k*dt:.1f}s 真値={true_x:.2f}cm センサ={z:.2f}cm 推定位置={est_x:.2f}cm 推定速度={est_v:.2f}cm/s")
