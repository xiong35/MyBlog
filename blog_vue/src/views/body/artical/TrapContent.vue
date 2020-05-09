// dependency: 
// 
<template>
  <div class="col-12 col-md-9">
    <go-back></go-back>
    <mavon-editor
      class="blog-content"
      :value="trapContent"
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
    name: "TrapContent",
    components: {
      GoBack
    },
    data() {
      return {
        trap: {}
      };
    },
    computed: {
      trapContent() {
        return `## ${this.trap.context}\n### ${this.trap.problem}\n---\n${this.trap.solution}`;
      }
    },
    watch: {},
    methods: {},
    created() {},
    mounted() {
      getArtical(this.$route.params.trapId, "trap").then(response => {
        if (response.status != 200) {
          this.$router.replace("/404");
        }
        this.trap = response.data;
      });
    }
  };
</script>
<style scoped>
  .blog-content {
    width: 100% !important;
  }
</style>