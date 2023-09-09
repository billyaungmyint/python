import numpy as np
import pandas as pd

def generate_random_data():
    df = pd.DataFrame()
    df['col1'] = np.random.randint(0, 100, 100)
    df['col2'] = np.random.randint(0, 100,100)
    df['col3'] = np.random.randint(0, 100,100)
    print(df.head())

generate_random_data()