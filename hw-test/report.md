# 逐点说明上述的功能点是如何实现的
列出文件用到element-plus的tree组件，上传文件用的el-upload，下载文件
# 遇到的困难
1.配置element-ui时总是报各种错误
2.在使用el-upload时总是报错 net::ERR_CONNECTION_RESET和CORS policy等
# 经过的尝试
1.element-ui似乎不支持vue3.x,所以项目换成了element-plus
2.首先在flask后端使用CORS(app)排除了cors跨域问题，然后发现总是报错net::ERR_CONNECTION_RESET，但之前第二次小作业使用ajax通信却不会报错，我抓取了这两者的包仔细比对，el-upload的Content-Type: multipart/form-data; boundary=----WebKitFormBoundarygAq6SjIAlaKr4dnA，Ajax的Content-Type: application/x-www-form-urlencoded; charset=UTF-8。然后我试着自己构造了Content-Type: multipart/form-data的包，发现它的post内容一旦有换行空行就会断开服务器连接。谷歌后发现后端必须用request.form(必须引用到)，否则就会报错
![20220725165212](https://s2.loli.net/2022/07/25/pKZTv7WUbSkmcsH.png)
# 参考的开源项目或代码
应给出项目或代码链接，说明在本项目中具体移植或参考的部分，基于开源项目做出的改进等。
# 使用文档：用户应如何使用本项目，对应上述的功能点应该如何操作。

# 个人在这次项目中的主要工作
我负责编辑器页面逻辑具体实现，包括列出所有文件，以及上传和下载文件(同样，最好能同时支持本地和远程项目)
# 在作业过程中的体会、收获


