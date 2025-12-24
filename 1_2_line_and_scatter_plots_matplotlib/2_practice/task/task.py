import matplotlib.pyplot as plt
import pandas as pd

from data import read


def plot(experiment: pd.DataFrame) -> plt.Figure:

    fig, ax = plt.subplots()

    ax.plot(experiment['x'] ,experiment['approximated_y'], color='navy')
    ax.scatter(data=experiment, x='x', y='y', color='grey', alpha=0.05)

    ax.spines[['top', 'right']].set_visible(False)
    ax.set_xticks([-4,0,4])
    ax.set_yticks([-1.5,0,1.5])
    ax.set_xlim([-4,4])
    ax.set_ylim([-2,2])
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    #insets
    ax_inset = ax.inset_axes([0.15,0.7, 0.3, 0.3], xlim=[0.5,1.5], ylim=[0.6,1.1], xticks=[0.5,1.5], yticks=[0.6,1.1])

    ax_inset.plot(experiment['x'] ,experiment['approximated_y'], color='navy')
    ax_inset.scatter(data=experiment, x='x', y='y', color='grey', alpha=0.05)
    ax.indicate_inset_zoom(ax_inset)



    return  fig# TODO


# Please solve the task in the plot function and do not modify this one
def main():
    experiment = read()

    fig = plot(experiment)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
