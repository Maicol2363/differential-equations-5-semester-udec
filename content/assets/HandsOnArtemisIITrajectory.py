import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
import astropy.coordinates as coord 
from datetime import datetime

'''
This should be the path in which you have the data file downloaded from the Artemis II website.
Basically here: https://www.nasa.gov/missions/artemis/artemis-2/track-nasas-artemis-ii-mission-in-real-time/

In the obsidian vault the file.txt is located in the same folder as this code
'''

data_path = r"G:\My Drive\obsidianVault_Drive\University\Differential_Equations\assets\Artemis_II_OEM_2026_04_02_to_EI_v3.asc"

data = np.loadtxt(data_path, skiprows=20, dtype=str)

artemis_t = [datetime.fromisoformat(t) for t in data[:, 0]]
artemis_vec  = data[:, 1:].astype(float)

artemis_t_sec = [(t - artemis_t[0]).total_seconds() for t in artemis_t]

artemis_v = np.linalg.norm(artemis_vec[:, 3:], axis=1)


ax = plt.figure().add_subplot(projection='3d')
ax.scatter(artemis_vec[:, 0], 
           artemis_vec[:, 1], 
           artemis_vec[:, 2], 
           c = artemis_v) 

# This is the position of the Earth in the plot, 
# since the data is in an Earth-centered inertial frame, 
# the Earth is at the origin (0,0,0)
ax.plot(0,0,0, 'g.', markersize=20, label='Earth')

plt.show()
