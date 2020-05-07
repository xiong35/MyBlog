<template>
  <div class="wrapper" ref="wrapper">
    <div class="content" ref="content">
      <slot></slot>
    </div>
  </div>
</template>

<script>
  import BScroll from "better-scroll";
  export default {
    name: "Scroll",
    components: {},
    props: {
      probeType: {
        type: Number,
        default: 0
      }
    },
    data() {
      return {};
    },
    mounted() {
      let scrollManager = new BScroll(this.$refs.wrapper, {
        scrollY: true,
        click: true,
        probeType: this.probeType,
        mouseWheel: true,
        preventDefault: false,
        bounceTime: 400
      });
      this.$store.commit("setScroll", scrollManager);
      // this.scrollManager.on("scroll", position => {
      //   // emit an event with postion : {x: , y: }
      //   this.$emit("scroll", position);
      // });
    },
    methods: {}
  };
</script>
<style scoped>
  .wrapper {
    height: 100vh;
    overflow: hidden;
  }
</style>