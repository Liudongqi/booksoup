import matplotlib as mpl
mpl.use('TkAgg')
from booksoup import BookSoup
import numpy as np
import matplotlib.pyplot as plt

# Enter the path to the top level of your facebook data folder below.
me = BookSoup("facebook-data")

# Enter the name of the conversation or the numerical ID below.
contact = me.load_conversation(274)

times = contact.interaction_freq()

objects = sorted(times.keys())
y_pos = np.arange(len(objects))
vals = [times[t] for t in objects]

plt.bar(y_pos, vals, align='center', alpha=0.5)
plt.xticks(y_pos, objects, fontsize=8, rotation=90)
plt.ylabel('Frequency')
plt.title('Interaction Frequency with ' + contact.name)

plt.show()
