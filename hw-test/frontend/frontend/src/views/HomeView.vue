<template>
  <div>
    <!-- <el-button type="primary">el-button</el-button> -->
    <el-tree :data="data" @node-click="handleNodeClick" />
  </div>
</template>

<script>
import axios from "axios";
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
    list2tree(files) {
      var tree_arr = [];
      for (var i = 0; i < files.length; i++) {
        var tree = {};
        tree["label"] = files[i]["name"];
        if (files[i]["folder"] == 1) {
          tree["children"] = this.list2tree(files[i]["files"]);
        }
        tree_arr.push(tree);
      }
      return tree_arr;
    },
    refreshlist() {
      axios
        .post(
          "http://127.0.0.1:4523/m1/1454888-0-default/project/list-files",
          JSON.stringify({
            session: "1",
            project: "a",
          })
        )
        .then((resp) => {
          resp = resp["data"];
          console.log(resp);
          this.data = [];
          if (resp["code"] == 0) {
            this.data = this.list2tree(resp["files"]);
          } else if (resp["code"] == 1) {
            alert("session无效");
          } else if (resp["code"] == 2) {
            alert("session无效");
          } else {
            alert("未知错误");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>

