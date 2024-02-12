'''
This code defines a Python module that generates random data sets and visualizes them 
using Matplotlib.

The module includes a function called normalRandomGenerator that takes several input 
parameters (including seed, data length, number of samples, and upper/lower limits) 
and returns a list of randomly generated values. The function generates dataLength 
values by repeatedly averaging numberSamples values randomly selected from a 
uniformly distributed population defined by lowLim and highLim.

The module also defines a class called Runner, which includes a method called run(). 
The run() method generates a new data set using the normalRandomGenerator function 
and then creates a 2x2 grid of subplots using Matplotlib. The upper-left subplot 
shows a histogram of the generated data using 50 bins, the lower-left subplot shows 
a box plot of the data, the upper-right subplot shows a violin plot of the data, 
and the lower-right subplot shows a "flipped" histogram.

Finally, the run() method adds a title to the overall figure, adjusts the layout 
of the subplots for better presentation, and shows the figure.
'''
import numpy as np
import random
import matplotlib.pyplot as plt
import math
from statistics import median, stdev, pstdev, mode, StatisticsError
from statistics import mean as statMean
def normalRandomGenerator(seed=1,dataLength=10000,numberSamples=50,lowLim=0,highLim=100):

    '''Create a new dataset of dataLength values consisting of the average of numberSamples 
    samples taken from a population of uniformly distributed values between lowLim 
    and highLim generated with a seed of seed.

    Input keyword parameters and their default values:

    seed = 1 seed used to generate the uniformly distributed values
    dataLength = 10000 number of samples in the returned list of values
    numberSamples = 50 number of samples taken from the uniformly distributed population
                       and averaged into the output
    lowLim = 0 lower limit value of the uniformly distributed population
    highLim = 100 high limit value of the uniformly distributed population

    returns: a list containing the dataset'''


    xData = []
    random.seed(seed)

    for cnt in range(dataLength):
        theSum = 0
        for cnt1 in range(numberSamples):
            theSum += random.uniform(lowLim,highLim)
        xData.append(theSum/numberSamples)
        
    return xData

def normalProbabilityDensity(x,mu=0,sigma=1.0):
    
    eVal = 2.718281828459045
    exp = -((x-mu)**2)/(2*(sigma**2))
    numerator = pow(eVal,exp)
    denominator = sigma*(math.sqrt(2*math.pi))
    return numerator/denominator

def standardNormalDistribution(x):

    eVal = 2.718281828459045
    exp = (-x**2)/2
    numerator = pow(eVal,exp)
    denominator = math.sqrt(2*math.pi)
    return numerator/denominator
#==============================================================================

class Runner():

    def run():

        print("I certify that this program is my own work")
        print("and is not the work of others. I agree not")
        print("to share my solution with others.")
        print("Thomas Brightly.")      
        
        #Create a figure with two rows and two columns.
        fig,ax = plt.subplots(2,2)

        #Create a dataset
        data = normalRandomGenerator(
          dataLength=10001,
          numberSamples=4,
          lowLim=0,
          highLim=400)
        
        
        # SCATTERPLOT FOR TOP LEFT CORNER
        # create data for scatter plot
        scat_data_x = []
        scat_data_y = []
        
        # create x data
        for num in range(101):
            scat_data_x.append(random.randint(0, 100))

        # create y data
        for num in scat_data_x:
            scat_data_y.append(num + np.random.normal(0, 15))

        # get averages for scatter plot
        xAvg = np.average(scat_data_x)
        yAvg = np.average(scat_data_y)      
           
        #Plot scatterplot in upper left quadrant
        ax[0,0].scatter(scat_data_x,scat_data_y, color='red', edgecolors='blue')
        

        # fitting a linear regression line
        slope, intercept = np.polyfit(scat_data_x, scat_data_y, 1)

        # Create a list of values in the best fit line
        abline_values = [slope * i + intercept for i in scat_data_x]

        # # adding the regression line to the scatter plot
        ax[0,0].plot(scat_data_x, abline_values, 'b')




        # BELL CURVE IN TOP RIGHT CORNER
        # plot a standard normal probability density function
        x = np.arange(-3,3,0.1)
        y = [standardNormalDistribution(val) for val in x]

        ax[0,1].plot(x, y)




        # BIMODAL HISTOGRAM IN BOTTOM LEFT CORNER

        #Create a dataset
        newData = normalRandomGenerator(
          dataLength=10001,
          numberSamples=20,
          lowLim=0,
          highLim=300)
        #Create another dataset
        bimodalList = normalRandomGenerator(
          dataLength=10001,
          numberSamples=4,
          lowLim=0,
          highLim=100)  
        #Create skewed dataset
        skewedList = normalRandomGenerator(
          dataLength=2000,
          numberSamples=4,
          lowLim=125,
          highLim=300)  
        
        # this leaves less gap between peaks
        for cnt in range(len(newData)):
            newData[cnt] -= 20

        

        #Plot and label histogram
        ax[1,0].hist(newData+bimodalList+skewedList,bins=50,density=True)
        


        # Plot a flipped histogram in the lower right quadrant
        mean = np.mean(data)
        centered_data = data - mean
        flipped_data = -centered_data
        flipped_data += mean
        ax[1,1].hist(flipped_data, bins=50, density=True)
        ax[1,1].grid(True)
        ax[1,1].set_title('Flipped Histogram')




        #Add title to the figure and show it
        plt.suptitle('Thomas Brightly')

        plt.tight_layout()
        plt.show()

    #end run function
#end class Runner


