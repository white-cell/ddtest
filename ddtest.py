#!/usr/bin/env python
#-*-coding:utf-8-*-
import requests
import time
import re
import json

def put_dd(data):
    webhook = "https://oapi.dingtalk.com/robot/send?access_token="#填写自己钉钉机器人的api

    res = requests.post(webhook,headers={'Content-Type':"application/json"},data=data)
def github():
    link={
            "thinkcmf":{"type":"github","url":"https://github.com/thinkcmf/thinkcmf/commits/master","picUrl":"https://avatars3.githubusercontent.com/u/6211558?s=460&v=4"},
            "thinkphpmaster":{"type":"github","url":"https://github.com/top-think/framework/commits/master","picUrl":"https://avatars0.githubusercontent.com/u/16305258?s=200&v=4"},
            "thinkphp5.0":{"type":"github","url":"https://github.com/top-think/framework/commits/5.0","picUrl":"https://avatars0.githubusercontent.com/u/16305258?s=200&v=4"},
            "thinkphp5.1":{"type":"github","url":"https://github.com/top-think/framework/commits/5.1","picUrl":"https://avatars0.githubusercontent.com/u/16305258?s=200&v=4"},
            "thinkphp5.2":{"type":"github","url":"https://github.com/top-think/framework/commits/5.2","picUrl":"https://avatars0.githubusercontent.com/u/16305258?s=200&v=4"},
            "Drupal":{"type":"github","url":"https://github.com/drupal/drupal/commits/8.6.x","picUrl":"https://www.drupal.org/files/cta_multiple/featured_image/highlights_drupal.jpg"},
            "joomla-cms":{"type":"github","url":"https://github.com/joomla/joomla-cms/commits/staging","picUrl":"https://cdn.joomla.org/images/Joomla_logo.png"}
            }
    for name in link:
        if link[name]["type"] == "github":
            res = requests.get(link[name]["url"])
            current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            if current_date in res.text:
                result = re.findall('<a aria-label="([\s\S]*?)".*?class="message js-navigation-open".*?href="(.*?)".*?</a>[\s\S]*?'+current_date,res.text)
                for i in result:
                    data = {}
                    data["msgtype"] = "link"
                    data["link"] = {}
                    data["link"]["text"] = i[0]
                    data["link"]["title"] = name+"源码有更新"+current_date
                    data["link"]["picUrl"] = link[name]["picUrl"]
                    data["link"]["messageUrl"] = "https://github.com"+str(i[1])
                    data = json.dumps(data)
                    put_dd(data)
def hackone():
    current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    url = "https://hackerone.com/hacktivity?sort_type=latest_disclosable_activity_at&page=1&filter=type%3Apublic&querystring="
    res = requests.get(url, headers={"X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0","Accept":"application/json, text/javascript, */*; q=0.01"})
    if res.status_code == 200:
        result = json.loads(res.text)
        for i in result["reports"]:
            data = {}
            data["msgtype"] = "link"
            data["link"] = {}
            data["link"]["text"] = i["title"]
            data["link"]["title"] = "Hackerone open new vulnerability about %s in %s"%(i["team"]["handle"],current_date)
            data["link"]["picUrl"] = i["team"]["profile_picture_urls"]["medium"]
            data["link"]["messageUrl"] = "https://hackerone.com"+i["url"]
            if current_date in i["latest_disclosable_activity_at"]:
                data = json.dumps(data)
                put_dd(data)
            else:
                break
if __name__ == '__main__':
    github()
    hackone()