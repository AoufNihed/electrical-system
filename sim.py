import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#source:
V_rms = 17606.95885
f = 50  
X_R = 7

#tran line:
R1 = 0.690 
R0 = 1.0873  
I1 = 0.0016
I0 = 0.0047
C1 = 1.2175e-8 
C0 = 5.5916e-6

length_km = 5  

V_a, V_b, V_c = 4.9e3, 24.9e3, 24.9e3  
P_a, P_b, P_c = 0.1e6, 0.15e6, 0.1e6
Q_la, Q_lb, Q_lc = 10e3, 10e3, 10e3  

#load :
sim_time = 0.1  
time_step = 1e-4 
time = np.arange(0, sim_time, time_step)


omega = 2 * np.pi * f
V_a_wave = V_rms * np.sqrt(2) * np.sin(omega * time)
V_b_wave = V_rms * np.sqrt(2) * np.sin(omega * time - 2 * np.pi / 3)
V_c_wave = V_rms * np.sqrt(2) * np.sin(omega * time + 2 * np.pi / 3)


S_sc = 100e6  
I_sc = S_sc / (np.sqrt(3) * V_rms)  

# line modeling:
Z1 = R1 + 1j * omega * I1
Z0 = R0 + 1j * omega * I0


S_a = P_a + 1j * Q_la
S_b = P_b + 1j * Q_lb
S_c = P_c + 1j * Q_lc

I_a = np.conj(S_a / V_a)
I_b = np.conj(S_b / V_b)
I_c = np.conj(S_c / V_c)


data = {
    "Time (s)": time,
    "V_a (V)": V_a_wave,
    "V_b (V)": V_b_wave,
    "V_c (V)": V_c_wave,
    "I_a (A)": [I_a.real] * len(time),
    "I_b (A)": [I_b.real] * len(time),
    "I_c (A)": [I_c.real] * len(time),
}
df = pd.DataFrame(data)


plt.figure(figsize=(10, 6))
plt.plot(time, V_a_wave, label="Phase A Voltage")
plt.plot(time, V_b_wave, label="Phase B Voltage")
plt.plot(time, V_c_wave, label="Phase C Voltage")
plt.title("3-Phase Voltage Waveforms")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.grid()
plt.show()


df.to_csv("data.csv", index=False)
print("done!! 'data.csv'")
