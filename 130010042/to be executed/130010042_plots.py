from scipy.integrate import odeint
from numpy import arange
from pylab import *
import matplotlib.pyplot as plt

tnrfont = {'fontname':'Times New Roman'}
t = arange(0, 20, 0.1)
init_state = [1, 1]
def FrictionPendulumup(init_state, t, dam):
    def FrictionPendulum(init_state,t):
        vel, ang = init_state
        lam = dam
        d_vel = -(lam * vel + 9.8 * ang)
        d_ang = vel
        return [d_vel, d_ang]
    return FrictionPendulum

Frictionpen1 = FrictionPendulumup(init_state,t,0.5)


state = odeint(Frictionpen1, init_state, t)



k = range(0,20,1)
fig1 = plt.figure()
plt.plot(t,state[:, 1], 'b.', color="blue", linewidth=1, linestyle="-", label="Angular Velocity")
plt.plot(t,state[:, 0], 'r+', color="red",  linewidth=1, linestyle="-", label="Angular Position")
plt.grid()

plt.xlabel("Time",fontsize = 12,**tnrfont)
plt.legend(loc='upper right',fontsize = 10)
plt.title("130010042 Pendulum with Friction: Damping = 0.5",fontsize =12,**tnrfont)
plt.savefig("ud_pen.png")

Frictionpen1 = FrictionPendulumup(state,t,1)

t = arange(0, 20, 0.1)
init_state = [1, 1]
state = odeint(Frictionpen1, init_state, t)



k = range(0,20,1)
fig2 = plt.figure()
plt.plot(t,state[:, 1], 'b.', color="blue", linewidth=1, linestyle="-", label="Angular Velocity")
plt.plot(t,state[:, 0], 'r+', color="red",  linewidth=1, linestyle="-", label="Angular Position")
plt.grid()

plt.xlabel("Time",fontsize = 12,**tnrfont)
plt.legend(loc='upper right',fontsize = 10)
plt.title("130010042 Pendulum with Friction: Damping = 1",fontsize =12,**tnrfont)
plt.savefig("cd_pen.png")

Frictionpen1 = FrictionPendulumup(state,t,0)

t = arange(0, 20, 0.1)
init_state = [1, 1]
state = odeint(Frictionpen1, init_state, t)



k = range(0,20,1)
fig3 = plt.figure()
plt.plot(t,state[:, 1], 'b.', color="blue", linewidth=1, linestyle="-", label="Angular Velocity")
plt.plot(t,state[:, 0], 'r+', color="red",  linewidth=1, linestyle="-", label="Angular Position")
plt.grid()

plt.xlabel("Time",fontsize = 12,**tnrfont)
plt.legend(loc='upper right',fontsize = 10)
plt.title("13010042 Pendulum with Friction: Damping = 0",fontsize =12,**tnrfont)
plt.savefig("zer_pen.png")
