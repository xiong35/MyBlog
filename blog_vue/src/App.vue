// dependency: 
// 
<template>
  <div class="app">
    <router-view></router-view>
  </div>
</template>

<script>
  export default {
    name: "App",
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
<style>
  html {
    font-size: 14px;
  }
  hr {
    max-width: 1200px;
    width: 80%;
  }

  @media (min-width: 768px) {
    html {
      font-size: 16px;
    }
  }

  .container {
    max-width: 1200px;
  }
  ::selection {
    color: #ffffff;
    background-color: #41afee;
    text-shadow: none;
  }
  ::-moz-selection {
    color: #ffffff;
    background-color: #41afee;
    text-shadow: none;
  }
  ::-webkit-selection {
    color: #ffffff;
    background-color: #41afee;
    text-shadow: none;
  }
</style>