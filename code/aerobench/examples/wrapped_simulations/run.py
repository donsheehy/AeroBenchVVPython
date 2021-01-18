'''
Stanley Bak

should match 'GCAS' scenario from matlab version
'''

import math

from numpy import deg2rad
import matplotlib.pyplot as plt

from aerobench.run_f16_sim import run_f16_sim

from aerobench.visualize import plot

from aerobench.examples.gcas.gcas_autopilot import GcasAutopilot

class InitialConditions:
    def __init__(self,
                 power,
                 trim_aoa,
                 side_slip_angle,
                 altitude,
                 velocity,
                 roll,
                 pitch,
                 yaw,
                 P = 0,
                 Q = 0,
                 R = 0,
                 pn = 0,
                 pe = 0):
        self.power = power
        self.trim_aoa = trim_aoa
        self.side_slip_angle = side_slip_angle
        self.altitude = altitude
        self.velocity = velocity
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw
        self.P = P
        self.Q = Q
        self.R = R
        self.pn = pn
        self.pe =pe

    def aslist(self):
        # state = [vt, alpha, beta, phi, theta, psi, P, Q, R, pn, pe, h, pow]
        return [self.velocity,
                self.trim_aoa,
                self.side_slip_angle,
                self.roll,
                self.pitch,
                self.yaw,
                self.P,
                self.Q,
                self.R,
                self.pn,
                self.pe,
                self.altitude,
                self.power
                ]


def main():
    'main function'

    # ### Initial Conditions ###
    # engine power level (0-10)
    #
    # # Default alpha & beta
    # Trim Angle of Attack (rad)
    # Side slip angle (rad)
    #
    # # Initial Attitude
    # altitude (ft)
    # initial velocity (ft/sec)
    # Roll angle from wings level (rad)
    # Pitch angle from nose level (rad)
    # Yaw angle from North (rad)
    #

    init = InitialConditions(power = 9,
                             velocity = 540,
                             altitude = 1000,
                             trim_aoa = deg2rad(2.1215),
                             side_slip_angle = 0,
                             roll = -math.pi/8,
                             pitch = (-math.pi/2)*0.3,
                             yaw = 0)
    tmax = 3.51 # simulation time

    ap = GcasAutopilot(init_mode='roll', stdout=True, gain_str='old')

    res = run_f16_sim(init.aslist(), tmax, ap, extended_states=True)

    print(f"Simulation Completed in {round(res['runtime'], 3)} seconds")

    plot.plot_single(res, 'alt', title='Altitude (ft)')
    filename = 'alt.png'
    plt.savefig(filename)
    print(f"Made {filename}")

    plot.plot_attitude(res)
    filename = 'attitude.png'
    plt.savefig(filename)
    print(f"Made {filename}")

    # plot inner loop controls + references
    plot.plot_inner_loop(res)
    filename = 'inner_loop.png'
    plt.savefig(filename)
    print(f"Made {filename}")

    # plot outer loop controls + references
    plot.plot_outer_loop(res)
    filename = 'outer_loop.png'
    plt.savefig(filename)
    print(f"Made {filename}")

if __name__ == '__main__':
    main()
