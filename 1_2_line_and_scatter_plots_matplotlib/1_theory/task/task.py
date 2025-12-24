import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from data import preprocess, read, aggregate


def plot(games: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots()
    agg = aggregate(games)


    ax.set_xlabel("User Score")
    ax.set_ylabel('Critic Score')
    ax.set_xticks(range(0,11))
    ax.set_yticks(range(0, 110, 10))
    ax.spines[['top','right']].set_visible(False)
    ax.plot(agg['user_score'], agg['critic_score'], color='firebrick')
    ax.scatter(games['user_score'], games['critic_score'], alpha=0.1)
    return  fig


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
