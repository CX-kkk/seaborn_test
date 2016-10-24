import numpy as np
import pandas as pd 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.set(color_codes=True)
np.random.seed(sum(map(ord,"regression")))
#matplotlib inline

tips = pd.read_csv("E:/my_scriptLib/JolieXPackage/python/studio/JolieX/seaborn/aaa.csv",error_bad_lines=False)

#tips = sns.load_dataset(".csv")
test = sns.regplot(x="TranslateX",y="TranslateZ",data=tips).figure.savefig("E:/my_scriptLib/JolieXPackage/python/studio/JolieX/seaborn/test.png")### Save a pic
### use plt Figure display
sns.plt.show()
