import matplotlib.pyplot as plt
import pandas as pd

from data import preprocess, read


def plot_region(ax: plt.Axes, games: pd.DataFrame, region: str, trace: int = 0):
    # TODO: do not implement this function until the corresponding task
    pass


def plot(games: pd.DataFrame) -> plt.Figure:
    return  # TODO


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
