import matplotlib.pyplot as plt
import pandas as pd

from data import read, get_city_sales, get_weights, get_bins, get_median


def plot(sales: pd.DataFrame) -> plt.Figure:
    bins = get_bins(sales)
    bel_sales = get_city_sales(sales, "Belgrade")
    yer_sales = get_city_sales(sales, "Yerevan")


    bel = get_weights(bel_sales)
    yer = get_weights(yer_sales)

    yer_median = get_median(yer_sales)
    bel_median = get_median(bel_sales)



    fig, (ax1, ax2) = plt.subplots(2, 1, height_ratios=[1,10])
    ax1.scatter(yer_sales,  [0.1] * len(yer_sales), color = 'crimson', alpha = 0.05)

    ax1.scatter(bel_sales, [0.2] * len(bel_sales), color = "black", alpha = 0.05)
    ax1.spines[["top", "bottom", "left", "right"]].set_visible(False)

    ax1.set_ylim(0, 0.3)
    ax1.set_yticks([])
    ax1.set_xticks([])



    ax2.hist(yer_sales, bins = bins, label = "Yerevan", histtype= 'step',
                  color='crimson', weights= yer)
    ax2.axvline(yer_median, color = 'crimson', linestyle = '--',
                linewidth=1.5)
    ax2.text(yer_median - 25, 0.005, ha = 'right', s = f"{yer_sales.median():.1f}", color = 'crimson',)

    ax2.hist(bel_sales, bins = bins, label = "Belgrade", color = 'black',
              histtype= 'step', weights= bel)
    ax2.axvline(bel_median, color = 'black', linestyle = '--',
                linewidth=1.5, )
    ax2.text(bel_median + 25, 0.005, ha = 'left', s = f"{bel_sales.median():.1f}", color = 'black',)

    fig.suptitle("Sales Distribution in Belgrade and Yerevan")
    ax2.set_xlabel("Sales")
    ax2.set_ylabel('Probability')
    ax2.legend()


    return  fig# TODO


# Please solve the task in the plot function and do not modify this one
def main():
    sales = read()

    fig = plot(sales)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
