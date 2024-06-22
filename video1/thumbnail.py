import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', **{'family': 'STIXGeneral'})

my_dpi = 96
fs = 76  # font size
margin = 0.1  # from bottom and top
real_estate = 1 - 2*margin  # how much of the page we actually want to use
lines = ["LLMs CAN", "DECEIVE", "THEIR USERS", "WHEN PUT", "UNDER", "PRESSURE"]
gap = real_estate / len(lines)
ys = [margin + i*gap for i in range(len(lines))][::-1]


fig, ax = plt.subplots(figsize=(1080/my_dpi, 1920/my_dpi), dpi=my_dpi)
for l, y in zip(lines, ys):
    ax.text(x=0.5, y=y, s=l, fontsize=fs, ha='center', va='center')
# ax.text(x=0.5, y=top, s='LLMs CAN', fontsize=76, ha='center', va='center')
# ax.text(x=0.5, y=top-2*gap, s='DECEIVE', fontsize=76, ha='center', va='center')
# ax.text(x=0.5, y=top-3*gap, s='THEIR USERS', fontsize=76, ha='center', va='center')
# ax.text(x=0.5, y=top-4*gap, s='WHEN PUT', fontsize=76, ha='center', va='center')
# ax.text(x=0.5, y=top-5*gap, s='UNDER', fontsize=76, ha='center', va='center')
# ax.text(x=0.5, y=top-6*gap, s='PRESSURE', fontsize=76, ha='center', va='center')
# ax.text(x=0.5, y=0.7, s="LLMs CAN \n STRATEGICALLY \n DECEIVE \n THEIR USERS",
#         fontsize=fs, ha='center', va='center', wrap=True)
ax.set_xticks([])
ax.set_yticks([])
plt.show()
