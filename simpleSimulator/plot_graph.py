import matplotlib.pyplot as plt
import math as m
cycleCount=[]
memAddress=[]

def plot_graph(cycleCount,memAddress):
    
    print("\n")
    plt.scatter(cycleCount,memAddress, color='blue')
    plt.title('Scatter Plot Graph', fontsize=20)
    plt.xlabel('Cycle Number', fontsize=20)
    plt.ylabel('Memory Adress', fontsize=20)
    plt.show()
    