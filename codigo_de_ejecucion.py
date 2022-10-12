import cloudpickle
import pandas as pd

from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import RandomForestClassifier

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

def ejecutar_modelos(df):

    with open('pipe_ejecucion.pickle', mode='rb') as file:
       pipe_ejecucion = cloudpickle.load(file)

    scoring = pipe_ejecucion.predict_proba(df)[:, 1]
    
    return(scoring)

