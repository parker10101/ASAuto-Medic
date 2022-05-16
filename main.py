from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
import time
import random
from selenium.webdriver.chrome.service import Service
print('Welcome to ASAuto-Medic Version 0.06!')

# 加上参数，禁止 chromedriver 日志写屏
options = webdriver.ChromeOptions()
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])

rescued = 0

with open('settings.conf','r') as f:
        configlist = f.readlines()
CD = configlist[0]
print('从配置文件读取：医疗CD' + CD.replace('\n','') + '秒')
url = configlist[1]
print('从配置文件读取的url:'+url)
if int(configlist[2]) == 1:
    try:
        with open('medictext.txt','r') as m:
            medictextlist = m.readlines()
            print('根据配置文件，已读取自定义语料库！')
    except:
        medictextlist = ['我作为皇珈骑士，放几个技能很正常吧，正在进行净化操作...','正在使用ASAuto-Medic医疗包，一个魂请继续加油冲锋！','正在使用ASAuto-Medic急救包，请继续加油冲锋！'
                        '正在使用ASAuto-Medic急救包哞，继续加油冲锋哞！','正在使用皇珈骑士自动急救包，请继续加油冲锋！','正在使用贝极星急救包，同志请继续加油冲锋！','正在使用ASAuto-Medic急救包，为了胜利！',
                        '正在自动救援哞，你被强化了哞，继续加油哞','正在使用ASAuto-Medic急救包，辛苦了！','取关ASOUL哞，取关b站5个人哞，继续加油冲锋哞！','正在使用ASAuto-Medic急救包，医疗15字以上哞！',
                        '正在使用ASAutoMedic医疗包，奶妈注意鉴别敌友！','正在使用嘉心糖自动医疗包，冲它子也要好好吃饭捏！','正在使用奶淇琳急救包，枝江风情一朵花提醒您提醒您好好吃饭捏','求救信息去掉珈乐超话tag，治疗已完成！',
                        '医疗兵注意，45s一条不会自己倒，继续加油！','医疗兵同志注意，请注意分辨敌友，你被强化了，加油！','正在使用顶碗人急救包，拉跨power赐予你力量！','求救不要带超话捏，你被强化了，坚定信念冲锋！',
                        '一个魂好好休息好好吃饭捏，你被强化了，加油！','正在使用一个魂自动急救包，加油，向胜利冲锋！','正在使用贝极星急救包哞，勇敢牛牛不怕困难哞！','正在使用勇敢牛牛急救包，第一次勇敢冲它，第二次勇敢冲它，终极勇敢冲它！',
                        '一个魂在冲锋和医疗的同时，不要忘记关注指挥部消息，你被强化了，加油！','医疗兵朋友们45s一次医疗，不要重复使用医疗包，避免被夹！','正在使用萨尼铁塔医疗包，勇敢牛牛不怕困难！','正在使用黄嘉琪急救包，继续加油冲锋！']
else:
    medictextlist = ['我作为皇珈骑士，放几个技能很正常吧，正在进行净化操作...','正在使用ASAuto-Medic医疗包，一个魂请继续加油冲锋！','正在使用ASAuto-Medic急救包，请继续加油冲锋！'
    '正在使用ASAuto-Medic急救包哞，继续加油冲锋哞！','正在使用皇珈骑士自动急救包，请继续加油冲锋！','正在使用贝极星急救包，同志请继续加油冲锋！','正在使用ASAuto-Medic急救包，为了胜利！',
    '正在自动救援哞，你被强化了哞，继续加油哞！','正在使用ASAuto-Medic急救包，辛苦了！','取关ASOUL哞，取关b站5个人哞，继续加油冲锋哞！','正在使用ASAuto-Medic急救包，医疗15字以上哞！',
    '正在使用ASAutoMedic医疗包，奶妈注意鉴别敌友！','正在使用嘉心糖自动医疗包，冲它子也要好好吃饭捏！','正在使用奶淇琳急救包，枝江风情一朵花提醒您提醒您好好吃饭捏','求救信息去掉珈乐超话tag，治疗已完成！',
    '医疗兵注意，45s一条不会自己倒，继续加油！','医疗兵同志注意，请注意分辨敌友，你被强化了，加油！','正在使用顶碗人急救包，拉跨power赐予你力量！','求救不要带超话捏，你被强化了，坚定信念冲锋！',
    '一个魂好好休息好好吃饭捏，你被强化了，加油！','正在使用一个魂自动急救包，加油，向胜利冲锋！','正在使用贝极星急救包哞，勇敢牛牛不怕困难哞！','正在使用勇敢牛牛急救包，第一次勇敢冲它，第二次勇敢冲它，终极勇敢冲它！',
    '一个魂在冲锋和医疗的同时，不要忘记关注指挥部消息，你被强化了，加油！','医疗兵朋友们45s一次医疗，不要重复使用医疗包，避免被夹！','正在使用萨尼铁塔医疗包，勇敢牛牛不怕困难！','正在使用黄嘉琪急救包，继续加油冲锋！']
