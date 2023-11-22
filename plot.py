import numpy as np
import matplotlib.pyplot as plt

# Light stimuli duration
t_max = 30; # minutes

# Update period of PWM
periodo = 1 # each second

# time vector definition
t = np.arange(0,t_max,(periodo/60))

#☻ Amplitude from the PWM resolution
res = 4; # 12 bits resolution
amp_max = 2**res -1

# Duration of stimuli
on_off = np.array([4,9,14,17,22,23])+0.25;

mascara = np.zeros((1,len(t)));
pendientes = np.zeros((1,len(t)));
x2 = np.zeros((1,len(t)));

for i in range(len(on_off)):
    if i%2 == 0:
        segmento = (t<=on_off[i + 1])*(t>=on_off[i])
        m = amp_max/( on_off[i + 1] - on_off[i] );
        mascara = mascara + segmento;
        pendientes = pendientes + m*segmento;
        x2 = x2 + segmento*on_off[i + 1];


# Sinus signal
frec = 0.05 # Sinus frequency
sen = np.sin(2*np.pi*frec*t*60)
senoidal = np.floor( amp_max*(sen + 1)/2 )*mascara

# square signal
cuadrado = amp_max*mascara

# Ramp signal
rampa = np.floor((amp_max - pendientes*(x2 - t))*mascara)

plt.figure(1)
plt.suptitle('Signals for '+str(res)+'bits PWM')

plt.subplot(3,1,1)
plt.title('Sinus Signal')
plt.step(t,senoidal.T,'deepskyblue')
plt.grid('on')
plt.axis([0, t_max, 0, amp_max+amp_max*0.1])

plt.subplot(3,1,2)
plt.title('Square Signal')
plt.step(t,cuadrado.T,'r')
plt.grid('on')
plt.axis([0, t_max, 0, amp_max+amp_max*0.1])

plt.subplot(3,1,3)
plt.title('Ramp Signal')
plt.step(t,rampa.T,'orange')
plt.grid('on')
plt.axis([0, t_max, 0, amp_max+amp_max*0.1])
plt.savefig('plots.png',dpi=300)
plt.show()

