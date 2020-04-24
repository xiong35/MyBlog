// dependency: 
// better scroll, font-awesome
<template>
  <ul class="floatnav list-unstyled">
    <li>
      <div class="nav-item">
        <i class="fa fa-bars"></i>
      </div>
    </li>
    <li>
      <div class="nav-item">
        <img src="~assets/img/kill_duck.jpg" @click="$emit('kill-duck')" alt="kill duck" />
      </div>
    </li>
    <li>
      <div class="nav-item" @click="$emit('totop')">
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
    height: 2.5rem;
    width: 2.5rem;
    text-align: center;
    margin: 0.5vmin;
    border-radius: 2px;
    background-image: linear-gradient(49deg, #3aaef19f -14%, #d93eeea2 114%);
    animation: hue 3s infinite linear;
  }
  @keyframes hue {
    0% {
      filter: hue-rotate(0deg);
    }
    100% {
      filter: hue-rotate(-360deg);
    }
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