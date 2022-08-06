import matplotlib.pyplot as plt
import math as m
cycleN=[]
memAdd=[]
def plot_graph(cycleN,memAdd):
    
    print("\n")
    plt.scatter(cycleN, memAdd, color='black')
    plt.title('Scatter Plot Graph', fontsize=20)
    plt.xlabel('Cycle Number', fontsize=20)
    plt.ylabel('Memory Adress', fontsize=20)
    plt.show()
    