import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from data import read, get_product_order


def plot(votes: pd.DataFrame) -> sns.FacetGrid:

    print(votes)
    g = sns.catplot(
        data=votes,
        y = 'product',
        order=get_product_order(votes),
        hue='category',
        kind = 'count')
    plt.show()
    return  g


# Please solve the task in the plot function and do not modify this one
def main():
    votes = read()

    fig = plot(votes)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
