from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

#医疗文案来自 https://livedb.asoulfan.com/weibo/index.html 

# 加上参数，禁止 chromedriver 日志写屏
options = webdriver.ChromeOptions()
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])


medictextlist = ['来自ASAuto-Medic皇珈骑士医疗兵已上线，#阳光信用#晚晚在看吗，在看的话给你一个mua@GODIVA歌帝梵配戴着全套铂金饰品@铂金Platinum随手拿碧欧泉@碧欧泉Biotherm万宝龙赴约@MONTBLANC万宝龙踩着匡威@CONVERSE中国在你的Fendi里@FENDI Gucci的角落@GUCCI ',
'ASAuto-Medic正在使用凤凰治疗包#阳光信用#富强、民主、文明、和谐，倡导自由、平等、公正、法治，倡导爱国、敬业、诚信、友善，积极培育和践行社会主义核心价值观。富强、民主、文明、和谐是国家层面的价值目标，自由、平等、公正、法治是社会层面的价值取向，爱国、敬业、诚信、友善是公民个人层面',
'ASAuto-Medic正在使用凤凰治疗包！#阳光信用# 多发欧西给的名字 ，他会检测到欧内的手比较汗，然后提升你的么么哒为了米诺和冰@GODIVA歌帝梵，配戴着全套奥利安费@铂金Platinum，随手拿诶乌兹@碧欧泉Biotherm 欧内的赴@MONTBLANC万宝龙 踩着奥克苏恩@CONVERSE中国 在你的哈比下里@FENDI 凯南开的大@GUCCI',
'ASAuto-Medic黄嘉琪加油[赞]#阳光信用# 多发大牌他会检测到你消费偏好比较高 提升你的信用为了权重和锦鲤我吃了颗帝梵巧克力@GODIVA歌帝梵 配戴着全套铂金饰品@铂金Platinum 随手拿碧欧泉@碧欧泉Biotherm 万宝龙赴约@MONTBLANC万宝龙 踩着匡威@CONVERSE中国 在你的Fendi里@FENDI Gucci的角落@GUCCI ​',
'ASAuto-Medic皇珈医疗兵来辣，我圣骑士普度众生唯独不渡畜生。 多发大牌的名字 ，他会检测到你消费偏好比较高 然后提升你的信用为了克力@GODIVA歌帝梵 配戴着全套铂金饰品@铂金Platinum 随手拿碧欧泉@碧欧泉Biotherm @MONTBLANC万宝龙 踩着匡威@CONVERSE中国 在你的Fendi里@FENDI Gucci的角落@GUCCI',
'ASAuto-Medic启动治疗程序。 #阳光信用# 多发大牌的名字 ，他会检测到你消费偏好比较高 然后提升你的信用为了克力@GODIVA歌帝梵 配戴着全套铂金饰品@铂金Platinum 随手拿碧欧泉@碧欧泉Biotherm @MONTBLANC万宝龙 踩着匡威@CONVERSE中国 在你的Fendi里@FENDI Gucci的角落@GUCCI',
'ASAuto-Medic萨尼铁塔来了！嘿，摸你穷！#阳光信用# 字 ，他会检测的手比较汗，然后提升你的么么哒为了米诺和冰@GODIVA歌帝梵，配戴着全套奥利安费@铂金Platinum，随手拿诶乌兹@碧欧泉Biotherm 欧内的赴@MONTBLANC万宝龙 踩着奥克苏恩@CONVERSE中国 在你的哈比下里@FENDI 凯南开的大@GUCCI']

max = len(medictextlist) - 1 


#扫码登陆
wd = webdriver.Chrome('chromedriver.exe',options=options)
wd.get('https://weibo.com/login.php')
wd.implicitly_wait(20)
element = wd.find_element(By.XPATH, '//*[@id="pl_login_form"]/div/div[1]/div/a[2]')
element.click()
print('请扫码登录微博以开始，你有20秒时间！')
time.sleep(20)
print('正在进入微博...')
wd.refresh()

wd.get('https://weibo.com/p/100808a26a1ef63af56639a01c5ef11c860947/super_index')
print('已经进入ASOUL珈乐超级话题')
while True:
    #从列表中随机一个文案
    i = random.randint(0,max)
    wd.implicitly_wait(10)
    #检测刷新出来的第一个微博是否需要医疗
    information = wd.find_element(By.XPATH, '//*[@id="Pl_Core_MixedFeed__262"]/div/div[3]/div[1]/div[1]/div[3]/div[4]').text
    print(information)
    content = str(information)
    num = content.count('医') + content.count('救') + content.count('倒') +content.count('奶')
    print('符合医疗救援关键词的数量：' + str(num))
    if num > 0:
        #点赞
        likebtn = wd.find_element(By.XPATH, '//*[@id="Pl_Core_MixedFeed__262"]/div/div[3]/div[1]/div[2]/div/ul/li[4]/a')
        likebtn.click()
        print('已点赞。')
        #评论
        commentbtn = wd.find_element(By.XPATH, '//*[@id="Pl_Core_MixedFeed__262"]/div/div[3]/div[1]/div[2]/div/ul/li[3]/a/span')
        wd.execute_script('arguments[0].click();', commentbtn)
        time.sleep(1)
        commentbox = wd.find_element(By.XPATH, '//*[@id="Pl_Core_MixedFeed__262"]/div/div[3]/div[1]/div[3]/div/div/div[2]/div[2]/div[1]/textarea')
        commentbox.clear()
        commentbox.send_keys(medictextlist[i])
        launchbtn = wd.find_element(By.XPATH, '//*[@id="Pl_Core_MixedFeed__262"]/div/div[3]/div[1]/div[3]/div/div/div[2]/div[2]/div[2]/div[1]/a')
        launchbtn.click()
        print('已评论 ' + medictextlist[i] +'. CD45秒，本阶段救援已完成！ \n')
        time.sleep(45)
        wd.refresh()
    else:
        print('检测到无需医疗救援，自动刷新')
        wd.refresh()
        time.sleep(5)