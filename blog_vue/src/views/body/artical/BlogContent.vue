// dependency: 
// 
<template>
  <div class="blogcontent">
    <mavon-editor
      class="markdown"
      :value="content"
      :subfield="false"
      :defaultOpen="'preview'"
      :toolbarsFlag="false"
      :editable="false"
      :codeStyle="'atom-one-dark'"
      :scrollStyle="true"
    ></mavon-editor>
  </div>
</template>


<script>
  import { getBlog } from "network/artical";

  export default {
    name: "BlogContent",
    components: {},
    data() {
      return {
        blogContent: "加载中",
        content: `
  # pap

  ### pakdc

  **fwsoigfwf**sdvoiuhbosd

  \`\`\`python
  a = dict()
  b = "dskjfvhb"

  class aaa(adf):
      def __init__(self):
          self.num = 124254 + 9857

      def dada(self):
          return 666
  \`\`\`
                      `
      };
    },
    computed: {},
    watch: {},
    methods: {
      changeData(value, render) {
        console.log(value);
        console.log(render);
        this.contentHtml = render;
      }
    },
    created() {},
    mounted() {
      getBlog(this.$route.params.blogId).then(response => {
        this.blogContent = response.content.content;
      });
    }
  };
</script>
<style scoped>
  .markdown {
    width: 50vw !important;
  }
</style>