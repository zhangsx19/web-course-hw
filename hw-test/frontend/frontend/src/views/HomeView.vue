<template>
  <div>
    <!-- <el-button type="primary">el-button</el-button> -->
    <el-tree :data="data" @node-click="handleNodeClick" />
  </div>
</template>

<script>
import $ from "jquery";
export default {
  name: "HomeView",
  components: {},
  data() {
    return {
      data: [
        {
          label: "Level one 1",
          children: [
            {
              label: "Level two 1-1",
              children: [],
            },
          ],
        },
      ],
    };
  },

  setup() {
    const handleNodeClick = (data) => {
      console.log(data);
    };
    return {
      handleNodeClick,
    };
  },
  mounted() {
    setTimeout(() => {
      this.refreshlist();
    }, 2000);
  },
  methods: {
    refreshlist() {
      $.ajax({
        url: "http://127.0.0.1:5000/project/list-files",
        type: "POST",
        data: JSON.stringify({
          userid: "1",
          projectid: "a",
        }),
        dataType: "json",
        success: (resp) => {
          // console.log(resp);
          this.data = [];
          this.data.push(resp);
          console.log(this.data);
        },
      });
    },
  },
};
</script>

