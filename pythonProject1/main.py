import by as by
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re as re

from pandas._libs.reshape import explode
from sklearn.linear_model import LinearRegression

assists = pd.read_csv("Assist.csv", index_col = "Player")
crosses = pd.read_csv("Crosses.csv", index_col = "Player")
passes = pd.read_csv("Passes.csv", index_col = "Player")
shotsOnTarget = pd.read_csv("ShotsOnTarget.csv", index_col = "Player")
throughBalls = pd.read_csv("ThroughBalls.csv", index_col = "Player")
blocks = pd.read_csv("Blocks.csv", index_col= "Player")
interceptions = pd.read_csv("Interceptions.csv", index_col= "Player")
tackles = pd.read_csv("Tackles.csv", index_col= "Player")
goals = pd.read_csv("Goals.csv", index_col= "Player")
gamesPlayed = pd.read_csv("GamesPlayed.csv", index_col = "Player")
fifa22Ratings = pd.read_csv("ORGFifa22.csv", index_col ="PLAYER")

df3 = pd.merge(assists, crosses, how="outer", left_index=True, right_index=True)
df3 = pd.merge(df3, passes, how="outer", left_index=True, right_index=True)
df3 = pd.merge(df3, shotsOnTarget, how="outer", left_index=True, right_index=True)
df3 = pd.merge(df3, throughBalls, how="outer", left_index=True, right_index=True)
df3 = pd.merge(df3, blocks, how="outer", left_index=True, right_index=True)
df3 = pd.merge(df3, interceptions, how="outer", left_index=True, right_index=True)
df3 = pd.merge(df3, tackles, how="outer", left_index=True, right_index=True)
df3 = pd.merge(df3, goals, how="outer", left_index=True, right_index=True)
df3 = pd.merge(df3, gamesPlayed, how="outer", left_index=True, right_index=True)
df3 = pd.merge(df3, fifa22Ratings, how="inner", left_index=True, right_index=True)
df3.fillna(0, inplace=True)

#Sorting
df3.sort_values(by = "Games Played", ascending=False, inplace=True, kind='quicksort', na_position='last', ignore_index=False, key=None)
df4 = df3.loc[df3["Games Played"] >= 5]
df5 = df4.copy()
#Changing Assists
#df5["Assist"] = (df4["Assist"]/df4["Games Played"]).rank(pct=True)
#df5.loc[df5["Assist"] < 0.6, "Assist"] = 0.6
df5["Assist"] = df4["Assist"]/df4["Games Played"]

x = df4["Assist"].values.reshape(-1, 1)
y = df4["PAS"].values.reshape(-1, 1)
regresser = LinearRegression()
regresser.fit(x, y)
#print(regresser.coef_)
#regression = regresser.predict(x)
#plt.scatter(x, y)
#plt.plot(x, regression)
#plt.show()

#Changing Crosses
#df5["Crosses"] = (df4["Crosses"]/df4["Games Played"]).rank(pct=True)
#df5.loc[df5["Crosses"] < 0.6, "Crosses"] = 0.6
df5["Crosses"] = df4["Crosses"]/df4["Games Played"]

x2 = df4["Crosses"].values.reshape(-1, 1)
y2 = df4["PAS"].values.reshape(-1, 1)
regresser2 = LinearRegression()
regresser2.fit(x2, y2)
#print(regresser2.coef_)
#Changing Passes
#df5["Passes"] = (df4["Passes"]/df4["Games Played"]).rank(pct=True)
#df5.loc[df5["Passes"] < 0.6, "Passes"] = 0.6
df5["Passes"] = df4["Passes"]/df4["Games Played"]

x3 = df4["Passes"].values.reshape(-1, 1)
y3 = df4["PAS"].values.reshape(-1, 1)
regresser3 = LinearRegression()
regresser3.fit(x3, y3)
#print(regresser3.coef_)
#Changing Shots on Target
#df5["Shots on Target"] = (df4["Shots on Target"]/df4["Games Played"]).rank(pct=True)
#df5.loc[df5["Shots on Target"] < 0.6, "Shots on Target"] = 0.6
df5["Shots on Target"] = df4["Shots on Target"] / df4["Games Played"]

x5 = df4["Shots on Target"].values.reshape(-1, 1)
y5 = df4["SHO"].values.reshape(-1, 1)
regresser5 = LinearRegression()
regresser5.fit(x5, y5)
#print(regresser5.coef_)
#Changing Through Balls
#df5["Through Balls"] = (df4["Through Balls"]/df4["Games Played"]).rank(pct=True)
#df5.loc[df5["Through Balls"] < 0.6, "Through Balls"] = 0.6
df5["Through Balls"] = df4["Through Balls"]/df4["Games Played"]

