import json
import pickle
from typing import Union

import numpy as np
import pandas as pd

class Model:
    def infer(self, x: Union[dict, str, np.ndarray]):
        if isinstance(x, str):
            x = json.loads(x)
            
        if isinstance(x, dict):
            x = np.array(x['x'])
            
        result = pd.DataFrame(
            {
                'y1': np.sin(x),
                'y2': np.cos(x),
                'y3': np.sin(x) * np.cos(x)
            }
        )
        return result
    
if __name__ == '__main__':
    m = Model() 
    with open('model.pkl', 'wb') as fp:
        pickle.dump(m, fp) 
    