import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from PIL import Image

bildes = []
label = []

bilzu_adrese = "maju_meklesana/bildes/"

for nosaukums in os.listdir(bilzu_adrese):
    image = Image.open(os.path.join(bilzu_adrese,nosaukums)).resize((200,200), Image.Resampling.NEAREST)
    bildes.append(np.array(image))
    tests = np.array(bildes)
    if "maja" in nosaukums:
        label.append(1)
    else:
        label.append(0)

bildes = np.array(bildes)
label = np.array(label)

bildes = bildes/255.0 
bildes = bildes.reshape(bildes.shape[0], -1)

X_train, X_test, y_train, y_test = train_test_split(bildes, label, test_size=3)

modelis = RandomForestClassifier()

modelis.fit(X_train, y_train)

paregojums = modelis.predict(X_test)

precizitate = accuracy_score(y_test, paregojums)

print(precizitate)