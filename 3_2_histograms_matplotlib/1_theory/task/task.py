import matplotlib.pyplot as plt
import pandas as pd

from data import preprocess, read, filter_by_global_sales, filter_by_publisher, get_weights, get_bins


def plot(games: pd.DataFrame) -> plt.Figure:
    fig = plt.figure()
    ea_games = filter_by_publisher(games, 'Electronic Arts')
    ubi_games = filter_by_publisher(games, 'Ubisoft')
    ea_games = filter_by_global_sales(ea_games)
    ubi_games = filter_by_global_sales(ubi_games)
    ea_weights = get_weights(ea_games)
    ubi_weights = get_weights(ubi_games)
    bins = get_bins(games)

    ax = fig.add_subplot()

    ax.hist(data = ea_games, x = 'global_sales', alpha =0.7, weights = ea_weights, histtype = 'step',
            bins=bins, label=ea_games['publisher'])
    ax.hist(data = ubi_games, x = 'global_sales', alpha =0.7, weights = ubi_weights,
            histtype = 'step', bins=bins, label=ubi_games['publisher'])

    ax.set_xlabel('Global Sales (millions)')
    ax.set_ylabel('Proportion')
    ax.legend()

    ax.set_title('Global Sales Distribution for Electronic Arts and Ubisoft')

    return  fig # TODO


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
