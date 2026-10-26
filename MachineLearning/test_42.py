import random
import plotly.express as px

sample_size = 31
sample_count = 1000

x_values = [ sum(random.uniform(0.0, 1.0) for _ in range(sample_size)) / sample_size for _ in range(sample_count)]
y_values = [1 for _ in range(sample_count)]
px.histogram(x=x_values, y=y_values, nbins=20).show()