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
  #artical ul {
    margin: 0;
  }
  .blog-brief {
    width: 95%;
    height: auto;
    margin: auto;
    border-bottom: solid 1px #6c757d;
    position: relative;
  }
  .blog-brief:last-child {
    border-bottom: none;
  }
  .time {
    width: 100%;
    height: auto;
    margin: auto;
    position: relative;
    text-align: right;
  }
  .tag {
    border: solid 1px #000;
    border-radius: 2000px;
    text-align: center;
    padding: 2px 10px 4px 10px;
  }
  .blog-trap {
    height: 4rem;
    width: 100%;
    margin: auto;
    border-bottom: solid 1px #000;
  }
  .headlines {
  }
</style>