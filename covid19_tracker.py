######################### PROGRAMMER : S.MUKILAN ##############################

import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import tkinter as tk
import requests
from io import BytesIO
import matplotlib.pyplot as plt
from urllib.request import urlopen
from PIL import Image,ImageTk

my_url = requests.get("https://www.worldometers.info/coronavirus/").text
data_corona = BeautifulSoup(my_url, 'html.parser')
covid_data = data_corona.findAll('div',{'class':"maincounter-number"})

corona = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv")
corona.to_csv('covid19_data.csv')
covid_19 = pd.read_csv('covid19_data.csv')
corona["Country_Region"] = corona["Country_Region"].str.lower()
countrys = []
mortality_data = covid_19.sort_values('Mortality_Rate',ascending=False).head(7)
confirmed_data = covid_19.sort_values('Confirmed',ascending=False).head(7)
death_data = covid_19.sort_values('Deaths',ascending=False).head(7)
recovered_data = covid_19.sort_values('Recovered',ascending=False).head(7)
active_data = covid_19.sort_values('Active',ascending=False).head(7)

for i in corona["Country_Region"]:
   countrys.append(i)
   
WINDOW =tk.Tk()
WINDOW.geometry('800x600')
WINDOW.title('COVID-19 TRACKER')
tk.Label(WINDOW,fg='blue',font=(None, 11),text='@creator by S.MUKILAN').place(x=10,y=575)
title = Image.open('img_corona.png')
virus = Image.open('corona.png')
world_chart = Image.open('world_data.png')
world_chart = ImageTk.PhotoImage(world_chart)
virus = ImageTk.PhotoImage(virus)
title = ImageTk.PhotoImage(title)
title_img = tk.Label(WINDOW,image=title).place(x=330,y=10)
virus_img = tk.Button(WINDOW,image=virus).place(x=260,y=470)
world_chart_img = tk.Label(WINDOW,image=world_chart).place(x=390,y=100)
sym = Image.open('symptoms.png')
sym = ImageTk.PhotoImage(sym)
sym_img = tk.Label(WINDOW,image=sym)
sym_img.place(x=390,y=325)
    
def country_corona_detail(country):
    global d1,d2,d3,d4,d5,d6,d7
    country_detail = corona.set_index("Country_Region")  
    d1 = tk.Label(WINDOW, font=(None,10), text='COUNTRY                   :    '+ str(country).upper())
    d1.place(x=80,y=225)
    d2 = tk.Label(WINDOW, font=(None, 10),text='CONFIRMED CASES   :    '+ str(int(country_detail.loc[str(country)]['Confirmed'])))
    d2.place(x=80,y=255)
    d3 = tk.Label(WINDOW, font=(None, 10),text='RECOVERED CASES  :    '+ str(int(country_detail.loc[str(country)]['Recovered'])))
    d3.place(x=80,y=285)
    d4 = tk.Label(WINDOW, font=(None, 10),text='TOTAL DEATHS           :   '+ str(int(country_detail.loc[str(country)]['Deaths'])))
    d4.place(x=80,y=315)
    d5 = tk.Label(WINDOW, font=(None, 10),text='MORTALITY RATE(%)  :    '+ str(country_detail.loc[str(country)]['Mortality_Rate']))
    d5.place(x=80,y=345)
    d6 = tk.Label(WINDOW, font=(None, 10),text='ACTIVE CASES          :    '+ str(int(country_detail.loc[str(country)]['Active'])))
    d6.place(x=80,y=375)
    d7 = tk.Label(WINDOW, font=(None, 10),text='COUNTRY CODE         :    '+ str(country_detail.loc[str(country)]['ISO3']))
    d7.place(x=80,y=405)
    
entry = tk.Entry(WINDOW, borderwidth=5)
entry.place(x=25,y=200,height=25,width=300)

