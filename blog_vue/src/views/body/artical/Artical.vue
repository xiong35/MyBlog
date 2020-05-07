<template>
  <div class="col-12 col-md-9" id="artical">
    <ul class="nav nav-tabs my-2">
      <li class="nav-item">
        <big class="nav-link active" href="#">文章</big>
      </li>
      <li class="nav-item">
        <big class="nav-link" href="#">踩坑记录</big>
      </li>
    </ul>

    <ul class="tag-list my-2 p-3 list-inline">
      <li class="list-inline-item tag">2333</li>
      <li class="list-inline-item tag">2333</li>
      <li class="list-inline-item tag">2333</li>
      <li class="list-inline-item tag">2333</li>
      <li class="list-inline-item tag toggle-tags">toggle</li>
    </ul>
    <div class="headlines">
      <blog></blog>
    </div>
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
  }
  .nav-tabs,
  .tag-list {
    width: 90%;
    margin: auto;
  }
  .tag {
    border: solid 1px #000;
    border-radius: 2000px;
    text-align: center;
    padding: 2px 10px 4px 10px;
    transition: all 0.3s ease;
    cursor: pointer;
  }
  .tag:hover {
    box-shadow: 0 0 5px #007bff71;
    background-color: #0da5fd;
    color: #fff;
    border-color: #0da5fd;
  }
  .nav-item {
    cursor: pointer;
  }
</style>