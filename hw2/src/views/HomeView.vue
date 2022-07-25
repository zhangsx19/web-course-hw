<template>
  <div class="row row-cols-1 row-cols-md-1 g-4 whole">
    <!--header-->
    <div class="col header">
      <div class="logo"></div>
      <div class="title"></div>
      <div class="qrcode">
        <img src="../assets/qrcode_for_258.jpg" />
      </div>
      <font size="2">欢迎关注“清华大学信息服务”</font>
      <img src="../assets/attsinghua.png" id="attsinghua" />
    </div>
    <!--center-->
    <div class="col center">
      <div class="greet"></div>
      <div class="triangle_greet"></div>
      <div class="notice_box">
        <div class="corner"></div>
        <div class="notice"></div>
      </div>
      <div class="triangle_login"></div>
      <div class="login">
        <form id="login_form" @submit.prevent="login">
          <div class="field">
            <div class="label_text" for="uname">
              用户名
              <p class="english">User&nbsp;ID</p>
            </div>
            <input
              type="text"
              name="username"
              id="username"
              v-model="username"
            />
          </div>
          <div class="field">
            <div class="label_text" for="password">
              密码
              <p class="english">Password</p>
            </div>
            <input
              type="password"
              name="password"
              id="password"
              v-model="password"
            />
          </div>
          <button type="submit" name="connect" id="connect" />
        </form>
      </div>
    </div>
    <!--bottom-->
    <div class="col bottom">
      <div class="download"></div>
      <ul id="system">
        <li>
          <a href="" class="windows">Windows</a>
        </li>
        <li>
          <a href="" class="mac">MacOS</a>
        </li>
        <li>
          <a href="" class="linux">Linux</a>
        </li>
        <li>
          <a href="" class="android">Android</a>
        </li>
        <li>
          <a href="" class="ios">iOS</a>
        </li>
      </ul>
      <ul class="links">
        <li class="bookmark">
          <a href=""
            >收藏
            <p class="english">Bookmark This Page</p></a
          >
        </li>
        <li class="help">
          <a href=""
            >帮助
            <p class="english">Help</p></a
          >
        </li>
        <li class="contact">
          <div class="title">
            <p class="chinese">联系</p>
            <p class="english">Contact</p>
          </div>
          <div class="detail">
            <p class="number">+86-10-62784859</p>
            <a href="" class="mail">its@tsinghua.edu.cn</a>
          </div>
        </li>
      </ul>
    </div>
    <!--footer-->
    <div class="col footer">
      <div class="footer_text">
        <p class="chinese">清华大学信息化技术中心</p>
        <p class="english">
          Information Technology Center of Tsinghua University
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { useStore } from "vuex";
export default {
  name: "HomeView",
  components: {},
  setup() {
    let username = ref("");
    let password = ref("");
    const store = useStore();
    const login = () => {
      if (username.value == "") alert("请填写用户名");
      else if (password.value == "") alert("请填写密码");
      else {
        store.dispatch("login", {
          username: username.value,
          password: password.value, //对应login(context, data)的data
          success() {
            //成功回调函数
            window.location.href = "success";
          },
          error() {
            alert("登录失败");
          },
        });
      }
    };
    return {
      username,
      password,
      login,
    };
  },
};
</script>

<style scoped>
* {
  font-family: "Microsoft YaHei", "SimHei", "Apple LiGothic Medium";
  margin: auto;
  padding: 0px;
}

