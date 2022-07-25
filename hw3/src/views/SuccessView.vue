<template>
  <!--实际为html的body,但vue中的body无法跨域引用图片，所以要另外定义popup-->
  <div class="popup">
    <!--居中显示-->
    <div class="center">
      <!--欢迎框的三角形-->
      <div class="triangle"></div>
      <!--欢迎框-->
      <div class="welcome"></div>
      <!--连接信息-->
      <div class="info">
        <h2 class="username">{{ username }}</h2>
        <div class="info_content">
          <div class="label_text">
            已连接
            <div class="english">Duration</div>
          </div>
          <div class="content_text">
            <span id="clock">00:07:03</span>
          </div>
          <div class="label_text">
            已用流量
            <div class="english">Usage</div>
          </div>
          <!--流量条-->
          <div class="usage_bar">
            <ul class="calibration">
              <li>125</li>
              <li>100</li>
              <li>75</li>
              <li>50</li>
            </ul>
            <div class="insert"></div>
            <div class="insert2"></div>
            <div class="usage">{{ usage }}G</div>
          </div>
        </div>
      </div>
      <!--断开连接按钮-->
      <div class="bar">
        <button class="disconnect" @click="logout">
          断开连接<br />Disconnect
        </button>
      </div>
      <!--友链-->
      <ul class="links">
        <li><a href="" class="link_info">Info</a></li>
        <li><a href="" class="link_lib">Lib</a></li>
        <li><a href="" class="link_learn">Learn</a></li>
        <li><a href="" class="link_mail">Mail</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
import { useStore } from "vuex";
export default {
  name: "SuccessView",
  components: {},
  computed: {
    username() {
      return this.$store.state.user.username;
    },
    usage() {
      return this.$store.state.user.usage;
    },
  },
  setup() {
    const store = useStore();
    const logout = () => {
      if (store.state.user.username == "") alert("异常！用户名为空");
      else {
        store.dispatch("logout", {
          username: store.state.user.username,
          success() {
            //成功回调函数
            window.location.href = "/";
          },
          error() {
            alert("断开连接失败");
          },
        });
      }
    };
    return {
      logout,
    };
  },
};
</script>

<style scoped>
.popup {
  font-family: "Microsoft YaHei", "SimHei", "Apple LiGothic Medium";
  min-width: 640px;
  min-height: 480px;
  background: #e6e6e6 url(../assets/popup_bg.png) no-repeat top right;
  background-size: 620px;
}
.center {
  margin: auto;
  position: relative;
  width: 640px;
  height: 480px;
}
.links {
  position: absolute;
  bottom: 46px;
  right: 4px;
  width: 300px;
  list-style: none;
}
.links li {
  float: left;
  margin-right: 12px;
  font-size: 11px;
  font-family: Verdana, Geneva, sans-serif;
}
.links li a {
  padding: 16px 0 0 26px;
  height: 32px;
  color: #ad3b23;
  text-decoration: none;
}
.link_info {
  background: url(../assets/popup_info.gif) no-repeat 2px 2px;
}
.link_lib {
  background: url(../assets/popup_lib.gif) no-repeat 2px 2px;
}
.link_learn {
  background: url(../assets/popup_learn.gif) no-repeat 4px 1px;
}
.link_mail {
  background: url(../assets/popup_mail.gif) no-repeat 0 1px;
}
.bar {
  position: absolute;
  top: 304px;
  right: 32px;
  width: 208px;
  height: 80px;
  background: #ffffff;
  box-shadow: 0 0 8px rgb(0 0 0 / 10%); /*断开连接框的阴影*/
}
.disconnect {
  margin: 16px;
  width: 174px;
  height: 46px;
  background: #c0bdcc;
}
.welcome {
  background: #e64e2e url(../assets/popup_greeting.png) no-repeat 30px 46px;
  width: 512px;
  height: 224px;
  position: relative;
  top: 64px;
  left: 48px;
}
.info {
  background: #f2f2f2;
  padding: 33px; /*距离边框的空白距离*/
  width: 416px;
  height: 272px;
  position: absolute;
  top: 96px;
  left: 176px;
  box-shadow: 0 0 8px rgb(0 0 0 / 10%);
}
.username {
  float: left;
  color: #e64e2e;
  font-family: Helvetica, Arial, sans-serif;
  font-size: 34px;
  width: 164.46px;
  height: 39px;
}
.info_content {
  float: left;
  width: 352px;
  height: 112px;
  margin-top: -8px; /*连接信息与用户名的行距*/
  color: #000000;
}
.label_text {
  clear: left;
  float: left;
  width: 56px;
  height: 32px;
  margin-top: 22px;
  text-align: right;
  font-size: 13px;
}
.english {
  color: #303030;
  font-size: 13px;
}
.content_text {
  float: left;
  margin: 18px 0 0 20px; /*改变时间与流量条的行间距*/
  padding-top: 4px;
  height: 28px;
  font-family: Helvetica, Arial, sans-serif;
  font-size: 28px;
}
#clock {
  color: #ec6677;
}
.usage_bar {
  position: relative;
  float: left;
  margin: 24px 0 0 16px;
  width: 280px;
  height: 32px;
  background: url(../assets/usage_bg.gif) repeat-y;
}
.calibration {
  position: absolute;
  top: -16px;
  right: 14px px;
  font-family: Verdana, Geneva, sans-serif;
  font-size: 13px;
  color: #969696;
  list-style: none; /*去掉li的间隔号*/
  width: 265px;
  height: 32px;
}
.calibration li {
  float: right;
  width: 53px;
  height: 16px;
  text-align: right; /*数字向右对齐*/
}
.triangle {
  position: absolute;
  left: 80px;
  top: 288px;
  border-top: 48px solid #e64e2e;
  border-right: 48px solid transparent;
  border-bottom: 48px solid transparent;
}
.insert {
  position: absolute;
  top: 0;
  right: 4px;
  width: 4px;
  height: 100%;
  background: #f2f2f2;
}
.insert2 {
  position: absolute;
  top: 0;
  right: 12px;
  width: 4px;
  height: 100%;
  background: #f2f2f2;
}
.usage {
  width: 83.5px;
  height: 32px;
  float: left;
  background: #fbb03b;
  font-size: 24px;
  color: #5c5c5c;
  padding-left: 8px;
}
</style>
