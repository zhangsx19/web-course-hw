<template>
  <div>
    <div :style="{ height: height, width: width }" :id="id" class="chart"></div>
  </div>
</template>
<script>
// 引入echarts
import * as echarts from "echarts";
export default {
  name: "EchartsBase",
  props: {
    height: {
      type: String,
      default: "500px",
    },
    width: {
      type: String,
      default: "1500px",
    },
    id: {
      type: String,
      default: "usage",
    },
  },
  data() {
    return {
      timeData: [],
      valueData: [],
      usage: 1000, //起始流量
    };
  },
  mounted() {
    setInterval(() => {
      this.refreshchart();
    }, 2000);
  },
  methods: {
    drawLine() {
      var chartDom = document.getElementById(this.id); //id调用的template里的
      var myChart = echarts.init(chartDom); // 基于chartdom，初始化echarts实例
      // 绘制图表
      var option = {
        title: { text: "流量使用情况" },
        tooltip: {
          trigger: "axis",
        },
        xAxis: {
          type: "category",
          data: this.timeData,
          axisTick: {
            alignWithLabel: true, //让刻度对齐x轴下方标签
          },
        },
        yAxis: { type: "value" },
        series: [
          {
            type: "line",
            color: "purple", //设定实线点的颜色
            itemStyle: {
              normal: {
                lineStyle: {
                  color: "purple", //设置实线的颜色
                },
              },
            },
            data: this.valueData,
          },
        ],
      };
      myChart.setOption(option); //设置准备好的选项
    },
    addZero(i) {
      if (i < 10) {
        i = "0" + i;
      }
      return i;
    },
    refreshchart() {
      var date = new Date();
      var curHour = this.addZero(date.getHours());
      var curMinutes = this.addZero(date.getMinutes());
      var curSeconds = this.addZero(date.getSeconds());
      var curtime = curHour + ":" + curMinutes + ":" + curSeconds;
      // 获取完数据，延迟0.1秒执行图表
      if (this.timeData.length >= 9) {
        setTimeout(() => {
          this.drawLine();
        }, 100);
        //执行完图表后更新下一次数据
        for (var i = 0; i < 8; i++) {
          this.timeData[i] = this.timeData[i + 1];
          this.valueData[i] = this.valueData[i + 1];
        }
        this.timeData[i] = curtime;
        this.valueData[i] = this.usage;
      } else {
        this.timeData.push(curtime);
        this.valueData.push(this.usage);
      }
      this.usage += Math.floor(Math.random() * 290 + 10); //10-300随机数
    },
  },
};
</script>
<style scoped>
.chart {
  margin: auto;
}
</style>