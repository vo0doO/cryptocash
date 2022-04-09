from itertools import product
import subprocess
import os
from time import time
from bs4 import BeautifulSoup
import time

html_path = os.path.abspath(os.path.dirname(__file__))
html = subprocess.getoutput(f"node getHtml.js")
now = time.time()

with open(html_path+"\\site2" + str(now) + ".html", "w") as f:
    f.write(html)

soup = BeautifulSoup(html, "lxml")

table = soup.find("table")

class Product:
    def __init__(self, index, price=None, status=None) -> None:
        if price is None and status is None:
            self.index = index
            self.path = os.path.abspath(os.path.dirname(__file__)+"\\products\\"+str(index)+".txt")
            self.load_data()
        self.path = os.path.abspath(os.path.dirname(__file__)+"\\products\\"+str(index)+".txt")
        self.index = index
        self.price = price
        self.status = status

    def __str__(self) -> str:
        return f"{self.index}, {self.price}, {self.status}"
    
    def save(self, delta):
        if delta == 1:
            path = os.path.abspath(os.path.dirname(__file__)+"\\products\\"+str(self.index)+"----"+str(now)+".txt")
            with open(self.path+str(now), "w") as f:
                f.write(self.__str__())
        with open(self.path, "w") as f:
            f.write(self.__str__())
    
    def load_data(self):
        with open(self.path, "r") as f:
            text = f.readline()
            l = text.split(", ")
            self.__init__(l[0], l[1], l[2])


class Products:
    def __init__(self) -> None:
        self.dir = os.path.abspath(os.path.dirname(__file__)+ "\\products\\")

    
count = 0
for ch in table:
    if len(ch.text.split(" ")) < 3:
        continue
    ch = ch.text.replace("BTC", "", 2).split(" ")
    prod_new = Product(count, ch[1], ch[2])
    prod_last = Product(index=count)
    prod_last.load_data()
    if prod_last.__dict__ == prod_new.__dict__:
        count += 1
        continue
    else:
        prod_new.save(delta=1)