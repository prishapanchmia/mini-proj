import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
	buffered = BytesIO()
	plt.savefig(buffered,format="png")
	buffered.seek(0)
	image_png = buffered.getvalue()
	graph = base64.b64encode(image_png)
	graph = graph.decode('utf-8')
	buffered.close()
	return graph

def get_plot():
	df1 = pd.read_csv('coviddata.csv')
	groups = df1.groupby('State/UnionTerritory').agg({'Confirmed':'sum'}).sort_values(by='Confirmed',ascending=False).head(10)
	x , y = groups.Confirmed.index , groups.Confirmed.values
	plt.switch_backend('AGG')
	plt.figure(figsize=(13,6))
	plt.plot(x,y)
	plt.tight_layout()
	graph = get_graph()
	print(x,y)
	return graph