<template>
  <div id="aside" class="d-none d-md-block col-3">
    <me></me>
    <blog-meta></blog-meta>
    <hr />
    <nav-aside></nav-aside>
  </div>
</template>

<script>
  import Me from "./components/Me";
  import NavAside from "./components/NavAside";
  import BlogMeta from "./components/Meta";

  export default {
    name: "Aside",
    components: {
      Me,
      NavAside,
      BlogMeta
    },
    data() {
      return {};
    },
    computed: {},
    watch: {},
    methods: {},
    created() {},
    mounted() {}
  };
</script>
<style scoped>
  #aside {
    position: relative;
  }
</style>