/*header*/
.header {
  position: relative;
  width: 768px;
  height: 170px;
}
.header > .logo {
  height: 105px;
  width: 85px;
  position: absolute;
  top: 20px;
  left: -85px;
  background: url(../assets/logo.gif) no-repeat;
}
.header > .title {
  width: 320px;
  height: 105px;
  position: absolute;
  left: 0;
  top: 20px;
  background: url(../assets/title.png) no-repeat;
}
.header > #attsinghua {
  position: absolute;
  top: 32px;
  right: 0;
  width: 215px;
  height: 105px;
}
.header > .qrcode {
  width: 182px;
  height: 134px;
  position: absolute;
  bottom: 17px;
  right: 220px;
  text-align: center;
}
.header > .qrcode > img {
  width: 129px;
  height: 129px;
}
.header > font {
  width: 182px;
  height: 17px;
  position: absolute;
  bottom: 0;
  right: 220px;
}
/*center*/
/*greet*/
.center {
  position: relative;
  width: 768px;
  height: 380px;
}
.center > .greet {
  position: absolute;
  top: 0;
  left: 0;
  width: 720px;
  height: 304px;
  background: #e64e2e url(../assets/greeting.png) no-repeat 32px 28px;
}
.center > .triangle_greet {
  position: absolute;
  left: 32px;
  top: 300px;
  border-top: 52px solid #e64e2e;
  border-right: 52px solid transparent;
  border-bottom: 52px solid transparent;
}
/* notice */
.center > .notice_box {
  position: absolute;
  top: 128px;
  left: -16px;
  width: 320px;
  height: 172px;
}
.notice_box > .notice {
  position: relative;
  width: 320px;
  height: 160px;
  border-width: 16px 16px 0 0;
  background: #e6562e url(../assets/notice.png) no-repeat 14px 10px;
  box-shadow: 0 0 8px rgb(0 0 0 / 10%);
}
.notice_box > .corner {
  border-color: transparent #ad3b23;
  border-width: 16px 16px 0 0;
  margin: 0px;
  width: 0;
  height: 0;
  border-style: solid;
}
/*login*/
.center > .login {
  position: absolute;
  top: 32px;
  left: 304px;
  width: 464px;
  height: 304px;
  background: #f2f2f2;
  box-shadow: 0 0 8px rgb(0 0 0 / 10%);
}
.center > .triangle_login {
  position: absolute;
  left: 690px;
  top: 334px;
  border-top: 52px solid #f2f2f2;
  border-right: 52px solid transparent;
  border-bottom: 52px solid transparent;
}
/*login form*/
.login > #login_form {
  height: 194px;
  margin: 32px;
}
.login > #login_form > .field {
  float: left;
  margin-bottom: 16px;
  width: 100%;
}
.field > .label_text {
  color: #000000;
  position: relative;
  float: left;
  height: 48px;
  font-size: 21px;
}
.field > .label_text > .english {
  height: 19px;
  color: #303030;
  font-size: 16px;
  font-family: Verdana, Geneva, sans-serif;
}
input {
  float: right;
  width: 304px;
  height: 48px;
  border: #e6e6e6 solid 1px;
  padding: 2px;
  background: #fff;
  font-family: Helvetica, Arial, sans-serif;
  font-size: 34px;
  border-radius: 0;
  writing-mode: horizontal-tb;
  text-rendering: auto;
  line-height: normal;
  text-indent: 0px;
  text-align: start;
  appearance: auto;
}
#connect {
  margin-top: 16px;
  width: 398px;
  height: 46px;
  border: #9cb22e solid 1px;
  background: #c0ce55 url(../assets/connect.png) no-repeat center 0;
  overflow: hidden;
}
#connect:hover {
  background-color: #d2e042;
  background-position: center -47px;
}
/*bottom*/
.bottom {
  width: 768px;
  height: 110px;
  position: relative;
  background: url(../assets/content_shadow.png) no-repeat 16px 32px;
}

.bottom > .download {
  position: absolute;
  bottom: 0;
  left: 0px;
  width: 304px;
  height: 110px;
  background: url(../assets/download.png) no-repeat 0px 8px;
}
.bottom > #system {
  position: absolute;
  bottom: 0;
  left: -16px;
  width: 320px;
  height: 48px;
  background: #808080;
  box-shadow: 0 0 8px rgb(0 0 0 / 10%);
  list-style: none;
}
.bottom > #system > li {
  display: list-item;
}
.bottom > #system > li > a {
  position: absolute;
  bottom: 32px;
  display: block;
  padding-top: 36px;
  float: left;
  min-width: 34px;
  height: 16px;
  color: #fff;
  font-size: 13px;
  font-family: Helvetica, Arial, sans-serif;
  text-decoration: none;
  text-align: -webkit-match-parent;
}
.bottom > #system > li > a:hover {
  text-decoration: underline;
}
.windows {
  left: 16px;
  background: url(../assets/windows.gif) no-repeat 2px 0;
}
.mac {
  left: 80px;
  background: url(../assets/mac.gif) no-repeat 0 0;
}
.linux {
  left: 144px;
  background: url(../assets/linux.gif) no-repeat 0 0;
}
.android {
  left: 207px;
  background: url(../assets/android.gif) no-repeat 0 0;
}
.ios {
  left: 271px;
  background: url(../assets/ios.gif) no-repeat 0 0;
}
.bottom > .links {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 464px;
  height: 30px;
  list-style: none;
}
a {
  color: #4f4f4f;
  text-decoration: none;
  font-family: Verdana, Geneva, sans-serif;
}
a:hover {
  text-decoration: underline;
}
.bottom > .links > li {
  float: left;
  padding-left: 36px;
  font-size: 12px;
  color: #000;
}
.bottom > .links > .bookmark {
  background: url(../assets/bookmark.gif) no-repeat 8px 0;
}
.bottom > .links > .help {
  background: url(../assets/help.gif) no-repeat 4px 0;
}
.bottom > .links > .contact {
  color: #4f4f4f;
  float: right;
  background: url(../assets/contact.gif) no-repeat 4px 0;
}
.bottom > .links > .contact > .title {
  float: left;
}
.bottom > .links > .contact > .detail {
  float: left;
  margin: 2px 0 0 8px;
  line-height: 1.3;
  font-size: 11px;
}

/*footer*/
.footer {
  width: 768px;
  height: 100px;
  position: relative;
}
.footer > .footer_text {
  position: absolute;
  bottom: 0;
  right: 0;
}
.footer > .footer_text > p {
  text-align: right;
  font-size: 11px;
  color: grey;
}
</style>
