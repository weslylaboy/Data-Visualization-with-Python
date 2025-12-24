import matplotlib.pyplot as plt
import pandas as pd

from data import preprocess, read


def plot(votes: pd.DataFrame) -> plt.Figure:
    return  # TODO


# Please solve the task in the plot function and do not modify this one
def main():
    votes = read()
    votes = preprocess(votes)

    fig = plot(votes)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
