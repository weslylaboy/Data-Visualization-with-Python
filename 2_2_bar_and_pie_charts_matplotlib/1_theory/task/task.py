import matplotlib.pyplot as plt
import pandas as pd

from data import aggregate, get_number_of_decades, get_region_sales, preprocess, read, get_all_regions, get_number_of_regions, get_all_decades


def plot_region(ax: plt.Axes, games: pd.DataFrame, region: str, trace: int = 0):
    number_of_groups = get_number_of_decades(games)
    region_sales = get_region_sales(games, region)
    number_of_regions = get_number_of_regions(games)

    width = 1
    positions = []
    # print(decades)
    for j in range(number_of_groups):
        positions.append(j+ j*number_of_regions + width * trace)

    ax.bar(positions, region_sales, width, label=region)
    ax.legend()


def plot(games: pd.DataFrame) -> plt.Figure:
    games = aggregate(games)
    regions = get_all_regions(games)
    number_of_groups = get_number_of_decades(games)
    decades = get_all_decades(games)
    number_of_regions = get_number_of_regions(games)


    fig, ax = plt.subplots()
    for i, region in enumerate(regions):
        plot_region(ax, games, region, trace=i)

    width = 1

    ticks = [j + j * number_of_regions + (number_of_regions - 1) * width / 2 for j in range(number_of_groups)]
    ax.set_xticks(ticks, labels=[str(decade) for decade in decades])

    ax.set_xlabel("Decade")
    ax.set_ylabel('Sales')
    ax.set_title('Total sales for each region over decades')
    fig.tight_layout()
    return fig


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
