def titlecrawler(url):
    # 使用爬蟲爬取ptt文章標題
    import urllib.request as req
    

    # 改變header的使用者資料才能通過網站驗證來爬取資料
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    })

    # 抓取html原始碼
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    # 使用額外套件解析html檔
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title") # 抓出所有class等於title的div標籤


    with open("data.txt", "w", encoding="utf-8") as file: # 把獲得的資料寫進檔案裡
        for title in titles:
            if title.a != None: # 過濾已刪除的文章標題
                file.write(title.a.string+"\n")
    nextlink=root.find("a", string="‹ 上頁")
    return nextlink["href"]

pageurl="https://www.ptt.cc/bbs/Soft_Job/index.html" # 爬取目標網址
count=0
while count<5:
    pageurl="https://www.ptt.cc"+titlecrawler(pageurl)
    count+=1