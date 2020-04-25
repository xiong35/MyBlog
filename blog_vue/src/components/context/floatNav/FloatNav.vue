// dependency: 
// better scroll, font-awesome
<template>
  <ul class="floatnav list-unstyled">
    <li>
      <div class="nav-item" @click="$emit('toggle-f-nav')">
        <i class="fa fa-bars"></i>
      </div>
    </li>
    <li>
      <div class="nav-item">
        <img src="~assets/img/kill_duck.png" @click="$emit('kill-duck')" alt="kill duck" />
      </div>
    </li>
    <li>
      <div class="nav-item" @click="$emit('to-top')">
        <i class="fa fa-angle-double-up"></i>
      </div>
    </li>
  </ul>
</template>

<script>
  export default {
    name: "FloatNav",
    components: {},
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
  ul {
    position: fixed;
    right: 4vmin;
    bottom: 3vmin;
  }
  li {
    height: 2.1rem;
    width: 2.1rem;
    text-align: center;
    position: relative;
    background-color: rgba(255, 255, 255, 0.7);
    margin: 0.2rem;
    border-radius: 2px;
    border: solid 1px;
    transition: all 0.3s ease;
  }
  li:hover {
    background-color: rgba(0, 0, 0, 0.8);
    color: #fff;
  }
  .nav-item {
    width: 80%;
    height: 80%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  i {
    font-size: 1.2rem;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  img {
    width: 100%;
    height: 100%;
  }
</style>