x4 = df4["Through Balls"].values.reshape(-1, 1)
y4 = df4["PAS"].values.reshape(-1, 1)
regresser4 = LinearRegression()
regresser4.fit(x4, y4)
#print(regresser4.coef_)
df5["myPAS"] = (regresser.coef_[0][0] * df5["Assist"] + regresser2.coef_[0][0] * df5["Crosses"] + regresser3.coef_[0][0] * df5["Passes"] + regresser4.coef_[0][0] * df5["Through Balls"])
#1.14848355 *

#Changing Blocks
#df5["Blocks"] = (df4["Blocks"]/df4["Games Played"]).rank(pct=True)
#df5.loc[df5["Blocks"] < 0.6, "Blocks"] = 0.6
df5["Blocks"] = df4["Blocks"]/df4["Games Played"]

x7 = df4["Blocks"].values.reshape(-1, 1)
y7 = df4["DEF"].values.reshape(-1, 1)
regresser7 = LinearRegression()
regresser7.fit(x7, y7)
#print(regresser7.coef_)
#Changing Interceptions
#df5["Interceptions"] = (df4["Interceptions"]/df4["Games Played"]).rank(pct=True)
#df5.loc[df5["Interceptions"] < 0.6, "Interceptions"] = 0.6
df5["Interceptions"] = df4["Interceptions"]/df4["Games Played"]

x8 = df4["Interceptions"].values.reshape(-1, 1)
y8 = df4["DEF"].values.reshape(-1, 1)
regresser8 = LinearRegression()
regresser8.fit(x8, y8)
#print(regresser8.coef_)
#Changing Tackles
#df5["Tackles"] = (df4["Tackles"]/df4["Games Played"]).rank(pct=True)
#df5.loc[df5["Tackles"] < 0.6, "Tackles"] = 0.6
df5["Tackles"] = df4["Tackles"]/df4["Games Played"]

x9 = df4["Tackles"].values.reshape(-1, 1)
y9 = df4["DEF"].values.reshape(-1, 1)
regresser9 = LinearRegression()
regresser9.fit(x9, y9)
#print(regresser9.coef_)
df5["myDEF"] = (regresser7.coef_[0][0] * df5["Blocks"] + regresser8.coef_[0][0] * df5["Interceptions"] + regresser9.coef_[0][0] * df5["Tackles"])
#0.552623031 *

#Changing Goals
#df5["Goals"] = (df4["Goals"]/df4["Games Played"]).rank(pct=True)
#df5.loc[df5["Goals"] < 0.6, "Goals"] = 0.6
df5["Goals"] = df4["Goals"]/df4["Games Played"]

x6 = df4["Goals"].values.reshape(-1, 1)
y6 = df4["SHO"].values.reshape(-1, 1)
regresser6 = LinearRegression()
regresser6.fit(x6, y6)
#print(regresser6.coef_)
df5["mySHO"] = (regresser5.coef_[0][0] * df5["Shots on Target"] + regresser6.coef_[0][0] * df5["Goals"])
#0.813833317

shoP = 1.5 * df5["myPAS"].max()
shoD = 1.5 * df5["myDEF"].max()
shoC = 1.5 * df5["mySHO"].max()

df5["myPAS"] = df5["myPAS"] + shoP
df5["myPAS"] = 100 * df5["myPAS"] / df5["myPAS"].max()

df5["myDEF"] = df5["myDEF"] + shoD
df5["myDEF"] = 100 * df5["myDEF"] / df5["myDEF"].max()

df5["mySHO"] = df5["mySHO"] + shoC
df5["mySHO"] = 100 * df5["mySHO"] / df5["mySHO"].max()

dfF1 = df5.loc[df5["Position"] == "F"]
dfF = dfF1.copy()
dfM1 = df5.loc[df5["Position"] == "M"]
dfM = dfM1.copy()
dfD1 = df5.loc[df5["Position"] == "D"]
dfD = dfD1.copy()

x10 = dfF["SHO"].values.reshape(-1, 1)
y10 = dfF["OVR"].values.reshape(-1, 1)
regresser10 = LinearRegression()
regresser10.fit(x10, y10)
#print(regresser10.coef_)

x11 = dfF["PAS"].values.reshape(-1, 1)
y11 = dfF["OVR"].values.reshape(-1, 1)
regresser11 = LinearRegression()
regresser11.fit(x11, y11)
#print(regresser11.coef_)

