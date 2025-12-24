import pandas as pd
import seaborn as sns

from data import read


def plot(experiment: pd.DataFrame) -> sns.FacetGrid:
    return  sns.lmplot(data=experiment, x='x', y ='y',
                       line_kws={'color': 'navy'}, scatter_kws={'alpha': 0.05, 'color': 'grey'})


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
