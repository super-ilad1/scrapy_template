import pandas as pd
import random
database=pd.read_csv(r"D:\PycharmProject\scrapY_oxfold\scrapy_oxfold\scrapy_oxfold\spiders\vocabularies.csv")
list_=list(range(0,4267))
random.shuffle(list_)
database=database.reindex(index=list_)


database['words']=database['words'].str.replace("_1","")
# print((database))

page=0
number=0
for i in range(9):
    page+=1

    db_export=database.iloc[number:number+500]

    number+=500

    db_export.to_csv(f"D:\\PycharmProject\\scrapY_oxfold\\scrapy_oxfold\\scrapy_oxfold\\spiders\\real_voc_{page}.csv",index=False)