def clear():
   global sym_img,head_mort,head_death,head_conf,head_act,head_recover
   sym_img.destroy()
   try:
      global mort1,mort2,mort3,mort4,mort5,mort6,mort7,mort8,mort9,mort10,mort11,mort12,mort13,mort14
      mort_lst = [head_mort,mort1,mort2,mort3,mort4,mort5,mort6,mort7,mort8,mort9,mort10,mort11,mort12,mort13,mort14]
      for i in mort_lst:
         i.destroy()
   except:
      pass
   try:
      global death1,death2,death3,death4,death5,death6,death7,death8,death9,death10,death11,death12,death13,death14
      death_lst = [head_death,death1,death2,death3,death4,death5,death6,death7,death8,death9,death10,death11,death12,death13,death14]
      for i in death_lst:
         i.destroy()
   except:
      pass
   try:
      global conf1,conf2,conf3,conf4,conf5,conf6,conf7,conf8,conf9,conf10,conf11,conf12,conf13,conf14
      conf_lst = [head_conf,conf1,conf2,conf3,conf4,conf5,conf6,conf7,conf8,conf9,conf10,conf11,conf12,conf13,conf14]
      for i in conf_lst:
         i.destroy()  
   except:
      pass
   try:
      global act1,act2,act3,act4,act5,act6,act7,act8,act9,act10,act11,act12,act13,act14
      act_lst = [head_act,act1,act2,act3,act4,act5,act6,act7,act8,act9,act10,act11,act12,act13,act14]
      for i in act_lst:
         i.destroy()  
   except:
      pass
   try:
      global recover1,recover2,recover3,recover4,recover5,recover6,recover7,recover8,recover9,recover10,recover11,recover12,recover13,recover14
      recover_lst = [head_recover,recover1,recover2,recover3,recover4,recover5,recover6,recover7,recover8,recover9,recover10,recover11,recover12,recover13,recover14]
      for i in recover_lst:
         i.destroy()
   except:
      pass
def symptoms():
   global sym_img
   clear()
   sym_img = tk.Label(WINDOW,image=sym)
   sym_img.place(x=390,y=325)
   
def mortality():
   global head_mort,mort1,mort2,mort3,mort4,mort5,mort6,mort7,mort8,mort9,mort10,mort11,mort12,mort13,mort14
   clear()
   head_mort = tk.Label(WINDOW, font=(None , 12),text="COUNTRY                             MORTALITY RATE")
   head_mort.place(x=430,y=335)
   mort1 = tk.Label(WINDOW, font=(None , 12),text=str(mortality_data.iloc[0]["Country_Region"]))
   mort2 = tk.Label(WINDOW, font=(None , 12),text=str(mortality_data.iloc[1]["Country_Region"]))
   mort3 = tk.Label(WINDOW, font=(None , 12),text=str(mortality_data.iloc[2]["Country_Region"]))
   mort4 = tk.Label(WINDOW, font=(None , 12),text=str(mortality_data.iloc[3]["Country_Region"]))
   mort5 = tk.Label(WINDOW, font=(None , 12),text=str(mortality_data.iloc[4]["Country_Region"]))
   mort6 = tk.Label(WINDOW, font=(None , 12),text=str(mortality_data.iloc[5]["Country_Region"]))
   mort7 = tk.Label(WINDOW, font=(None , 12),text=str(mortality_data.iloc[6]["Country_Region"]))
   mort8 = tk.Label(WINDOW, font=(None , 12),text=str(mortality_data.iloc[0]['Mortality_Rate'])+"%")
   mort9 = tk.Label(WINDOW, font=(None , 12),text=str(mortality_data.iloc[1]['Mortality_Rate'])+"%")
   mort10 = tk.Label(WINDOW, font=(None , 12),text=str(mortality_data.iloc[2]['Mortality_Rate'])+"%")
   mort11 = tk.Label(WINDOW, font=(None , 12),text=str(mortality_data.iloc[3]['Mortality_Rate'])+"%")
   mort12 = tk.Label(WINDOW, font=(None , 12),text=str(mortality_data.iloc[4]['Mortality_Rate'])+"%")
   mort13 = tk.Label(WINDOW, font=(None , 12),text=str(mortality_data.iloc[5]['Mortality_Rate'])+"%")
   mort14 = tk.Label(WINDOW, font=(None , 12),text=str(mortality_data.iloc[6]['Mortality_Rate'])+"%")
   mort_lst = [mort1,mort2,mort3,mort4,mort5,mort6,mort7]
   mort_lsts = [mort8,mort9,mort10,mort11,mort12,mort13,mort14]
   y_s = 365
   for i in mort_lst:
      i.place(x=420,y=y_s)
      y_s = y_s + 30
   y_s = 365   
   for i in mort_lsts:
      i.place(x=615,y=y_s)
      y_s = y_s + 30       
