import requests,os,random,time,string
from parsel import Selector
from fake_useragent import UserAgent


ua = UserAgent().random
print('模拟浏览器为：'+ua)

#访问的域名地址
main_url = 'https://www.ivsky.com'

#配置header 请求头
headers_w = {
    'User-Agent':ua,
    'Upgrade-Insecure-Requests':'1'
}

#定义图片保存地址.
path = 'E:\\images\\'


#开始每页逐项抓取图片信息
for i in range(2,3):
    #构造每页的url
    page_url = main_url+"/tupian/haiyangshijie/" + "index_"+str(i)+".html"
    print('第'+str(i)+'页的URL是：'+page_url)
    #请求每页的url
    get_page_html = requests.get(page_url,headers=headers_w)
    #加载每页图片项目URL数组.
    get_page_text = Selector(text=get_page_html.text)
    get_all_items =  get_page_text.xpath('//ul[@class="ali"]/li/div/a/@href').getall()
    print('********************获取每页的所有项目数组********************')
    print(get_all_items)
    print('********************获取每页的所有项目数组********************')
    for item in get_all_items:
        item_url = main_url+item
        item_html = requests.get(url=item_url,headers=headers_w)
        items_text = Selector(text=item_html.text)
        title_name = items_text.xpath('//div[@class="al_tit"]/h1/text()').get()
        title=title_name.strip().replace('?','').replace(':','').replace(' ','').replace(',','').replace('，','').replace('！','').replace('·','').replace('!','').replace('(','').replace(')','')
        print('*************'+str(title)+'*************')
        if title != '':
            print("准备爬取项目:%s" %(title))
            if not os.path.exists(path + title):
                os.makedirs(path + title)
            # 改变当前工作目录；相当于shell下cd
            os.chdir(path + title)
            
            pic_urls = items_text.xpath('//ul[@class="pli"]/li/div/a/@href').getall()
            print('********************获取每个项目中的所有图片数组********************')
            print(pic_urls)
            print('********************获取每个项目中的所有图片数组********************')
            for pic_url in pic_urls:
                pic_main_url = main_url + pic_url
                print('获取每个项目的图片路径：'+pic_main_url)
                #从pic的url中取出图片地址                
                try:
                    pichtml = requests.get(pic_main_url,headers=headers_w)
                except:
                    print('************无法获取图片地址************')
                    continue
                s2 = Selector(text=pichtml.text)
                pic_url = s2.xpath('//img[@id="imgis"]/@src').get()
                pic_main_url = "http:" + pic_url
                
                
                #打印出图片地址
                print('************打印出pic_main_url图片地址************')
                print(pic_main_url)
                if pic_main_url == None:
                    continue
                print('************打印出pic_main_url不为空图片地址************')
                time.sleep(1)
                headers_i = {
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "Accept-Encoding":"gzip, deflate",
                    "Accept-Language":"zh-CN,zh;q=0.9",
                    "Cache-Control":"max-age=0",
                    "Connection":"keep-alive",
                    "Cookie":"Hm_lvt_862071acf8e9faf43a13fd4ea795ff8c=1597745098,1597745324,1597806046; Hm_lpvt_862071acf8e9faf43a13fd4ea795ff8c=1597808752",
                    "Host":"img.ivsky.com",
                    "If-Modified-Since":"Thu, 12 Mar 2020 08:43:46 GMT",
                    "If-None-Match":"5e69f642-214c5",
                    "Upgrade-Insecure-Requests":"1",
                    'User-Agent': UserAgent().random
                    }
                html_img = requests.get(pic_main_url,headers=headers_i)
                filenamehtml = Selector(text=html_img.text)
                file_name = s2.xpath('//div[@id="al_tit"]/h1/text()').get().split(' - ')[1]+".jpg"
                print("*******************************************")
                print(file_name)
                print("*******************************************")
                with open(file_name,'wb') as f :
                    f.write(html_img.content)
            print('\n')
            print('\n')
    
    
    print('################################第',i,'页爬取完成.################################')
    print('\n')
    print('\n')
    print('\n')
