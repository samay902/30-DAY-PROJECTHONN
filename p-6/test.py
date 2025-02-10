from sklearn.preprocessing import StandardScaler
import sklearn as sk
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
num_atr=["height","weight","iq"]
cat_atr=["country","religion","caste","city"]
num_pipeline=make_pipeline(SimpleImputer(strategy="median"),StandardScaler())
cat_pipeline=make_pipeline(SimpleImputer(strategy="most_frequent"),OneHotEncoder(handle_unknown="ignore"))
col_trans=ColumnTransformer([
("num",num_pipeline,num_atr),
("cat",cat_pipeline,cat_atr),
])
print(sk.__version__)
sorted(zip(rand_))