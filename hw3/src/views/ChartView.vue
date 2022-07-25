<template>
  <!--实际为html的body,但vue中的body无法跨域引用图片，所以要另外定义popup-->
  <div class="whole">
    <!--居中显示-->
    <EchartsBase :width="width" :height="height" :id="id"></EchartsBase>
  </div>
</template>

<script>
import EchartsBase from "../components/EchartsBase";
export default {
  name: "ChartView",
  components: {
    EchartsBase,
  },
};
</script>

<style scoped>
* {
  font-family: "Microsoft YaHei", "SimHei", "Apple LiGothic Medium";
  margin: auto;
  padding: 0px;
}
</style>