def death():
   global head_death,death1,death2,death3,death4,death5,death6,death7,death8,death9,death10,death11,death12,death13,death14
   clear()
   head_death = tk.Label(WINDOW, font=(None , 12),text="COUNTRY                          TOTAL DEATHS CASES")
   head_death.place(x=430,y=335)
   death1 = tk.Label(WINDOW, font=(None , 12),text=str(death_data.iloc[0]["Country_Region"]))
   death2 = tk.Label(WINDOW, font=(None , 12),text=str(death_data.iloc[1]["Country_Region"]))
   death3 = tk.Label(WINDOW, font=(None , 12),text=str(death_data.iloc[2]["Country_Region"]))
   death4 = tk.Label(WINDOW, font=(None , 12),text=str(death_data.iloc[3]["Country_Region"]))
   death5 = tk.Label(WINDOW, font=(None , 12),text=str(death_data.iloc[4]["Country_Region"]))
   death6 = tk.Label(WINDOW, font=(None , 12),text=str(death_data.iloc[5]["Country_Region"]))
   death7 = tk.Label(WINDOW, font=(None , 12),text=str(death_data.iloc[6]["Country_Region"]))
   death8 = tk.Label(WINDOW, font=(None , 12),text=str(int(death_data.iloc[0]['Deaths'])))
   death9 = tk.Label(WINDOW, font=(None , 12),text=str(int(death_data.iloc[1]['Deaths'])))
   death10 = tk.Label(WINDOW, font=(None , 12),text=str(int(death_data.iloc[2]['Deaths'])))                  
   death11 = tk.Label(WINDOW, font=(None , 12),text=str(int(death_data.iloc[3]['Deaths'])))
   death12 = tk.Label(WINDOW, font=(None , 12),text=str(int(death_data.iloc[4]['Deaths'])))
   death13 = tk.Label(WINDOW, font=(None , 12),text=str(int(death_data.iloc[5]['Deaths'])))
   death14 = tk.Label(WINDOW, font=(None , 12),text=str(int(death_data.iloc[6]['Deaths'])))
   death_lst = [death1,death2,death3,death4,death5,death6,death7]
   death_lsts = [death8,death9,death10,death11,death12,death13,death14]
   y_s = 365
   for i in death_lst:
      i.place(x=420,y=y_s)
      y_s = y_s + 30
   y_s = 365   
   for i in death_lsts:
      i.place(x=650,y=y_s)
      y_s = y_s + 30       
def confirmed():
   global head_conf,conf1,conf2,conf3,conf4,conf5,conf6,conf7,conf8,conf9,conf10,conf11,conf12,conf13,conf14
   clear()
   head_conf = tk.Label(WINDOW, font=(None , 12),text="COUNTRY                   TOTAL CONFIRMED CASES")
   head_conf.place(x=430,y=335)
   conf1 = tk.Label(WINDOW, font=(None , 12),text=str(confirmed_data.iloc[0]["Country_Region"]))
   conf2 = tk.Label(WINDOW, font=(None , 12),text=str(confirmed_data.iloc[1]["Country_Region"]))
   conf3 = tk.Label(WINDOW, font=(None , 12),text=str(confirmed_data.iloc[2]["Country_Region"]))
   conf4 = tk.Label(WINDOW, font=(None , 12),text=str(confirmed_data.iloc[3]["Country_Region"]))
   conf5 = tk.Label(WINDOW, font=(None , 12),text=str(confirmed_data.iloc[4]["Country_Region"]))
   conf6 = tk.Label(WINDOW, font=(None , 12),text=str(confirmed_data.iloc[5]["Country_Region"]))
   conf7 = tk.Label(WINDOW, font=(None , 12),text=str(confirmed_data.iloc[6]["Country_Region"]))
   conf8 = tk.Label(WINDOW, font=(None , 12),text=str(int(confirmed_data.iloc[0]['Confirmed'])))
   conf9 = tk.Label(WINDOW, font=(None , 12),text=str(int(confirmed_data.iloc[1]['Confirmed'])))                 
   conf10 = tk.Label(WINDOW, font=(None , 12),text=str(int(confirmed_data.iloc[2]['Confirmed'])))
   conf11 = tk.Label(WINDOW, font=(None , 12),text=str(int(confirmed_data.iloc[3]['Confirmed'])))
   conf12 = tk.Label(WINDOW, font=(None , 12),text=str(int(confirmed_data.iloc[4]['Confirmed'])))                  
   conf13 = tk.Label(WINDOW, font=(None , 12),text=str(int(confirmed_data.iloc[5]['Confirmed']))) 
   conf14 = tk.Label(WINDOW, font=(None , 12),text=str(int(confirmed_data.iloc[6]['Confirmed'])))
   y_s = 365
   conf_lst = [conf1,conf2,conf3,conf4,conf5,conf6,conf7]
   conf_lsts = [conf8,conf9,conf10,conf11,conf12,conf13,conf14]
   for i in conf_lst:
      i.place(x=420,y=y_s)
      y_s = y_s + 30
   y_s = 365   
   for i in conf_lsts:
      i.place(x=650,y=y_s)
      y_s = y_s + 30    
