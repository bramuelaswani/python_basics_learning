fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(x=df["P2.L1"], y=df["P2"])
ax.plot([0, 120], [0, 120], linestyle="--", color="orange")
plt.xlabel("P2.L1")
plt.ylabel("P2")
