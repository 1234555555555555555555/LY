import pandas as pd

# 清洗生命清单中的无用信息
def clear_life():
    list2 = ["/home/mw/input/life5998/2018_SpeciesProfile.csv", "/home/mw/input/life5998/2019_SpeciesProfile.csv",
             "/home/mw/input/life5998/2020_SpeciesProfile.csv", "/home/mw/input/life5998/2021_SpeciesProfile.csv",
             "/home/mw/input/life5998/2022_SpeciesProfile.csv"]
    list3 = ["dwc:taxonID", "dcterms:language", "dwc:vernacularName", "dwc:locality"]
    data_exinct = []
    for i in list2:
        count = 0
        data1 = pd.read_csv(i, encoding="utf-8")
        del data1[list3[0]]
        del data1[list3[1]]
        del data1[list3[2]]
        del data1[list3[3]]

        # data1.to_csv(i, index=False, header=True)

# 清洗全球自然灾害无用数据

def clear_disa():
    fname = "/home/mw/input/disaster2792/Disaster.csv"
    dis_column = ["Dis No", "Disaster Group", "Country/Region", "Region", "Seq", "ISO", "Dis Mag Scale", "Location",
                  "Geo Locations", "OFDA Response", "Appeal", "Declaration", "AID Contribution ('000 US$)",
                  "Reconstruction Costs ('000 US$)", "Reconstruction Costs, Adjusted ('000 US$)",
                  "Insured Damages ('000 US$)", "Insured Damages, Adjusted ('000 US$)", "Total Damages ('000 US$)",
                  "Total Damages, Adjusted ('000 US$)", "CPI", "Adm Level", "Admin1 Code", "Admin2 Code",
                  "Total Deaths", "No Injured", "No Affected", "No Homeless", "Total Affected"]
    data2 = pd.read_csv(fname, encoding="utf-8")
    for i in dis_column:
        del data2[i]
    data2.to_csv(fname, index=False, header=True)



filename = ["/home/mw/input/endangered3545/Vulnerable.csv", "/home/mw/input/endangered3545/Endangered.csv",
            "/home/mw/input/endangered3545/Critically Endangered.csv", "/home/mw/input/disaster2792/Disaster.csv",
            "/home/mw/input/life5998/2018_SpeciesProfile.csv", "/home/mw/input/life5998/2019_SpeciesProfile.csv",
            "/home/mw/input/life5998/2020_SpeciesProfile.csv", "/home/mw/input/life5998/2021_SpeciesProfile.csv",
            "/home/mw/input/life5998/2022_SpeciesProfile.csv"]


def delwith():
    for i in filename:
        data = pd.read_csv(i, encoding="utf-8")
        # data.duplicated().sum()#查看重复值
        # 删除缺失率大于0.5的列
        t = int(0.5 * data.shape[0])
        data = data.dropna(thresh=t, axis=1)  # 保留至少有 t 个非空的列
        data.to_csv(i, index=False, header=True)
        # print(data.isnull().sum()/data.shape[0])

delwith()
clear_life()
clear_disa()