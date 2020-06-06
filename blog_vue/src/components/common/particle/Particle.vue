// dependency: 
// font-awesome
<template>
  <div class="particle">
    <div
      v-for="(item, index) in particles"
      :key="index"
      :style="{top:item.top+'px',left:item.left+'px',fontSize:item.fontSize}"
    >
      <span>.</span>
    </div>
  </div>
</template>

<script>
  let V = 10;
  let interval = 10;
  let G = 0.3;
  let particleNum = 14;
  let duringTime = 1000;

  export default {
    name: "Particle",
    components: {},
    data() {
      return {
        click: { x: 0, y: 0 },
        particles: [],
        spreadTimer: null,
        spreader: 0
      };
    },
    computed: {},
    watch: {},
    methods: {
      fatherClick(event) {
        let x = event.clientX -2;
        let y = event.clientY - 25;
        let added = 0;
        while (added < particleNum) {
          let vx = (Math.random() - 0.5) * V;
          let vy = (Math.random() - 0.84) * V;
          let fontSize = (Math.random() + 0.28) * 35 + "px";
          let curParticle = { top: y, left: x, fontSize, vx, vy };
          this.particles.push(curParticle);
          added++;
        }
        this.spread();
      },
      spread() {
        this.clear();
        this.spreader++;
        this.spreadTimer = setInterval(() => {
          this.particles.forEach(item => {
            item.vy += G;
            item.top += item.vy;
            item.left += item.vx;
          });
        }, interval);
        setTimeout(index => {
          this.spreader--;
          if (this.spreader == 0) {
            this.clear();
          }
          this.particles.splice(0, particleNum);
          this.isSpreading = false;
        }, duringTime);
      },
      clear() {
        if (this.spreadTimer) {
          clearInterval(this.spreadTimer);
          this.spreadTimer = null;
        }
      }
    },
    created() {},
    mounted() {}
  };
</script>
<style scoped>
  div {
    position: fixed;
    -moz-user-select: none;
    -khtml-user-select: none;
    user-select: none;
  }
</style>