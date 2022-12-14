import newModel
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from tqdm import tqdm
import matplotlib
import pandas as pd

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

def data(vec):
    x = np.arange(0, int(max(vec))+1)
    y = np.zeros(int(max(vec))+1)
    for element in vec:
        y[int(element)] += 1
    return x,y

net = newModel.newModel(5,10**5)
n = 1*10**6
for i in tqdm(range(int(n))):
    net.evolveSavings()

sns.distplot(net.getPlayers(), hist=False)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Capital (a. currency)')
plt.ylabel('Frequency (a.u.)')
plt.ylim([10**(-6),10**(1)])
# plt.savefig("./tex/img/savings.pgf")
# plt.show()

plt.clf()

df = pd.read_csv("./data/adult_cleaned.csv")
data = df['fnlwgt'].values.tolist()

data = [x/(10**5) for x in data]

sns.distplot(data, hist=False)
sns.distplot(net.getPlayers(), hist=False)
plt.xlabel('Capital (US dollars)')
plt.ylabel('Frequency (a.u.)')
plt.yscale('log')
plt.xscale('log')
plt.legend(['Real data','Simulation'], fontsize=12)
plt.xlim([10**(-1),2*10**1])
plt.ylim([10**(-8),10])
plt.savefig("./tex/img/real_overlay_savings.pgf")
