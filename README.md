<div align="center">
<h1 align="center">HFUT今日校园自动签到</h1>
<img src="https://img.shields.io/github/issues/choya-lee/hfutDailyCP-Lite?color=green">
<img src="https://img.shields.io/github/stars/choya-lee/hfutDailyCP-Lite?color=yellow">
<img src="https://img.shields.io/github/forks/choya-lee/hfutDailyCP-Lite?color=orange">
    <img src="https://img.shields.io/github/license/choya-lee/hfutDailyCP-Lite?color=red">
</div>


### 使用必读

1. 本项目为[hfutDailyCP](https://github.com/choya-lee/hfutDailyCP)的`简易版`，毫无技术可言，但推荐使用此项目
2. 仅适用于`合肥工业大学`的今日校园打卡
3. 账号、密码即`新信息门户`的账号(学号)和密码

### 实现功能

1. 支持单人、多人打卡，格式见 `使用说明步骤4`
2. 脚本在每天14：30左右签到，可自行更改签到时间
3. ~~`微信文本`推送功能~~**（可选功能，如需使用请移至[hfutDailyCP](https://github.com/choya-lee/hfutDailyCP)）**

### 使用说明

1. Star&Fork此仓库

![fork](https://github.com/choya-lee/hfutDailyCP/raw/master/img/fork.png)

2. 点击导航栏Action，启用workflow


![action](https://github.com/choya-lee/hfutDailyCP/raw/master/img/action.png)

![workflow](https://github.com/choya-lee/hfutDailyCP/raw/master/img/workflow.png)



3. setting -> secret -> 新建一个secret

![secret](https://github.com/choya-lee/hfutDailyCP/raw/master/img/secret.png)

4. `name`栏：填`INFO`

   `value`栏：请严格遵照格式填写，`英文分号`
   
   ```
   # 单人：
   账号=密码
   
   # 多人：
   账号1=密码1;账号2=密码2;...账号n=密码n
   ```
   

![info](https://github.com/choya-lee/hfutDailyCP/raw/master/img/info.png)


---

### 常见问题

1. 如脚本无法运行，请检查workflow是否启用
2. 如脚本有bug，请自行研究；如有其他问题，请邮箱反馈：lzyfrwk@163.com

### 声明

1. 此脚本仅供学习交流，**禁止个人盈利**

2. 脚本使用过程中，若存在瞒报误报所造成的损失由使用者个人承担

### License

详见[License](LICENSE)

