<template>
  <el-upload
    action="http://127.0.0.1:5000/project/upload-file"
    multiple
    :headers="header"
    :data="file_info"
    :on-success="upload_success"
  >
    <el-button type="primary">Click to upload</el-button>
  </el-upload>
</template>

<script lang="ts">
export default {
  name: "UploadView",
  components: {},
  data() {
    return {
      header: {
        // "Sec-Fetch-Site": "cross-site",
      },
    };
  },
  computed: {
    file_info() {
      const data = {
        userid: "1",
      };
      return data;
    },
  },
  methods: {
    upload_success(resp: any) {
      console.log(resp);
    },
  },
};
</script>

