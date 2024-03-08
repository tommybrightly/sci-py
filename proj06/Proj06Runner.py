import numpy as np
import matplotlib.pyplot as plt

class Runner():

    def run():

        # CERTIFICATION
        print("I certify that this program is my own work")
        print("and is not the work of others. I agree not")
        print("to share my solution with others.")
        print("Bri-0802")
        fig,axes = plt.subplots(2,2,
                        facecolor='0.75',
                        linewidth=10,
                        edgecolor='Red')
        fig.set_facecolor('0.75')
        x = np.arange(0, 6.0, 0.05)
        ax0,ax1,ax2,ax3 = axes.flatten()


        # TOP LEFT
        axes[0,0].plot(x, np.sin(1.5*np.pi*x))

        # TOP RIGHT
        ax1.set_xlim(0,1)
        x = np.arange(0, 6.0, 0.005)
        ax1.plot(x, np.exp(-x) * np.cos(5*np.pi*x))
        
        # axes[0,1].plot(t, np.exp(-t) * np.cos(2*np.pi*t))
        # axes[1,0].plot(t, np.exp(-t) * np.cos(3*np.pi*t))
        # axes[1,1].plot(t, np.exp(-t) * np.cos(4*np.pi*t))
        
        # turn on grids
        axes[0,0].grid(True)
        axes[0,1].grid(True)

        # labels
        axes[0,0].set_title("A Sine")
        axes[0,0].set_xlabel("This is an xlabel")
        axes[0,0].set_ylabel("This is a ylabel")

        ax1.set_title("A damped cosine")
        ax1.set_ylabel('This is a ylabel')
        ax1.set_xlabel('This is an xlabel')



        fig.suptitle('Bri-0802')
        plt.tight_layout()
        plt.show()