def recovered():
   global head_recover,recover1,recover2,recover3,recover4,recover5,recover6,recover7,recover8,recover9,recover10,recover11,recover12,recover13,recover14
   clear()
   head_recover = tk.Label(WINDOW, font=(None , 12),text="COUNTRY                   TOTAL RECOVERED CASES")
   head_recover.place(x=430,y=335)
   recover1 = tk.Label(WINDOW, font=(None , 12),text=str(recovered_data.iloc[0]["Country_Region"]))
   recover2 = tk.Label(WINDOW, font=(None , 12),text=str(recovered_data.iloc[1]["Country_Region"]))
   recover3 = tk.Label(WINDOW, font=(None , 12),text=str(recovered_data.iloc[2]["Country_Region"]))
   recover4 = tk.Label(WINDOW, font=(None , 12),text=str(recovered_data.iloc[3]["Country_Region"]))
   recover5 = tk.Label(WINDOW, font=(None , 12),text=str(recovered_data.iloc[4]["Country_Region"]))
   recover6 = tk.Label(WINDOW, font=(None , 12),text=str(recovered_data.iloc[5]["Country_Region"]))
   recover7 = tk.Label(WINDOW, font=(None , 12),text=str(recovered_data.iloc[6]["Country_Region"]))
   recover8 = tk.Label(WINDOW, font=(None , 12),text=str(int(recovered_data.iloc[0]["Recovered"])))
   recover9 = tk.Label(WINDOW, font=(None , 12),text=str(int(recovered_data.iloc[1]["Recovered"])))
   recover10 = tk.Label(WINDOW, font=(None , 12),text=str(int(recovered_data.iloc[2]["Recovered"])))
   recover11 = tk.Label(WINDOW, font=(None , 12),text=str(int(recovered_data.iloc[3]["Recovered"])))
   recover12 = tk.Label(WINDOW, font=(None , 12),text=str(int(recovered_data.iloc[4]["Recovered"])))
   recover13 = tk.Label(WINDOW, font=(None , 12),text=str(int(recovered_data.iloc[5]["Recovered"])))
   recover14 = tk.Label(WINDOW, font=(None , 12),text=str(int(recovered_data.iloc[6]["Recovered"])))
   recover_lst = [recover1,recover2,recover3,recover4,recover5,recover6,recover7]
   recover_lsts = [recover8,recover9,recover10,recover11,recover12,recover13,recover14]
   y_s = 365
   for i in recover_lst:
      i.place(x=420,y=y_s)
      y_s = y_s + 30
   y_s = 365   
   for i in recover_lsts:
      i.place(x=650,y=y_s)
      y_s = y_s + 30   
