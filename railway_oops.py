import pandas as pd

pd.DataFrame()
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

neerajApplication = RailwayForm()
neerajApplication.name = "neeraj"
neerajApplication.train = "Rajdhani Express"
neerajApplication.printData()