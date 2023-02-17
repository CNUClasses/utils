# importing required libraries
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#want interactivity in a jupyter notebook?
#install ipympl
# !conda install -c conda-forge ipympl -y
#and then turn on the widget by running this magic
#%matplotlib ipympl

#determines color of points plotted, typically cluster number
colors1 = {-1:"black",
            0:"cyan",
           1:"orange", 
           2:"purple",
           3:"green",
          4:"yellow",
          5:"red",
          6:"blue",
           7:"teal",
           8:"pink",
           9:"gold",
           10:"royalblue",
           11:"bisque",
           12:"brown"
          }

#TODO plot a 3D plot of first 3 PCA components, set hue to the cluster_guess from KMeans above
# used for custom color palette below
def plot_3D(x,y,z,hue, labels=['x','y','z','Title'], clrs=colors1):
    '''
    A 3d plot
    x pd.series for x axis
    y pd.series for y axis
    z pd.series for z axis
    hue pd.series of ints for hue, mapped to clrs, if hue has more than (len(colors1)) values then extend colors1
    clrs dict (see above) 
    '''
    # creating figure
    fig = plt.figure();

    ax = Axes3D(fig,auto_add_to_figure=False)
    ignore=fig.add_axes(ax)
    ignore=ax.set_facecolor("white");
    ignore=ax.grid(color="black");
    
    # creating the plot
    ignore=ax.scatter(x, y, z, c=hue.map(clrs))
    
    # setting title and labels
    ignore=ax.set_title(labels[3])
    ignore=ax.set_xlabel(labels[0])
    ignore=ax.set_ylabel(labels[1])
    ignore=ax.set_zlabel(labels[2])
    plt.show()