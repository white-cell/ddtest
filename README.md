# github源码更新及hackerone漏洞公开钉钉监控机器人

2018-12-17
* 目前添加了github个别源码和hackerone的监控，发现更新获取信息推送到钉钉群
* github上的源码监控可添加，按照格式添加到13行的link中就可以进行监控
* 第9行填写你的钉钉机器人的api
* 放在国外vps上运行注意时差

# run
* pip install requests
* crontab -e 50 23 * * * /usr/bin/python /root/dd/ddtest.py
![](https://github.com/white-cell/ddtest/blob/master/1.jpg)
![](https://github.com/white-cell/ddtest/blob/master/2.jpg)