x12 = dfF["DEF"].values.reshape(-1, 1)
y12 = dfF["OVR"].values.reshape(-1, 1)
regresser12 = LinearRegression()
regresser12.fit(x12, y12)
#print(regresser12.coef_)

x13 = dfM["SHO"].values.reshape(-1, 1)
y13 = dfM["OVR"].values.reshape(-1, 1)
regresser13 = LinearRegression()
regresser13.fit(x13, y13)
#print(regresser13.coef_)

x14 = dfM["PAS"].values.reshape(-1, 1)
y14 = dfM["OVR"].values.reshape(-1, 1)
regresser14 = LinearRegression()
regresser14.fit(x14, y14)
#print(regresser14.coef_)

x15 = dfM["SHO"].values.reshape(-1, 1)
y15 = dfM["OVR"].values.reshape(-1, 1)
regresser15 = LinearRegression()
regresser15.fit(x15, y15)
#print(regresser15.coef_)

x16 = dfD["SHO"].values.reshape(-1, 1)
y16 = dfD["OVR"].values.reshape(-1, 1)
regresser16 = LinearRegression()
regresser16.fit(x16, y16)
#print(regresser16.coef_)

x17 = dfD["PAS"].values.reshape(-1, 1)
y17 = dfD["OVR"].values.reshape(-1, 1)
regresser17 = LinearRegression()
regresser17.fit(x17, y17)
#print(regresser17.coef_)

x18 = dfD["DEF"].values.reshape(-1, 1)
y18 = dfD["OVR"].values.reshape(-1, 1)
regresser18 = LinearRegression()
regresser18.fit(x18, y18)
#print(regresser18.coef_)


dfF["myOVR"] = 0.708760742 * (regresser10.coef_[0][0] * df5["mySHO"] + regresser11.coef_[0][0] * df5["myPAS"] + regresser12.coef_[0][0] * df5["myDEF"])

dfM["myOVR"] = 0.86683015 * (regresser13.coef_[0][0] * df5["mySHO"] + regresser14.coef_[0][0] * df5["myPAS"] + regresser15.coef_[0][0] * df5["myDEF"])

dfD["myOVR"] = 0.852223063 * (regresser16.coef_[0][0] * df5["mySHO"] + regresser17.coef_[0][0] * df5["myPAS"] + regresser18.coef_[0][0] * df5["myDEF"])


#frames = [df5, dfF, dfM, dfD]
df6 = dfF.copy()
df6 = df6.append(dfM)
df6 = df6.append(dfD)

#df6["myOVR"] = df6["myOVR"] + (df6["OVR"].mean() - df6["myOVR"].mean())

df6.sort_values(by = "myOVR", ascending=False, inplace=True, kind='quicksort', na_position='last', ignore_index=False, key=None)

bin1 = df6["OVR"]
bin2 = df6["myOVR"]

plt.hist(bin1, edgecolor="blue", alpha=0.5, bins=[61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99], label="OVR")
plt.hist(bin2, edgecolor="blue", alpha=0.5, bins=[61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99], label="myOVR")
plt.legend(loc="upper right")
plt.xlabel("OVR")
plt.ylabel("Players")
plt.show()

df7= df6.copy()
df7["OVR"] = 100*df7["OVR"]/df7["OVR"].max()
df7["myOVR"] = 100*df7["myOVR"]/df7["myOVR"].max()

bin3 = df7["OVR"]
bin4 = df7["myOVR"]

plt.hist(bin3, edgecolor="blue", alpha=0.5, bins=[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99, 100], label="OVR")
plt.hist(bin4, edgecolor="blue", alpha=0.5, bins=[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99, 100], label="myOVR")
plt.legend(loc="upper right")
plt.xlabel("OVR")
plt.ylabel("Players")
plt.show()

df6.plot.scatter(x="OVR", y="myOVR", title = "Correlation: 0.279454",  colormap = "prism", colorbar = True)
print(df6.corr())
plt.show()

df6["Nationality"].replace(["Guinea","Cameroon","Zambia","Egypt","Zimbabwe","Senegal","Mali","Algeria","Morocco","Cote D’Ivoire","Ghana","Nigeria"],["African","African","African","African","African","African","African","African","African","African","African","African"],inplace=True)
df6["Nationality"].replace(["Mexico","Grenada","Venezuela","Paraguay","Uruguay","Colombia","Argentina","Brazil","Jamaica"],["Americas","Americas","Americas","Americas","Americas","Americas","Americas","Americas","Americas"],inplace=True)
df6["Nationality"].replace(["England","Northern Ireland","Scotland","Wales"],["UK","UK","UK","UK"],inplace=True)
df6["Nationality"].replace(["Turkey","Iran","Japan","New Zealand"],["Asia","Asia","Asia","Asia"],inplace=True)
df6["Nationality"].replace(["Kosovo","Croatia","Ukraine","Slovakia","Italy","Albania","Greece","Finland","Poland","Sweden","Norway"],["Eastern Europe","Eastern Europe","Eastern Europe","Eastern Europe","Eastern Europe","Eastern Europe","Eastern Europe","Eastern Europe","Eastern Europe","Eastern Europe","Eastern Europe"],inplace=True)
nation = df6["Nationality"]
#print(nation.value_counts())

