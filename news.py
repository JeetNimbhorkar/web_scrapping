import requests
from bs4 import BeautifulSoup
from newspaper import Article
import nltk
nltk.download('punkt')

url="http://news.google.com"
r_main=requests.get(url)
soup_main=BeautifulSoup(r_main.text,'lxml')

all=[]
i=0

class main_page:
    
    def latest_clicked(self):
        global all
        all=soup_main.find_all('h3')
        print_heading_summary()
        
    def india_latest_clicked(self):
        global all
        r=requests.get(url+soup_main.find("div",{"jsname":"V2bVMb"}).find_all('a')[1]['href'][1:])
        soup=BeautifulSoup(r.text,'lxml')
        all=soup.find_all('h3')
        print_heading_summary()
        
    def world_latest_clicked(self):
        global all
        r=requests.get(url+soup_main.find("div",{"jsname":"V2bVMb"}).find_all('a')[2]['href'][1:])
        soup=BeautifulSoup(r.text,'lxml')
        all=soup.find_all('h3')
        print_heading_summary()

class buisness_page:
    
    buisness_url=url+soup_main.find("div",{"jsname":"V2bVMb"}).find_all('a')[4]['href'][1:]
    r=requests.get(buisness_url)
    soup=BeautifulSoup(r.text,'lxml')
        
    def buisness_latest_clicked(self):
        global all
        all=self.soup.find_all('h3')
        print_heading_summary()
        
    def economy_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[1]['aria-controls'][3:]
        r1=requests.get(self.buisness_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def markets_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[2]['aria-controls'][3:]
        r1=requests.get(self.buisness_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def jobs_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[3]['aria-controls'][3:]
        r1=requests.get(self.buisness_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def finance_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[4]['aria-controls'][3:]
        r1=requests.get(self.buisness_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def entrepreneurship_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[5]['aria-controls'][3:]
        r1=requests.get(self.buisness_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()

class tech_page:
    
    tech_url=url+soup_main.find("div",{"jsname":"V2bVMb"}).find_all('a')[5]['href'][1:]
    r=requests.get(tech_url)
    soup=BeautifulSoup(r.text,'lxml')
    
    def tech_latest_clicked(self):
        global all
        all=self.soup.find_all('h3')
        print_heading_summary()
        
    def mobile_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[1]['aria-controls'][3:]
        r1=requests.get(self.tech_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
              
    def gadgets_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[2]['aria-controls'][3:]
        r1=requests.get(self.tech_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def internet_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[3]['aria-controls'][3:]
        r1=requests.get(self.tech_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def vr_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[4]['aria-controls'][3:]
        r1=requests.get(self.tech_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def ai_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[5]['aria-controls'][3:]
        r1=requests.get(self.tech_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def comp_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[6]['aria-controls'][3:]
        r1=requests.get(self.tech_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()

class entertainment_page:
    
    entertain_url=url+soup_main.find("div",{"jsname":"V2bVMb"}).find_all('a')[6]['href'][1:]
    r=requests.get(entertain_url)
    soup=BeautifulSoup(r.text,'lxml')
    
    def entertainment_latest_clicked(self):
        global all
        all=self.soup.find_all('h3')
        print_heading_summary()
        
    def movies_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[1]['aria-controls'][3:]
        r1=requests.get(self.entertain_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()

    def music_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[2]['aria-controls'][3:]
        r1=requests.get(self.entertain_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def tv_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[3]['aria-controls'][3:]
        r1=requests.get(self.entertain_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def books_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[4]['aria-controls'][3:]
        r1=requests.get(self.entertain_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def art_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[5]['aria-controls'][3:]
        r1=requests.get(self.entertain_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def celeb_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[6]['aria-controls'][3:]
        r1=requests.get(self.entertain_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()

class sports_page:
    
    sports_url=url+soup_main.find("div",{"jsname":"V2bVMb"}).find_all('a')[7]['href'][1:]
    r=requests.get(sports_url)
    soup=BeautifulSoup(r.text,'lxml')
        
    def sports_latest_clicked(self):
        global all
        all=self.soup.find_all('h3')
        
    def cricket_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[1]['aria-controls'][3:]
        r1=requests.get(self.sports_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def hockey_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[2]['aria-controls'][3:]
        r1=requests.get(self.sports_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def tennis_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[3]['aria-controls'][3:]
        r1=requests.get(self.sports_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def football_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[4]['aria-controls'][3:]
        r1=requests.get(self.sports_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def badminton_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[5]['aria-controls'][3:]
        r1=requests.get(self.sports_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def kabaddi_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[6]['aria-controls'][3:]
        r1=requests.get(self.sports_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def wc_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[7]['aria-controls'][3:]
        r1=requests.get(self.sports_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def basketball_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[8]['aria-controls'][3:]
        r1=requests.get(self.sports_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def f1_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[9]['aria-controls'][3:]
        r1=requests.get(self.sports_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()

class science_page:
    
    sci_url=url+soup_main.find("div",{"jsname":"V2bVMb"}).find_all('a')[8]['href'][1:]
    r=requests.get(sci_url)
    soup=BeautifulSoup(r.text,'lxml')
        
    def science_latest_clicked(self):
        global all
        all=self.soup.find_all('h3')
        print_heading_summary()
    
    def environment_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[1]['aria-controls'][3:]
        r1=requests.get(self.sci_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def outerspace_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[2]['aria-controls'][3:]
        r1=requests.get(self.sci_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def physics_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[3]['aria-controls'][3:]
        r1=requests.get(self.sci_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def genetics_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[4]['aria-controls'][3:]
        r1=requests.get(self.sci_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def wildlife_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[5]['aria-controls'][3:]
        r1=requests.get(self.sci_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()

class health_page:
    
    health_url=url+soup_main.find("div",{"jsname":"V2bVMb"}).find_all('a')[9]['href'][1:]
    r=requests.get(health_url)
    soup=BeautifulSoup(r.text,'lxml')
    
    def health_latest_clicked(self):
        global all
        all=self.soup.find_all('h3')
        print_heading_summary()
        
    def medicine_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[1]['aria-controls'][3:]
        r1=requests.get(self.health_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def healthcare_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[2]['aria-controls'][3:]
        r1=requests.get(self.health_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def mentalhealth_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[3]['aria-controls'][3:]
        r1=requests.get(self.health_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def nutrition_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[4]['aria-controls'][3:]
        r1=requests.get(self.health_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()
        
    def fitness_clicked(self):
        global all
        sub_url=self.soup.find_all('div',{'jsname':'AznF2e'})[5]['aria-controls'][3:]
        r1=requests.get(self.health_url[:-28]+'/sections/'+sub_url)
        soup1=BeautifulSoup(r1.text,'lxml')
        all=soup1.find_all('h3')
        print_heading_summary()

m=main_page()
b=buisness_page()
t=tech_page()
sc=science_page()
sp=sports_page()
e=entertainment_page()
h=health_page()

def print_heading_summary():
    global i
    i=0
    while True:
        try:
            article =Article("https://news.google.com"+ all[i].find("a")['href'][1:],language='en')
            article.download()
            article.parse()
            article.nlp()
        except:
            i=i+1
            continue
        break
    text.configure(state=NORMAL)
    text.delete(1.0,END)
    text.insert(INSERT,article.title+'\n\n\n')
    position=text.index(INSERT)
    text.tag_add("heading",'1.0',END)
    text.tag_config('heading',font=('verdana','13','bold'))
    text.insert(INSERT,article.summary)
    text.tag_add("summary",position,END)
    text.tag_config('summary',font=('tisa','12'))
    text.configure(state=DISABLED)

def next_news():
    global i
    if i<len(all)-1:
        i=i+1
        while True:
            try:
                article =Article("https://news.google.com"+ all[i].find("a")['href'][1:],language='en')
                article.download()
                article.parse()
                article.nlp()
            except:
                i=i+1
                continue
            break
        text.configure(state=NORMAL)
        text.delete(1.0,END)
        text.insert(INSERT,article.title+'\n\n\n')
        position=text.index(INSERT)
        text.tag_add("heading",'1.0',END)
        text.tag_config('heading',font=('verdana','13','bold'))
        text.insert(INSERT,article.summary)
        text.tag_add("summary",position,END)
        text.tag_config('summary',font=('tisa','12'))
        text.configure(state=DISABLED)

def previous_news():
    global i
    if i>0:
        i=i-1
        while True:
            try:
                article =Article("https://news.google.com"+ all[i].find("a")['href'][1:],language='en')
                article.download()
                article.parse()
                article.nlp()
            except:
                i=i-1
                continue
            break
        text.configure(state=NORMAL)
        text.delete(1.0,END)
        text.insert(INSERT,article.title+'\n\n\n')
        position=text.index(INSERT)
        text.tag_add("heading",'1.0',END)
        text.tag_config('heading',font=('verdana','13','bold'))
        text.insert(INSERT,article.summary)
        text.tag_add("summary",position,END)
        text.tag_config('summary',font=('tisa','12'))
        text.configure(state=DISABLED)

def search():
    global all
    key=entry.get()
    if key != '':
        r=requests.get(url+'/search?q='+key)
        soup=BeautifulSoup(r.text,'lxml')
        all=soup.find_all('h3')
        if len(all)==0:
            text.configure(state=NORMAL)
            text.delete(1.0,END)
            text.insert(INSERT,"No results found.")
            text.configure(state=DISABLED)
        else:
            print_heading_summary()

from tkinter import *

def buisness_news():
    fmain.grid_remove()
    fbuisness.grid(row=2,column=0,padx=20,pady=20)
    fdown.grid(row=3)

def tech_news():
    fmain.grid_remove()
    ftech.grid(row=2,column=0,padx=20,pady=20)
    fdown.grid(row=3)

def entertainment_news():
    fmain.grid_remove()
    fentertain.grid(row=2,column=0,padx=20,pady=20)
    fdown.grid(row=3)

def sports_news():
    fmain.grid_remove()
    fsports.grid(row=2,column=0,padx=20,pady=20)
    fdown.grid(row=3)

def science_news():
    fmain.grid_remove()
    fscience.grid(row=2,column=0,padx=20,pady=20)
    fdown.grid(row=3)

def health_news():
    fmain.grid_remove()
    fhealth.grid(row=2,column=0,padx=20,pady=20)
    fdown.grid(row=3)

def go_back():
    if fbuisness.winfo_ismapped():
        fbuisness.grid_remove()
    elif ftech.winfo_ismapped():
        ftech.grid_remove()
    elif fentertain.winfo_ismapped():
        fentertain.grid_remove()
    elif fsports.winfo_ismapped():
        fsports.grid_remove()
    elif fscience.winfo_ismapped():
        fscience.grid_remove()
    elif fhealth.winfo_ismapped():
        fhealth.grid_remove()
    fmain.grid(row=2,column=0)
    fdown.grid_remove()

window=Tk()
window.title('News')

fmain=Frame(window)
latest=Button(fmain,text='Latest',command=m.latest_clicked,width=15,font=('verdana','10'),bd=7)
latest.grid(row=0,column=0,pady=5)
india=Button(fmain,text='India',command=m.india_latest_clicked,width=15,font=('verdana','10'),bd=7)
india.grid(row=1,column=0,pady=5)
world=Button(fmain,text='World',command=m.world_latest_clicked,width=15,font=('verdana','10'),bd=7)
world.grid(row=2,column=0,pady=5)
buisness=Button(fmain,text='Buisness',command=buisness_news,width=15,font=('verdana','10'),bd=7)
buisness.grid(row=4,column=0,pady=5)
tech=Button(fmain,text='Technology',command=tech_news,width=15,font=('verdana','10'),bd=7)
tech.grid(row=5,column=0,pady=5)
entertain=Button(fmain,text='Entertainment',command=entertainment_news,width=15,font=('verdana','10'),bd=7)
entertain.grid(row=6,column=0,pady=5)
sports=Button(fmain,text='Sports',command=sports_news,width=15,font=('verdana','10'),bd=7)
sports.grid(row=7,column=0,pady=5)
sci=Button(fmain,text='Science',command=science_news,width=15,font=('verdana','10'),bd=7)
sci.grid(row=8,column=0,pady=5)
health=Button(fmain,text='Health',command=health_news,width=15,font=('verdana','10'),bd=7)
health.grid(row=9,column=0,pady=5)
fmain.grid(row=2,column=0,padx=20,pady=20)

fsearch=Frame(window)
label=Label(fsearch,text="Search using key word ",height=5,font=('Serif','15'),bd=7)
label.grid(row=0,column=0,padx=5)
entry=Entry(fsearch,width=25)
entry.grid(row=0,column=1,padx=5,ipady=5)
search=Button(fsearch,text='Search',command=search,height=2,width=10,font=('verdana','10'),bd=7)
search.grid(row=0,column=2,padx=5)
fsearch.grid(row=1,column=2)

fdisplay=Frame(window)
scroll = Scrollbar(fdisplay,orient="vertical")
scroll.grid(row=0,column=2,sticky='ns')
text=Text(fdisplay,wrap=WORD,padx=10,pady=10,bd=7,state=DISABLED,yscrollcommand=scroll.set)
scroll.config(command=text.yview)
text.grid(row=0,column=1)
previous=Button(fdisplay,text='<<',command=previous_news,font=('Serif','20'),bd=7)
previous.grid(row=0,column=0)
front=Button(fdisplay,text='>>',command=next_news,font=('Serif','20'),bd=7)
front.grid(row=0,column=3)
fdisplay.grid(row=2,column=2,padx=20,pady=(0,25))

fdown=Frame(window)
back=Button(fdown,text='<<Back',command=go_back,height=3,width=10,font=('verdana','10'),bd=7)
back.pack(side=LEFT,pady=15)

fbuisness=Frame(window)
l1=Button(fbuisness,text='Latest',command=b.buisness_latest_clicked,width=15,font=('verdana','10'),bd=7)
l1.grid(row=0,column=0,pady=5)
economy=Button(fbuisness,text='Economy',command=b.economy_clicked,width=15,font=('verdana','10'),bd=7)
economy.grid(row=1,column=0,pady=5)
markets=Button(fbuisness,text='Markets',command=b.markets_clicked,width=15,font=('verdana','10'),bd=7)
markets.grid(row=2,column=0,pady=5)
jobs=Button(fbuisness,text='Jobs',command=b.jobs_clicked,width=15,font=('verdana','10'),bd=7)
jobs.grid(row=3,column=0,pady=5)
finance=Button(fbuisness,text='Personal Finance',command=b.finance_clicked,width=15,font=('verdana','10'),bd=7)
finance.grid(row=4,column=0,pady=5)
enterpreneurship=Button(fbuisness,text='Enterpreneurship',command=b.entrepreneurship_clicked,width=15,font=('verdana','10'),bd=7)
enterpreneurship.grid(row=5,column=0,pady=5)

ftech=Frame(window)
l2=Button(ftech,text='Latest',command=t.tech_latest_clicked,width=15,font=('verdana','10'),bd=7)
l2.grid(row=0,column=0,pady=5)
mobile=Button(ftech,text='Mobile',command=t.mobile_clicked,width=15,font=('verdana','10'),bd=7)
mobile.grid(row=1,column=0,pady=5)
gadgets=Button(ftech,text='Gadgets',command=t.gadgets_clicked,width=15,font=('verdana','10'),bd=7)
gadgets.grid(row=2,column=0,pady=5)
internet=Button(ftech,text='Internet',command=t.internet_clicked,width=15,font=('verdana','10'),bd=7)
internet.grid(row=3,column=0,pady=5)
vr=Button(ftech,text='Virtual Reality',command=t.vr_clicked,width=15,font=('verdana','10'),bd=7)
vr.grid(row=4,column=0,pady=5)
ai=Button(ftech,text='Artificial Intelligence',command=t.ai_clicked,width=15,font=('verdana','9'),bd=7)
ai.grid(row=5,column=0,pady=5)
comp=Button(ftech,text='Computing',command=t.comp_clicked,width=15,font=('verdana','10'),bd=7)
comp.grid(row=6,column=0,pady=5)

fentertain=Frame(window)
l3=Button(fentertain,text='Latest',command=e.entertainment_latest_clicked,width=15,font=('verdana','10'),bd=7)
l3.grid(row=0,column=0,pady=5)
movies=Button(fentertain,text='Movies',command=e.movies_clicked,width=15,font=('verdana','10'),bd=7)
movies.grid(row=1,column=0,pady=5)
music=Button(fentertain,text='Music',command=e.music_clicked,width=15,font=('verdana','10'),bd=7)
music.grid(row=2,column=0,pady=5)
tv=Button(fentertain,text='TV',command=e.tv_clicked,width=15,font=('verdana','10'),bd=7)
tv.grid(row=3,column=0,pady=5)
books=Button(fentertain,text='Books',command=e.books_clicked,width=15,font=('verdana','10'),bd=7)
books.grid(row=4,column=0,pady=5)
art=Button(fentertain,text='Art',command=e.art_clicked,width=15,font=('verdana','10'),bd=7)
art.grid(row=5,column=0,pady=5)
celeb=Button(fentertain,text='Celebrities',command=e.celeb_clicked,width=15,font=('verdana','10'),bd=7)
celeb.grid(row=6,column=0,pady=5)

fsports=Frame(window)
l4=Button(fsports,text='Latest',command=sp.sports_latest_clicked,width=15,font=('verdana','10'),bd=7)
l4.grid(row=0,column=0,pady=5)
cricket=Button(fsports,text='Cricket',command=sp.cricket_clicked,width=15,font=('verdana','10'),bd=7)
cricket.grid(row=1,column=0,pady=5)
hockey=Button(fsports,text='Hockey',command=sp.hockey_clicked,width=15,font=('verdana','10'),bd=7)
hockey.grid(row=2,column=0,pady=5)
tennis=Button(fsports,text='Tennis',command=sp.tennis_clicked,width=15,font=('verdana','10'),bd=7)
tennis.grid(row=3,column=0,pady=5)
football=Button(fsports,text='Football',command=sp.football_clicked,width=15,font=('verdana','10'),bd=7)
football.grid(row=4,column=0,pady=5)
badminton=Button(fsports,text='Badminton',command=sp.badminton_clicked,width=15,font=('verdana','10'),bd=7)
badminton.grid(row=5,column=0,pady=5)
kabaddi=Button(fsports,text='Kabaddi',command=sp.kabaddi_clicked,width=15,font=('verdana','10'),bd=7)
kabaddi.grid(row=6,column=0,pady=5)
wc=Button(fsports,text="Women's Cricket",command=sp.wc_clicked,width=15,font=('verdana','10'),bd=7)
wc.grid(row=7,column=0,pady=5)
basketball=Button(fsports,text='Basketball',command=sp.basketball_clicked,width=15,font=('verdana','10'),bd=7)
basketball.grid(row=8,column=0,pady=5)
f1=Button(fsports,text='F1 Racing',command=sp.f1_clicked,width=15,font=('verdana','10'),bd=7)
f1.grid(row=9,column=0,pady=5)

fscience=Frame(window)
l5=Button(fscience,text='Latest',command=sc.science_latest_clicked,width=15,font=('verdana','10'),bd=7)
l5.grid(row=0,column=0,pady=5)
envi=Button(fscience,text='Environment',command=sc.environment_clicked,width=15,font=('verdana','10'),bd=7)
envi.grid(row=1,column=0,pady=5)
space=Button(fscience,text='Outer Space',command=sc.outerspace_clicked,width=15,font=('verdana','10'),bd=7)
space.grid(row=2,column=0,pady=5)
physics=Button(fscience,text='Physics',command=sc.physics_clicked,width=15,font=('verdana','10'),bd=7)
physics.grid(row=3,column=0,pady=5)
genetics=Button(fscience,text='Genetics',command=sc.genetics_clicked,width=15,font=('verdana','10'),bd=7)
genetics.grid(row=4,column=0,pady=5)
wildcraft=Button(fscience,text='Wildcraft',command=sc.wildlife_clicked,width=15,font=('verdana','10'),bd=7)
wildcraft.grid(row=5,column=0,pady=5)

fhealth=Frame(window)
l6=Button(fhealth,text='Latest',command=h.health_latest_clicked,width=15,font=('verdana','10'),bd=7)
l6.grid(row=0,column=0,pady=5)
medicine=Button(fhealth,text='Medicine',command=h.medicine_clicked,width=15,font=('verdana','10'),bd=7)
medicine.grid(row=1,column=0,pady=5)
healthcare=Button(fhealth,text='Health Care',command=h.healthcare_clicked,width=15,font=('verdana','10'),bd=7)
healthcare.grid(row=2,column=0,pady=5)
mental=Button(fhealth,text='Mental Health',command=h.mentalhealth_clicked,width=15,font=('verdana','10'),bd=7)
mental.grid(row=3,column=0,pady=5)
nutrition=Button(fhealth,text='Nutrition',command=h.nutrition_clicked,width=15,font=('verdana','10'),bd=7)
nutrition.grid(row=4,column=0,pady=5)
fitness=Button(fhealth,text='Fitness',command=h.fitness_clicked,width=15,font=('verdana','10'),bd=7)
fitness.grid(row=5,column=0,pady=5)

window.resizable(0,0)
window.mainloop()