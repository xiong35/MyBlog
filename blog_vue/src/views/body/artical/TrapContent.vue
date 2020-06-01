// dependency: 
// 
<template>
  <div class="col-12 col-md-9" :key="$route.params.trapId+'trap'">
    <go-back></go-back>
    <mavon-editor
      class="blog-content"
      :value="trap.solution"
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
  import { getarticle } from "network/article";
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
    },
    watch: {},
    methods: {},
    created() {},
    activated() {
      getarticle(this.$route.params.trapId, "trap").then(response => {
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
    z-index: 20 !important;
  }
</style>