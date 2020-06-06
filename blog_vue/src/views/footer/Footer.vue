// dependency: // font-awesome, bootstrap
<template>
  <footer class="pt-4 my-md-5 pt-md-5 border-top">
    <div class="row">
      <contributer />
      <recommend />
      <social />
      <license />
    </div>
    <p class="small text-muted text-center p-2">
      <i class="fa fa-copyright"></i> 2019-2020
      <br />
      <span>
        用
        <a
          class="text-secondary"
          href="https://www.google.cn/intl/zh-CN/chrome/"
          >谷歌浏览器</a
        >浏览效果最佳
      </span>
    </p>
  </footer>
</template>

<script>
  import Contributer from "./components/Contributer";
  import Recommend from "./components/Recommend";
  import License from "./components/License";
  import Social from "./components/Social";

  export default {
    name: "Footer",
    components: {
      Contributer,
      License,
      Social,
      Recommend,
    },
    data() {
      return {};
    },
    computed: {},
    watch: {},
    methods: {},
    created() {},
    mounted() {},
  };
</script>
<style scoped></style>
