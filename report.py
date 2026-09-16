import pandas as pd

def create_report(log_data):
   df=pd.DataFrame(log_data)
   df.to_excel("organisation_report.xlsx", index=False)
