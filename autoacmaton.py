import requests
import html
import http
import bs4

ofile=open("res.txt","w")

bs=bs4.BeautifulSoup
def getOnePage(page=1):
    urlMenu="https://wzoi.cc/s/1?page="+str(page)
    get_menu=requests.get(urlMenu)

    menures=bs(get_menu.content.decode("utf-8"),"html.parser")

    urls=[]

    for item in menures.tbody.find_all("td",class_="text-left"):
        urls.append(str(item.contents[0].get("href")))


    def getsol(url):
        solurl="https://wzoi.cc"+url
        ofile.write(solurl+"\n")
        print(solurl)
        #get_sol=requests.get(solurl)
        #solres=bs(get_sol.content.decode("utf-8"),"html.parser")
        #print(solres)


    def solveurl(url):
        _,p_set,p_id=url[1:].split("/")
        solsurl='https://wzoi.cc/solutions?problemset_id='+p_set+'&user_name=&problem_id='+p_id+'&score_min=100&score_max=&language=&status='
        #print(solurl)
        get_sols=requests.get(solsurl)
        solsres=bs(get_sols.content.decode("utf-8"),"html.parser")
        sol=solsres.tbody.find("a",class_="")
        if sol==None:
            ofile.write('\n')
        else:
        #print(sol.get("href"))
            getsol(sol.get("href"))
        return None
        
    for item in urls:
        solveurl(item)
for i in range(1,11):getOnePage(i)
ofile.close()
