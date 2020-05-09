// dependency: 
// font-awesome
<template>
  <ul class="floatnav list-unstyled">
    <li @click="$emit('toggle-f-nav')">
      <div class="nav-item">
        <i class="fa fa-bars"></i>
      </div>
    </li>
    <li @click="toggleDuck" :class="{'kill-duck':$store.state.duckAlive}">
      <div class="nav-item">
        <transition name="toggle" mode="out-in">
          <img
            v-if="$store.state.duckAlive"
            src="~assets/img/kill_duck.png"
            key="kill"
            alt="kill duck"
          />
          <img v-else src="~assets/img/duck.png" key="summon" alt="summon duck" />
        </transition>
      </div>
    </li>
    <li @click="$store.dispatch('scrollTo')">
      <div class="nav-item">
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
    methods: {
      toggleDuck() {
        this.$store.commit("toggleDuck");
      }
    },
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
    border: solid 1px #007bff;
    color: #007bff;
    box-shadow: 0 0 3px #007bff66;
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
  .kill-duck:hover {
    border: solid 1px #e93342;
    box-shadow: 0 0 3px #e933428f;
  }
  .toggle-enter-active,
  .toggle-leave-active {
    transition: opacity 0.2s;
  }
  .toggle-enter,
  .toggle-leave-to {
    opacity: 0;
  }
</style>