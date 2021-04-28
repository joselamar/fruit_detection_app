import matplotlib.pyplot as plt
import json

json_data = {}
data = [json.loads(line) for line in open('/Users/JoseLamarao/Downloads/metrics.json', 'r')]
json_data['iteration'] = []
json_data['total_loss'] = []


for i in range (1,len(data)):
    json_data['iteration'].append(data[i]['iteration'])
    json_data['total_loss'].append(data[i]['total_loss']) 

plt.figure()
fig, ax = plt.subplots(3,3)
ax[0,0].set_title('Training Total Loss')
ax[0,0].plot(json_data['iteration'],json_data['total_loss'])
ax[0,0].set_ylabel('Total Loss')
ax[0,0].set_xlabel('Iterations')

plt.show()
fig.tight_layout()
