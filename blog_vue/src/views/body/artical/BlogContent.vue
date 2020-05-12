// dependency: 
// 
<template>
  <div class="col-12 col-md-9" :key="$route.params.blogId">
    <go-back></go-back>
    <mavon-editor
      class="blog-content"
      :value="blogContent"
      :subfield="false"
      :defaultOpen="'preview'"
      :toolbarsFlag="false"
      :editable="false"
      :codeStyle="'atom-one-dark'"
      :scrollStyle="true"
      :boxShadow="false"
    ></mavon-editor>
  </div>
</template>


<script>
  import { getArtical } from "network/artical";
  import GoBack from "@/components/common/GoBack";

  export default {
    name: "BlogContent",
    components: {
      GoBack
    },
    data() {
      return {
        blogContent: "加载中"
      };
    },
    computed: {},
    watch: {},
    methods: {},
    created() {},
    activated() {
      getArtical(this.$route.params.blogId).then(response => {
        if (response.status != 200) {
          this.$router.replace("/404");
        }
        this.blogContent = response.content.content;
      });
    }
  };
</script>
<style scoped>
  .blog-content {
    z-index: 20 !important;
    width: 100% !important;
  }
</style>