def active():
   global head_act,act1,act2,act3,act4,act5,act6,act7,act8,act9,act10,act11,act12,act13,act14 
   clear()
   head_act = tk.Label(WINDOW, font=(None , 12),text="COUNTRY                        TOTAL ACTIVE CASES")
   head_act.place(x=430,y=335)
   act1 = tk.Label(WINDOW, font=(None , 12),text=str(active_data.iloc[0]["Country_Region"]))
   act2 = tk.Label(WINDOW, font=(None , 12),text=str(active_data.iloc[1]["Country_Region"]))
   act3 = tk.Label(WINDOW, font=(None , 12),text=str(active_data.iloc[2]["Country_Region"]))
   act4 = tk.Label(WINDOW, font=(None , 12),text=str(active_data.iloc[3]["Country_Region"]))
   act5 = tk.Label(WINDOW, font=(None , 12),text=str(active_data.iloc[4]["Country_Region"]))
   act6 = tk.Label(WINDOW, font=(None , 12),text=str(active_data.iloc[5]["Country_Region"]))
   act7 = tk.Label(WINDOW, font=(None , 12),text=str(active_data.iloc[6]["Country_Region"]))
   act8 = tk.Label(WINDOW, font=(None , 12),text=str(int(active_data.iloc[0]["Active"])))
   act9 = tk.Label(WINDOW, font=(None , 12),text=str(int(active_data.iloc[1]["Active"])))
   act10 = tk.Label(WINDOW, font=(None , 12),text=str(int(active_data.iloc[2]["Active"])))
   act11 = tk.Label(WINDOW, font=(None , 12),text=str(int(active_data.iloc[3]["Active"])))
   act12 = tk.Label(WINDOW, font=(None , 12),text=str(int(active_data.iloc[4]["Active"])))
   act13 = tk.Label(WINDOW, font=(None , 12),text=str(int(active_data.iloc[5]["Active"])))
   act14 = tk.Label(WINDOW, font=(None , 12),text=str(int(active_data.iloc[6]["Active"])))
   act_lst = [act1,act2,act3,act4,act5,act6,act7]
   act_lsts = [act8,act9,act10,act11,act12,act13,act14]
   y_s = 365
   for i in act_lst:
      i.place(x=420,y=y_s)
      y_s = y_s + 30
   y_s = 365   
   for i in act_lsts:
      i.place(x=650,y=y_s)
      y_s = y_s + 30
def SEARCH(country):
    try:
       try:
          global not_f
          not_f.destroy()
       except:
          pass
       searched_lst = [d1,d2,d3,d4,d5,d6,d7]
       for i in searched_lst:
          i.destroy()
    except:
      pass  
    if country == "":
        country = entry.get().lower()
    if country == 'america':
       country = 'us'      
    uk = ['england','scotland','wales','northern ireland']
    if country in uk:
       country = 'united kingdom'

    if country in countrys:
       country_corona_detail(country)      

    if country not in countrys:
        not_f = tk.Label(WINDOW, text='* NO COUNTRY MATCHES ! TRY AGAIN', fg='red')
        not_f.place(x=55,y=225)

confirm_case = tk.Label(WINDOW,fg='red',font=(None, 15),text=' CONFIRMED CASES '+str(covid_data[0].text)).place(x=40,y=5)
recover_case = tk.Label(WINDOW,fg='red',font=(None, 15),text=' RECOVERED CASES '+str(covid_data[2].text)).place(x=40,y=63)
death_case = tk.Label(WINDOW,fg='red',font=(None, 15),text='     TOTAL DEATH      '   +str(covid_data[1].text)).place(x=40,y=120)

tk.Button(WINDOW, borderwidth=5, bg = 'black', fg='white',text='search', command=lambda:SEARCH("")).place(x=325,y=200, height=25)
tk.Button(WINDOW, borderwidth=5, bg = 'black', fg='red',text='TOP MORTALITY RATE', command=lambda:mortality()).place(x=30,y=545, height=30)
tk.Button(WINDOW, borderwidth=5, bg = 'black', fg='red',text='TOP DEATH', command=lambda:death()).place(x=180,y=545, height=30)
tk.Button(WINDOW, borderwidth=5, bg = 'black', fg='red',text='TOP CONFIRMED', command=lambda:confirmed()).place(x=30,y=500, height=30)
tk.Button(WINDOW, borderwidth=5, bg = 'black', fg='red',text='TOP RECOVERED', command=lambda:recovered()).place(x=150,y=500, height=30)
tk.Button(WINDOW, borderwidth=5, bg = 'black', fg='red',text='TOP ACTIVE', command=lambda:active()).place(x=30,y=460, height=30)
tk.Button(WINDOW, borderwidth=5, bg = 'black', fg='red',text='CORONA SYMPTOMS', command=lambda:symptoms()).place(x=120,y=460, height=30)

WINDOW.mainloop()

########################### STAY HOME & STAY SAFE ##############################
