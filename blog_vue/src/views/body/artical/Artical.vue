<template>
  <div class="col-12 col-md-9" id="artical">
    <div class="blog-trap"></div>
    <div class="headlines">
      <blog></blog>
    </div>
    <div class="sweeper"></div>
  </div>
</template>

<script>
  import Blog from "./Blog";
  import Trap from "./Trap";

  export default {
    name: "Artical",
    components: {
      Blog,
      Trap
    },
    data() {
      return {};
    },
    computed: {},
    watch: {},
    methods: {},
    mounted() {}
  };
</script>
<style>
  #artical {
    width: 100%;
    margin: auto;
  }
</style>