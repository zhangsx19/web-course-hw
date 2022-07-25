<template>
  <form id="login_form" @submit.prevent="login">
    <div class="field">
      <div class="label_text" for="uname">
        用户名
        <p class="english">User&nbsp;ID</p>
      </div>
      <input type="text" name="username" id="username" v-model="username" />
    </div>
    <div class="field">
      <div class="label_text" for="password">
        密码
        <p class="english">Password</p>
      </div>
      <input type="password" name="password" id="password" v-model="password" />
    </div>
    <button type="submit" name="connect" id="connect" />
  </form>
</template>

<script lang="ts">
import { ref } from "vue";
import $ from "jquery";
export default {
  name: "UploadView",
  components: {},
  setup() {
    let username = ref("");
    let password = ref("");
    const login = () => {
      $.ajax({
        url: "http://127.0.0.1:5000/login",
        type: "POST",
        data: JSON.stringify({
          username: username.value,
          password: password.value,
        }),
        dataType: "json",
        success(resp: any) {
          console.log(resp);
        },
        error() {
          alert("登录失败");
        },
      });
    };
    return {
      login,
    };
  },
};
</script>

