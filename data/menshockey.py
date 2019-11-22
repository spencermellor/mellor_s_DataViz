import csv
import matplotlib.pyplot as plt

# pie chart for men's hockey medal colours (gold, silver, bronze)
# arrays for each colour

golds = []
silver = []
bronze = []

categories = []

# opens up the csvfile with the csv reader
with open ('menshockey.csv') as csvfile:
	reader = csv.reader(csvfile)

	line_count = 0

# removing the first line of code so that it doesn't appear in our chart.
	for row in reader:
		if line_count is 0:
			# parse that first row of text data out of the file
			categories.append(row)
			line_count += 1
		else:
			if row[7] == "Gold":
				print("won gold!")
				golds.append(row[7])

			elif row[7] == "Silver":
				print("won silver!")
				silver.append(row[7])

			elif row[7] == "Bronze":
				print("won bronze! Is that even winning?")
				bronze.append(row[7])

			line_count += 1

print("gold medals: ", len(golds))
print("silver medals: ", len(silver))
print("bronze medals: ", len(bronze))

# plot a pie chart!

labels = ("Gold", "Silver", "Bronze")
# sizes are how many and how large the slices of the pie chart will be
sizes = [len(golds), len(silver), len(bronze)]
colors = ['gold', 'silver', 'darkgoldenrod']
explode = (0.1, 0, 0)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Medals for Men's Hockey")
plt.xlabel("Medals since 1924")
plt.show()





