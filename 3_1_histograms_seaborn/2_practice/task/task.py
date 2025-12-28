import pandas as pd
import seaborn as sns

from data import read, get_bins


def plot(sales: pd.DataFrame) -> sns.FacetGrid:
    print(sales.head())
    p = sns.displot(kind='hist', bins=get_bins(sales), data = sales, x = 'sales',
                    hue='city',
                    common_norm=False, stat='probability')

    return  p# TODO


# Please solve the task in the plot function and do not modify this one
def main():
    sales = read()

    fig = plot(sales)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
