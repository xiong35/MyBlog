// dependency: 
// 
<template>
  <ul class="list-unstyled">
    <li class="m-3 nav-aside-li" v-for="(item, index) in links" :key="index">
      <div class="x-v"></div>
      <div class="x-h"></div>
      <div class="y-v"></div>
      <div class="y-h"></div>
      <router-link tag="div" class="nav-aside-div" :to="item.link">{{item.name}}</router-link>
    </li>
  </ul>
</template>

<script>
  let links = [
    { name: "文章", link: "/article" },
    { name: "简历", link: "/resume" },
    { name: "关于我", link: "/profile" },
    { name: "作品", link: "/works" }
  ];
  export default {
    name: "NavAside",
    components: {},
    data() {
      return {
        links
      };
    },
    computed: {},
    watch: {},
    methods: {},
    created() {},
    mounted() {}
  };
</script>
<style scoped>
  ul {
    text-align: center;
  }
  li {
    display: inline-block;
    width: 80%;
    margin: auto;
    line-height: 3rem;
    position: relative;
    cursor: pointer;
  }
  .x-v,
  .y-v,
  .x-h,
  .y-h {
    position: absolute;
    border-width: 1px;
    border-color: #000;
    transition: all 0.5s ease;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: -1;
  }
  .x-v {
    width: 107%;
    height: 90%;
  }
  .x-h {
    width: 104%;
    height: 100%;
  }
  .y-v {
    width: 100%;
    height: 123%;
  }
  .y-h {
    width: 90%;
    height: 130%;
  }
  .x-v,
  .y-v {
    border-style: none solid;
  }
  .x-h,
  .y-h {
    border-style: solid none;
  }
  .nav-aside-li:hover .x-h {
    width: 100%;
  }
  .nav-aside-li:hover .y-v {
    height: 100%;
  }
  .nav-aside-li:hover .x-v {
    height: 0;
  }
  .nav-aside-li:hover .y-h {
    width: 0;
  }
  .nav-aside-li:hover .x-h,
  .nav-aside-li:hover .y-v,
  .nav-aside-li:hover .x-v,
  .nav-aside-li:hover .y-h {
    border-color: #007bff;
  }
  .nav-aside-li:hover .x-h,
  .nav-aside-li:hover .y-v {
    border-color: #007bff;
    border-radius: 5px;
  }
  .nav-aside-li:hover .nav-aside-div {
    color: #007bff;
    box-shadow: 0 0 7px #209bff86;
  }
  .nav-aside-div {
    transition: all 0.7s ease;
  }
</style>