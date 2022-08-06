import matplotlib.pyplot as plt
import math as m

def plot_graph(cycleN,memAddress):
    
    print("\n")
    plt.scatter(cycleN,memAddress, color='blue')
    plt.title('Scatter Plot Graph', fontsize=20)
    plt.xlabel('Cycle Number', fontsize=20)
    plt.ylabel('Memory Adress', fontsize=20)
    plt.show()
    