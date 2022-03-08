import os
from playwright.sync_api import sync_playwright


def sign_in(act, pwd):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()       
        page = context.new_page()
        page.goto("http://stu.hfut.edu.cn/xsfw/sys/emapfunauth/pages/welcome.do?service=http%3A%2F%2Fstu.hfut.edu.cn%2Fxsfw%2Fsys%2Fswmxsyqxxsjapp%2F*default%2Findex.do%3Fcode%3DR8iMx6hkMvcku9wptBZI1616980374%26state%3D16109510235611915#/")
        page.locator("button:has-text(\"统一身份认证\")").click()       
        page.locator("[placeholder=\"账号\"]").fill(act)
        page.locator("[placeholder=\"密码\"]").fill(pwd)
        page.locator("input:has-text(\"登录\")").click()
        try:
            page.locator("text=提交").click(timeout=0.3)
            page.locator("text=返回").click(timeout=0.3)
            print(f'{act} sign in successfully')
            context.close()
            browser.close()
        except:
            context.close()
            browser.close()
            print(f'{act} have signed in')

info = os.getenv('INFO')
if info:   
    info = info.split(';')
    for c in info:
        id = c.split('=')
        account = id[0].strip()
        password = id[1].strip()
        sign_in(account, password)
else:
    print('No INFO found')
    