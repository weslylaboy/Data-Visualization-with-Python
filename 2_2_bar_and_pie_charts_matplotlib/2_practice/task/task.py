from shutil import which

import matplotlib.pyplot as plt
import pandas as pd

from data import preprocess, read, get_category_product_names, get_category_votes, get_category_size, get_categories


def plot(votes: pd.DataFrame) -> plt.Figure:
    categories = get_categories(votes)

    colors = {'bread': 'sienna', 'cheese' : 'goldenrod', 'salad' : 'forestgreen'}
    print(type(categories))
    categories.reverse()
    print(categories)

    product_names = []
    votes_count = []

    fig, ax = plt.subplots(figsize=(10, 6))

    for i, category in enumerate(categories):
        print(f" cat: {category}")
        product_names = get_category_product_names(votes, category)
        print(f" berfore  names: {product_names}")

        product_names.reverse()
        print(f"after  names: {product_names}")

        votes_count = get_category_votes(votes, category)
        print(f" before votes_count: {votes_count}")
        votes_count.reverse()
        print(f"after  votes_count: {votes_count}")
        print(f" votes_count[i]: {votes_count[i]}")

        print(f"colors: {colors[category]}")
        bars = ax.barh(y = product_names, width = votes_count, label = category, color = colors[category])
        for j, bar in enumerate(bars):
            print(f"real value count: {votes_count[j]}")
            ax.text(x=bar.get_width() + 1, y= bar.get_y() + bar.get_height()/2, s=f"{round(votes_count[j], 1)}", va='center')

    print(product_names)
    print(votes_count)

    handles,labels = ax.get_legend_handles_labels()
    ax.legend(reversed(handles), reversed(labels), loc='upper right')

    # Set major ticks (0, 25, 50, 75, 100)
    ax.set_xticks(range(0, 101, 25))

    # Set minor ticks (0, 5, 10, 15, ..., 95, 100)
    ax.set_xticks(range(0, 101, 5), minor=True)

    ax.set_xlim(0, 100)

    ax.tick_params(which='both', top=True, labeltop=True, bottom=True, labelbottom=True,
                   axis='x' )
    plt.xlabel("Respondents, %")
    plt.ylabel('Product name')

    plt.title("Distribution of votes per category")
    plt.tight_layout()

    return fig # TODO


# Please solve the task in the plot function and do not modify this one
def main():
    votes = read()
    votes = preprocess(votes)

    fig = plot(votes)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