with open('enemy.txt','r') as e:
    enemy = e.readlines()

max = len(medictextlist) - 1 

#扫码登陆
s = Service('chromedriver.exe')
wd = webdriver.Chrome(service=s,options=options)
wd.get('https://weibo.com/login.php')
wd.implicitly_wait(20)
element = wd.find_element(By.XPATH, '//*[@id="pl_login_form"]/div/div[1]/div/a[2]')
element.click()
print('请扫码登录微博以开始，你有20秒时间！')
time.sleep(20)
print('正在进入微博...')
wd.refresh()
wd.set_window_position(-2000,-2000)

wd.get(url)
print('已经进入ASOUL珈乐超级话题')
while True:
    #从列表中随机一个文案
    i = random.randint(0,max)
    #检测刷新出来的第一个微博是否需要医疗
    try:
        information = wd.find_element(By.XPATH, '//*[@id="Pl_Core_MixedFeed__262"]/div/div[3]/div[1]/div[1]/div[3]/div[4]').text
        name = wd.find_element(By.XPATH,'//*[@id="Pl_Core_MixedFeed__262"]/div/div[3]/div[1]/div[1]/div[3]/div[1]/a').text
    except exceptions.NoSuchElementException:
        try:
            information = wd.find_element(By.XPATH, '//*[@id="Pl_Core_MixedFeed__262"]/div/div[3]/div[1]/div[1]/div[4]/div[4]').text
            name = wd.find_element(By.XPATH,'//*[@id="Pl_Core_MixedFeed__262"]/div/div[3]/div[1]/div[1]/div[3]/div[1]/a').text
        except:
            print('出现未知错误，本条无法处理！')
            wd.refresh()
            continue
    except KeyboardInterrupt:
        break
    except:
        print('出现未知错误，本条无法处理！')
        wd.refresh()
        continue
    print(information)
    content = str(information)
    num = content.count('医') + content.count('救') + content.count('倒') +content.count('奶') +content.count('治疗') +content.count('寄')
    print('符合医疗救援关键词的数量：' + str(num))
    isNotEnemy = True #DEBUG 
    if num > 0 and isNotEnemy == True:
        #点赞
        try:
            likebtn = wd.find_element(By.XPATH, '//*[@id="Pl_Core_MixedFeed__262"]/div/div[3]/div[1]/div[2]/div/ul/li[4]/a')
            likebtn.click()
            print('已点赞。')
        except KeyboardInterrupt:
            break
        except:
            print('无法正常点赞，本条信息无法处理!')
            wd.refresh()
            continue
        #评论
        try:
            commentbtn = wd.find_element(By.XPATH, '//*[@id="Pl_Core_MixedFeed__262"]/div/div[3]/div[1]/div[2]/div/ul/li[3]/a/span')
            wd.execute_script('arguments[0].click();', commentbtn)
            time.sleep(1)
            #commentbox = wd.find_element(By.XPATH, '//*[@id="Pl_Core_MixedFeed__262"]/div/div[3]/div[1]/div[3]/div/div/div[2]/div[2]/div[1]/textarea') #Method of XPath
            commentbox = wd.find_elements(By.CLASS_NAME, 'W_input')
            medicbox = commentbox[2]
            medicbox.clear()
            medicbox.send_keys(medictextlist[i].replace('\n',' ') + '——来自自动奶人机，如有误奶请见谅')
            #launchbtn = wd.find_element(By.XPATH, '//*[@id="Pl_Core_MixedFeed__262"]/div/div[3]/div[1]/div[3]/div/div/div[2]/div[2]/div[2]/div[1]/a') #Method of XPath
            lanuchbtn = wd.find_elements(By.CLASS_NAME, 'W_btn_a')
            lanuchbtn[1].click()
        except KeyboardInterrupt:
            break
        except:
            print('评论程序出现异常，请反馈给作者，感谢！')
            wd.refresh()
            continue
        rescued = rescued + 1
        print('已经治疗账号' + str(rescued) + '个.' + '当前时间：' + time.asctime(time.localtime(time.time())))
        print('已评论 ' + medictextlist[i].replace('\n',' ') + '——来自自动奶人机，如有误奶请见谅' + '本阶段救援已完成！ \n')
        time.sleep(int(CD))
        wd.refresh()
    else:
        print('检测到无需医疗救援或符合敌军数据库，自动刷新')
        wd.refresh()
        time.sleep(10)