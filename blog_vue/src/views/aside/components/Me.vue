// dependency: 
// 
<template>
  <div id="me">
    <div id="mask">
      <div id="portrait"></div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Me",
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
  #me {
    width: 100%;
    height: auto;
    background-color: #000;
    text-align: center;
    position: relative;
    padding: 7%;
  }
  #mask {
    border-radius: 2000px;
    width: 80%;
    padding-top: 80%;
    height: auto;
    margin: auto;
    background-color: #0f0;
  }
</style>