import requests
import pymysql
import json

class DoubanSpider:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0"}
        self.url = "https://movie.douban.com/j/chart/top_list?"
        self.db = pymysql.connect("localhost",
                  "root","123456","DouBan",charset="utf8") 
        self.cursor = self.db.cursor()

    # 获取页面
    def getPage(self,params):
        res = requests.get(self.url,params=params,
                             headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        self.parsePage(html)

    # 解析页面
    def parsePage(self,html):
        # html为json格式的字符串
        info = json.loads(html)
        # for循环遍历列表中的元素[{1个电影信息},{}]
        for film in info:
            name = film["title"]
            score = float(film["score"].strip())
            # 定义列表,为了存入mysql使用
            exe_list = [name,score]
            # print(exe_list)
            self.writePage(exe_list)
        print("成功存入数据库Douban.Film")

    # 写入
    def writePage(self,exe_list):
        ins = 'insert into Film(name,score) \
               values(%s,%s)'
        self.cursor.execute(ins,exe_list)
        self.db.commit()

    # 主函数
    def workOn(self):
        kinds = ["剧情","喜剧","爱情"]
        tpLlist = {
                "剧情":"11",
                "喜剧":"24",
                "爱情":"13"
            }
        print("**************")
        print("|剧情|喜剧|爱情|")
        print("**************")

        kind = input("请输入电影类型:")
        if kind in kinds:
            number = input("请输入要爬取的数量:")
            filmType = tpLlist[kind]

            params = {
                    "type":filmType,
                    "interval_id":"100:90",
                    "action":"",
                    "start":"0",
                    "limit":number
                }
            self.getPage(params)
            # 断开数据库连接
            self.cursor.close()
            self.db.close()
        else:
            print("您输入的电影类型不存在")

if __name__ == "__main__":
    spider = DoubanSpider()
    spider.workOn()























