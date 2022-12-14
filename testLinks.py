import matplotlib.pyplot as plt
import numpy as np
import network as n
from tqdm import tqdm
import ROOT
from ROOT import gStyle
from ROOT import gPad
import matplotlib

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

def data(vec):
    x = np.arange(0, max(vec)+1)
    y = np.zeros(max(vec)+1)
    for element in vec:
        y[element] += 1
    return x,y

net = n.network(5, 50, 50)
net.createLinks(12)

n = 2*10**5
for i in tqdm(range(n)):
    net.evolveFixed()

x = data(net.getPlayers())[0][1::].tolist()
y = data(net.getPlayers())[1][1::].tolist()
y = [i/sum(y) for i in y] # normalization

h = ROOT.TH1F("h", "Fair Game", len(x), 0, 32)
for i in range(len(x)):
    h.Fill(x[i], y[i])

# fitting and extracting fit function
h.Fit("expo")
f = h.GetListOfFunctions().FindObject("expo")
print("ChiSquare/NDF = " + str(round(f.GetChisquare()/f.GetNDF(), 3)))
print("p-value = " + str(round(f.GetProb(), 3)))

plt.plot(x,y,'.',markersize=12)
fitX = np.arange(min(x), 32, 0.1)
fitY = np.exp(f.GetParameter("Constant")+f.GetParameter("Slope")*fitX)
plt.plot(fitX, fitY, color="red")
plt.yscale("log")
plt.xlabel('Capital (a. currency)')
plt.ylabel('Frequency (a.u.)')
plt.legend(['Simulated data','Fit line'], fontsize=12)
plt.xlim([0,35])
plt.savefig("./tex/img/fixedExpo.pgf")

probabilities = net.calcProb(net.getPoors())
prob_linked_and_poor = probabilities[0]
prob_linked = probabilities[1]
print("Contant: ", str(round(np.exp(f.GetParameter("Constant")), 3)))
print("Slope: ", str(round(f.GetParameter("Slope"), 3)))
print("Probability of having a link given their poorness: " + str(round(prob_linked_and_poor*100, 2)) + "%")
print("Probability of having a link in general: " + str(round(prob_linked*100, 2)) + "%")
