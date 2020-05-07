// dependency: 
// 
<template>
  <div class="blogcontent">{{blogContent}}</div>
</template>

<script>
  import { getBlog } from "network/artical";

  export default {
    name: "BlogContent",
    components: {},
    data() {
      return {
        blogContent: "加载中"
      };
    },
    computed: {},
    watch: {},
    methods: {},
    created() {},
    mounted() {
      getBlog(this.$route.params.blogId).then(response => {
        this.blogContent = response.content.content;
      });
    }
  };
</script>
<style scoped>
</style>