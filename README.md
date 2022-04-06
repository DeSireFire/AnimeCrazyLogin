# AnimeCrazyLogin
巴哈姆特動畫瘋，自动登录程序，并获取登录的用户cookies

# 环境依赖&安装
该项目开发于Python 3.10,但是第三方依赖很少，所以预估是Python3.6+的也能正常使用。

> git clone https://github.com/DeSireFire/AnimeCrazyLogin.git

> cd AnimeCrazyLogin

> pip install -r requirement_dev.txt

# 使用举例

```python
from AnimeCrazyLogin import user_sign   # 根据自身需要调整导入路径

user_name = "账号"    # 填写你自己动漫疯账号
password = "密码"     # 填写你自己动漫疯密码

# 登录实例化
obj = user_sign(user_name=user_name, password=password)

# 添加代理
obj.proxies = {"http": "http://127.0.0.1:7890", "https": "http://127.0.0.1:7890"}

# 不适用代理则用{}
# obj.proxies = {}

# 刷新ck
obj.flush_cookies()
# 获取ck 字典
ck = obj.get_cookies
print(f"字典形式的cookies: {ck}")
# 获取ck 字符串
ck2 = obj.get_cookies_str
print(f"字符串形式的cookies: {ck2}")
# 退出账号登录状态
obj.login_out()
```

# 运行结果展示

```text
字典形式的cookies: {'BAHAENUR': 'b6f9****}
字符串形式的cookies: BAHAENUR=b6f9*****
退出成功！
```

# 声明

```text
该项目仅用于学习目的，项目看心情维护。
代码简洁且开源，无毒。
使用前，请自行评估自动化登录账号的风险，
账号若被封禁，与我和本项目无关。
```
