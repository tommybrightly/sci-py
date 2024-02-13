
import numpy as np
import random
import matplotlib.pyplot as plt
import math
from statistics import mean as statMean
def normalRandomGenerator(seed=1,dataLength=10000,numberSamples=50,lowLim=0,highLim=100):


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

def cumulativeDistribution(x):
    # constants
    a1 =  0.254829592
    a2 = -0.284496736
    a3 =  1.421413741
    a4 = -1.453152027
    a5 =  1.061405429
    p  =  0.3275911

    # Save the sign of x
    sign = 1
    if x < 0:
        sign = -1
    x = abs(x)/math.sqrt(2.0)

    # A&S formula 7.1.26
    t = 1.0/(1.0 + p*x)
    y = 1.0 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)*t*math.exp(-x*x)

    return 0.5*(1.0 + sign*y)
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

        # less gap in skewed data
        for x in range(len(skewedList)):
            skewedList[x] -= 20
        

        #Plot and label histogram
        ax[1,0].hist(newData+bimodalList+skewedList,bins=50,density=True)
        


        # CUMULATIVE DISTRIBUTION IN BOTTOM RIGHT CORNER

        xCumulative = np.arange(-3,3,0.1)
        yCumulative = [cumulativeDistribution(val) for val in xCumulative]


        ax[1,1].plot(xCumulative,yCumulative)

        #Add title to the figure and show it
        plt.suptitle('Thomas Brightly')

        plt.tight_layout()
        plt.show()

    #end run function
#end class Runner


