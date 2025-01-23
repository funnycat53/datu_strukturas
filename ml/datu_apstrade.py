import pandas as pd #failu apstrade
import matplotlib.pyplot as plt #grafiki
import seaborn as sb #vizualizacijas

sb.set_style('whitegrid')
plt.rcParams['figure.figsize']=(15,10)

fails1 = "ml/auto_simple.csv"
fails2 = "ml/auto_imports.csv"

def heat_map(datne):
    datu_fails = pd.read_csv(datne).select_dtypes('number')
    sb.heatmap(datu_fails.corr(), annot=True, cmap='magma')
    plt.show()
    return

def distribution(datne, kolonna):
    datu_fails = pd.read_csv(datne)
    sb.histplot(datu_fails[kolonna], color='r')
    plt.show()


heat_map(fails2)