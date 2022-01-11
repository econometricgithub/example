import pandas as pd
from statsmodels.miscmodels.ordinal_model import OrderedModel
url = "https://stats.idre.ucla.edu/stat/data/ologit.dta"
data_student = pd.read_stata(url)

mod_log = OrderedModel(data_student['apply'],
                        data_student[['pared', 'public', 'gpa']],
                        distr='logit')

res_log = mod_log.fit(method='bfgs', disp=False)
print(res_log.summary())

mod_log = OrderedModel(data_student['apply'],
                        data_student[['pared', 'public', 'gpa']],
                        distr='logit')

res_log = mod_log.fit(method='bfgs', disp=False)

print(res_log.summary())