df6["Games Played Rank"] = 1
df6.groupby(['Nationality']).sum().plot(kind='pie', y='Games Played Rank', figsize = (8, 8), legend = False)
plt.ylabel('')
plt.show()

df6.groupby(['Nationality']).mean().plot(kind='bar', y='myOVR', legend = False)
plt.ylim(60,80)
plt.show()

team = df6["Club"]
#print(team.value_counts())

df6.groupby(['Club']).sum().plot(kind='pie', y='Games Played Rank', figsize = (8, 8), legend = False)
plt.ylabel('')
plt.show()

df6.groupby(['Club']).mean().plot(kind='bar', y='myOVR', legend = False, figsize = (10, 7), color=['blue','blue','blue','blue','blue','green','blue','blue','blue','blue','green','green','blue','blue','blue','blue','blue','blue','blue','blue'])
plt.ylim(60,80)
plt.show()

dfFinal = df6.copy()
dfFinal = dfFinal.drop(columns="Crosses")
dfFinal = dfFinal.drop(columns="Passes")
dfFinal = dfFinal.drop(columns="Assist")
dfFinal = dfFinal.drop(columns="Blocks")
dfFinal = dfFinal.drop(columns="Goals")
dfFinal = dfFinal.drop(columns="Interceptions")
dfFinal = dfFinal.drop(columns="Tackles")
dfFinal = dfFinal.drop(columns="Through Balls")
dfFinal = dfFinal.drop(columns="Shots on Target")
dfFinal = dfFinal.drop(columns="Games Played Rank")
dfFinal = dfFinal.drop(columns="Club")
dfFinal = dfFinal.drop(columns="Nationality")
dfFinal = dfFinal.drop(columns="Games Played")
dfFinal = dfFinal.drop(columns="DRI")
dfFinal = dfFinal.drop(columns="PHY")
dfFinal = dfFinal.drop(columns="PAC")
dfFinal = dfFinal.drop(columns="SHO")
dfFinal = dfFinal.drop(columns="PAS")
dfFinal = dfFinal.drop(columns="DEF")
dfFinal = dfFinal.drop(columns="myPAS")
dfFinal = dfFinal.drop(columns="mySHO")
dfFinal = dfFinal.drop(columns="myDEF")
diff = dfFinal["OVR"] - dfFinal["myOVR"]
dfFinal["Diff"] = diff

dfF2 = dfFinal.loc[dfFinal["Position"] == "F"]
dfF3 = dfF2.copy()
dfM2 = dfFinal.loc[dfFinal["Position"] == "M"]
dfM3 = dfM2.copy()
dfD2 = dfFinal.loc[dfFinal["Position"] == "D"]
dfD3 = dfD2.copy()

dfFinal = dfFinal.drop(columns="Position")

bin5 = dfF3["myOVR"]
bin6 = dfM3["myOVR"]
bin7 = dfD3["myOVR"]

plt.hist(bin5, edgecolor="blue", alpha=0.33, bins=[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90], label="F")
plt.hist(bin6, edgecolor="blue", alpha=0.33, bins=[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90], label="M")
plt.hist(bin7, edgecolor="blue", alpha=0.33, bins=[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90], label="D")
plt.legend(loc="upper right")
plt.xlabel("myOVR")
plt.ylabel("Players")
plt.show()


#result = pd.concat(frames)

#df5["myPAS"] = 100 * df5["myPAS"] / df5["myPAS"].max()
#df5["myDEF"] = 100 * df5["myDEF"] / df5["myDEF"].max()
#df5["mySHO"] = 100 * df5["mySHO"] / df5["mySHO"].max()

#print(df4["Assist"].rank(pct=True))
#print(df4.info())
#print(df6.describe().to_string(index=True))
print(dfD3.to_string(index=True))

#cross = df5["Crosses"].std()
#df5["Crosses"] = df5["Crosses"]/cross
#crossMax = df5["Crosses"].quantile(0.9)
#df5.loc[df5["Crosses"] > crossMax, "Crosses"] = crossMax
#df5["Crosses"] = df5["Crosses"]/crossMax


