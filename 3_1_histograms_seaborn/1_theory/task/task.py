import pandas as pd
import seaborn as sns

from data import preprocess, read, filter_by_global_sales, filter_by_publisher


def plot(games: pd.DataFrame) -> sns.FacetGrid:
    games = filter_by_publisher(games)
    games = filter_by_global_sales(games)
    p = sns.displot(kind='hist', data = games, x = 'global_sales', bins = 10,
                    hue = games['publisher'], stat='probability', common_norm = False)
    return p # TODO


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
