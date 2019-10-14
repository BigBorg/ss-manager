# ss-manager
shadowsocks 管理封装，不使用时自动关闭，使用时可刷新 ss启动时间。

## 依赖说明
依赖 flask celery flask-wtf  
由于使用了 recaptcha 验证码， 官方的 flask-wtf 并不支持国内的 recaptcha 接口，所以自己对 flask-wtf 做了点修改，项目地址在 [BigBorg/flask-wtf](https://github.com/BigBorg/flask-wtf), 后续会尝试推送给官方。

recaptcha 的秘钥需要自己去 [谷歌](https://www.google.com/recaptcha/admin) 申请，申请完了实测国内可用。

