// dependency: 
// 
<template>
  <ul class="list-unstyled">
    <li class="m-3 nav-aside-li" v-for="(item, index) in links" :key="index">
      <div class="nav-aside-div">{{item.name}}</div>
      <div class="x-v"></div>
      <div class="x-h"></div>
      <div class="y-v"></div>
      <div class="y-h"></div>
    </li>
  </ul>
</template>

<script>
  let links = [
    { name: "文章", link: "/artical" },
    { name: "文章", link: "/artical" },
    { name: "文章", link: "/artical" },
    { name: "文章", link: "/artical" }
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
  }
  .x-h,
  .x-v {
    width: 107%;
    height: 100%;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .y-h,
  .y-v {
    width: 100%;
    height: 130%;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
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
    border-color: #007bff;
  }
  .nav-aside-li:hover .y-v {
    height: 100%;
    border-color: #007bff;
  }
  .nav-aside-li:hover .x-v {
    height: 0;
    border-color: #007bff;
  }
  .nav-aside-li:hover .y-h {
    width: 0;
    border-color: #007bff;
  }
  .nav-aside-li:hover .nav-aside-div {
    color: #007bff;
    box-shadow: 0 0 10px #209bff86;
  }
  .nav-aside-div {
    transition: all 0.7s ease;
  }
</style>