import matplotlib.pyplot as plt
import pandas as pd

from data import preprocess, read, aggregate, filter_platforms


def plot_region(ax: plt.Axes, games: pd.DataFrame, region: str, trace: int = 0):
    # TODO: do not implement this function until the corresponding task
    pass


def plot(games: pd.DataFrame) -> plt.Figure:
    df = filter_platforms(aggregate(games))
    print(df.shape)

    fig, ax = plt.subplots()
    ax.barh(data = df, y= 'platform', width= 'count',
            color=[ 'grey', 'blue','green', 'cyan'])
    ax.set_xlabel('Count')
    ax.set_ylabel('Platform')
    ax.set_title('Number of games per platform')
    fig.tight_layout()
    # plt.show()
    return fig

# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
