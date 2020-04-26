// dependency: 
// 
<template>
  <div id="me">
    <div id="border-circle">
      <div id="rotate-box">
        <div id="mask-circle"></div>
      </div>
    </div>
    <img id="portrait" src="~assets/img/portrait.jpg" alt="portrait" />
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
    background-color: rgb(255, 255, 255);
    text-align: center;
    position: relative;
    padding: 8%;
  }
  #border-circle {
    border-radius: 2000px;
    width: 8vw;
    height: 8vw;
    margin: auto;
    background-color: #fff;
    border: 1px solid #000;
    padding: 0.5vw;
  }
  #rotate-box {
    background-color: rgb(0, 0, 0);
    width: 100%;
    height: 100%;
    border: #fff solid 0.38vw;
    animation: rotate 3s infinite linear;
  }
  @keyframes rotate {
    0% {
      transform: rotate(0deg);
    }
    25% {
      transform: rotate(90deg);
    }
    38% {
      transform: rotate(180deg);
    }
    63% {
      transform: rotate(270deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
  #mask-circle {
    background-color: rgb(255, 255, 255);
    width: 100%;
    height: 100%;
    border-radius: 2000px;
    transform: scale(1.27, 1.27);
    -webkit-transform: scale(1.27, 1.27);
    -ms-transform: scale(1.27, 1.27);
    -moz-transform: scale(1.27, 1.27);
    -o-transform: scale(1.27, 1.27);
  }
  #portrait {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 7vw;
    height: 7vw;
    border-radius: 2000px;
  }
</style>