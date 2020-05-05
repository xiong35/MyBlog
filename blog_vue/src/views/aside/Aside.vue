<template>
  <div id="aside" class="d-none d-md-block col-3 pl-5">
    <me></me>
    <hr />
    <nav-aside></nav-aside>
    <!-- <ul class="list-unstyled nav-aside">
      <li>
        <h5>some</h5>
        <ul class="list-unstyled">
          <li class="nl-anim pl-3">主页</li>
          <li class="nl-anim pl-3">哈哈哈</li>
          <li class="nl-anim pl-3">四个字呢</li>
        </ul>
      </li>
      <li>
        <h5>some</h5>
        <ul class="list-unstyled">
          <li class="pl-3 rb-link">asdasd</li>
          <li class="pl-3 rb-link">asdasd</li>
          <li class="pl-3 rb-link">asdasd</li>
        </ul>
      </li>
      <li>
        <h5>some</h5>
        <ul class="list-unstyled">
          <li class="pl-3 rb-link">sgh</li>
          <li class="pl-3 rb-link">sgh</li>
          <li class="pl-3 rb-link">sgh</li>
        </ul>
      </li>
    </ul>-->
  </div>
</template>

<script>
  import Me from "./components/Me";
  import NavAside from "./components/NavAside";
  export default {
    name: "Aside",
    components: {
      Me,
      NavAside
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