import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from data import preprocess, read, add_decades, extract_sales_region, get_sorted_regions


def plot(games: pd.DataFrame) -> sns.FacetGrid:
    games = extract_sales_region(add_decades(games))
    return sns.catplot(data=games,
                       x=games['decade'], y ='sales',
                       hue='region',
                       hue_order=get_sorted_regions(games),
                       kind='bar',
                       estimator='sum',
                       errorbar=None,
                       )



# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
