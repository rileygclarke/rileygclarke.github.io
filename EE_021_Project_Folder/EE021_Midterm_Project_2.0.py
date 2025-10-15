import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import math

#Functions
def capacitor_circuit(time_values, voltage_values):
    print("User has selected a capacitor circuit")
    resistance = 100
    print("The voltage of the capacitor is:")
    for time, voltage in zip(time_values, voltage_values):
        capacitance = 200
        capacitor_voltage = voltage * (1-(math.e ** (-1 * time_step/(resistance * capacitance))))
        print("Time:", time, "Voltage:", capacitor_voltage)
def resistor_circuit(time_values, voltage_values):
    print("User has selected a resistor circuit")
    resistance = 100
    charge = 0
    print("The charges going throught the circuit is:", charge)
    for time, voltage in zip(time_values, voltage_values):
        charge = voltage/resistance
        print("Time:", time, "Charge:",charge)



#Global variables
time_step = 0
time_scale = 15/1000 #seconds
waveform = ""

while True:
    show_graph_bool = input("Do you want to display graph? Choose Y/N")
    if show_graph_bool == "N":
        break
    print("Choose desired waveform from list: \n01. Sine wave \n02. Square wave \n03. Sawtooth wave")

    user_choice = int(input("What kind of wave form do you want generated?"))
    
    amplitude = float(input("What is the desired amplitude of the wave?"))
    frequency = float(input("What is the desired frequency of the wave?"))
    adjusted_frequency = 2 * np.pi * frequency

    fig, ax = plt.subplots()
    global y_values
    global t_values
    t_values,y_values = [], []
    line, = ax.plot(t_values, y_values, color="black")
    ax.set_xlim(0,1/frequency)
    ax.set_ylim(-1 * amplitude - (0.2 * amplitude),amplitude + (0.2 * amplitude))

    if user_choice == 1:
        waveform = "Sine wave"
    elif user_choice == 2:
        waveform = "Square wave"
    elif user_choice == 3:
        waveform == "Sawtooth wave"
    else:
        waveform = ""

    def animate(_):
        global time_step

        t = time_step * time_scale #seconds per frame
        
        if user_choice == 1:
            y = amplitude * np.sin(adjusted_frequency * t)
        elif user_choice == 2:
            y = signal.square(adjusted_frequency * t, duty=0.5)
        elif user_choice == 3:
            y = signal.sawtooth(adjusted_frequency * t, 0.5)
        else:
            exit()
        
        t_values.append(t)
        y_values.append(y)

        if len(t_values) >= 50:
            t_values.pop(0)
            y_values.pop(0)
            ax.set_xlim(t_values[0], t_values[-1])
        line.set_data(t_values, y_values)
        time_step += 1
        return line,


    print("The user has selected:", waveform, "of amplitude:", amplitude, "and frequency:", frequency)
    anim = animation.FuncAnimation(fig, animate, interval = 50, repeat = True, blit = True, cache_frame_data=False)
    plt.title(waveform)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.show()
    print("Circuit choices are: \n01. capacitor circuit \n02. resistor circuit")
    circuit_choice = int(input("What circuit do you want to simulate? Enter 1 or 2"))
    if circuit_choice == 1:
        capacitor_circuit(t_values, y_values)
    elif circuit_choice == 2:
        resistor_circuit(t_values, y_values)
    else:
        exit()

