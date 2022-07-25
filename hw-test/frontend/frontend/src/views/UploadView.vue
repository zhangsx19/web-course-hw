<template>
  <el-upload action="http://localhost:5000/upload-file" multiple method="POST">
    <el-button type="primary">Click to upload</el-button>
  </el-upload>
</template>

<script lang="ts">
export default {
  name: "UploadView",
  components: {},
};
</script>

