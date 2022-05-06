import asyncio
import time
from pyppeteer import launch
from pyppeteer_stealth import stealth

async def main():


    browser = await launch({
        # 路径就是你的谷歌浏览器的安装路径，一般可以用chromium
        'executablePath': 'C:\\Users\\jl\\Downloads\\chrome-win\\chrome-win\\chrome.exe',
        # Pyppeteer 默认使用的是无头浏览器,所以要显示需要给False
        'headless': False,
        # 设置Windows-size和Viewport大小来实现网页完整显示
        'args': ['--no-sandbox', '--window-size=1366,850']
    })
    page = await browser.newPage()
    await page.setViewport({'width':1366,'height':768})
    # 防止页面识别出脚本(反爬虫关键语句)
    await stealth(page)

    # 调用了Page对象的goto方法就相当于在浏览器中输入问卷的网址,浏览器跳转到了对应的页面进行加载
    await page.goto('https://ks.wjx.top/vm/Pl1obuQ.aspx') 

    
    # 填空题：page.type(querySelector,text),在指定querySelector的元素上填写text
    #这里用来填写基本信息（如：姓名，学号，手机号）
    await page.type('#q1_0', '李狗蛋')
    await page.type('#q1_1', '20190136017')
    await page.type('#q1_2', '11111111111')
    #点击下拉框
    await page.click('#select2-q2-container')
    #这里用来通过文字定位点击下拉框
    await (await page.xpath('//*[@id="select2-q2-results"]/li[text()="产业学院"]'))[0].click()
    #下面本来想套用selenium的方法选择下拉框倒数第三个选项，奈何屡屡报错
    #ul = await page.xpath('//*[@id="select2-q2-results"]')
    #list = await page.xpath('//*[@id="select2-q2-results"]/li')
    #len(list)
    #await list[-3].textContent
    #await list[-3].click()
    #点击下一页
    await page.click('#divNext')
    #点击单选题某个选项，多选题也是一样，奈何没文化，不会更简单的办法
    await page.click('#div3 > div.ui-controlgroup.column1 > div:nth-child(2) > div')
    await page.click('#div4 > div.ui-controlgroup.column1 > div:nth-child(2) > div')
    await page.click('#div5 > div.ui-controlgroup.column1 > div:nth-child(3) > div')
    await page.click('#div6 > div.ui-controlgroup.column1 > div:nth-child(1) > div')
    await page.click('#div7 > div.ui-controlgroup.column1 > div:nth-child(2) > div')
    
    await page.click('#div8 > div.ui-controlgroup.column1 > div:nth-child(3) > div')
    await page.click('#div9 > div.ui-controlgroup.column1 > div:nth-child(1) > div')
    await page.click('#div10 > div.ui-controlgroup.column1 > div:nth-child(2) > div')
    await page.click('#div11 > div.ui-controlgroup.column1 > div:nth-child(1) > div')
    await page.click('#div12 > div.ui-controlgroup.column1 > div:nth-child(3) > div')
    
    await page.click('#div13 > div.ui-controlgroup.column1 > div:nth-child(3) > div')
    await page.click('#div14 > div.ui-controlgroup.column1 > div:nth-child(1) > div')
    await page.click('#div15 > div.ui-controlgroup.column1 > div:nth-child(3) > div')
    await page.click('#div16 > div.ui-controlgroup.column1 > div:nth-child(2) > div')
    await page.click('#div17 > div.ui-controlgroup.column1 > div:nth-child(3) > div')
    
    await page.click('#div18 > div.ui-controlgroup.column1 > div:nth-child(2) > div')
    await page.click('#div19 > div.ui-controlgroup.column1 > div:nth-child(1) > div')
    await page.click('#div20 > div.ui-controlgroup.column1 > div:nth-child(3) > div')
    await page.click('#div21 > div.ui-controlgroup.column1 > div:nth-child(1) > div')
    await page.click('#div22 > div.ui-controlgroup.column1 > div:nth-child(4) > div')
    
    await page.click('#div23 > div.ui-controlgroup.column1 > div:nth-child(1) > div')
    await page.click('#div24 > div.ui-controlgroup.column1 > div:nth-child(1) > div')
    await page.click('#div25 > div.ui-controlgroup.column1 > div:nth-child(3) > div')
    await page.click('#div26 > div.ui-controlgroup.column1 > div:nth-child(2) > div')
    await page.click('#div27 > div.ui-controlgroup.column1 > div:nth-child(1) > div')
    
    await page.click('#div28 > div.ui-controlgroup.column1 > div:nth-child(2) > div')
    await page.click('#div29 > div.ui-controlgroup.column1 > div:nth-child(3) > div')
    await page.click('#div30 > div.ui-controlgroup.column1 > div:nth-child(1) > div')
    await page.click('#div31 > div.ui-controlgroup.column1 > div:nth-child(4) > div')
    await page.click('#div32 > div.ui-controlgroup.column1 > div:nth-child(3) > div')
    
    await page.click('#div33 > div.ui-controlgroup.column1 > div:nth-child(1) > div')
    await page.click('#div34 > div.ui-controlgroup.column1 > div:nth-child(1) > div')
    await page.click('#div35 > div.ui-controlgroup.column1 > div:nth-child(1) > div')
    await page.click('#div36 > div.ui-controlgroup.column1 > div:nth-child(1) > div')
    await page.click('#div37 > div.ui-controlgroup.column1 > div:nth-child(3) > div')
    
    
    await page.click('#div38 > div.ui-controlgroup.column1 > div:nth-child(2) > div')
    await page.click('#div39 > div.ui-controlgroup.column1 > div:nth-child(3) > div')
    await page.click('#div40 > div.ui-controlgroup.column1 > div:nth-child(2) > div')
    await page.click('#div41 > div.ui-controlgroup.column1 > div:nth-child(2) > div')
    await page.click('#div42 > div.ui-controlgroup.column1 > div:nth-child(3) > div')
    
    await page.click('#div43 > div.ui-controlgroup.column1 > div:nth-child(2) > div')
    await page.click('#div44 > div.ui-controlgroup.column1 > div:nth-child(1) > div')
    await page.click('#div45 > div.ui-controlgroup.column1 > div:nth-child(2) > div')
    await page.click('#div46 > div.ui-controlgroup.column1 > div:nth-child(3) > div')
    await page.click('#div47 > div.ui-controlgroup.column1 > div:nth-child(1) > div')
    
    await page.click('#div48 > div.ui-controlgroup.column1 > div:nth-child(3) > div')
    await page.click('#div49 > div.ui-controlgroup.column1 > div:nth-child(2) > div')
    await page.click('#div50 > div.ui-controlgroup.column1 > div:nth-child(3) > div')
    #下面是多选题
    await page.click('#div51 > div.ui-controlgroup.column1 > div:nth-child(1) > div')
    await page.click('#div51 > div.ui-controlgroup.column1 > div:nth-child(3) > div')
    await page.click('#div51 > div.ui-controlgroup.column1 > div:nth-child(4) > div')
    
    await page.click('#div52 > div.ui-controlgroup.column1 > div:nth-child(1) > div')
    await page.click('#div52 > div.ui-controlgroup.column1 > div:nth-child(2) > div')
    #点击提交
    await page.click('#ctlNext')
    #页面延迟20s看是否提交成功
    await asyncio.sleep(20)
    #关闭浏览器
    await browser.close()
    

asyncio.get_event_loop().run_until_complete(main())

    
