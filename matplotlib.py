import matplotlib.pyplot as plt
goods = ['Beer', 'Vodka', 'Whisky', 'Wine']
counts = [678, 438, 948, 123]
plt.pie(counts, labels = goods)
plt.show()