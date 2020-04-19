// dependency: 
// font-awesome
<template>
  <div class="partical">
    <div
      v-for="(item, index) in particals"
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
  let particalNum = 14;

  export default {
    name: "Partical",
    components: {},
    data() {
      return {
        click: { x: 0, y: 0 },
        particals: [],
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
        console.log(x, y);
        let added = 0;
        while (added < particalNum) {
          let vx = (Math.random() - 0.5) * V;
          let vy = (Math.random() - 0.8) * V;
          let fontSize = (Math.random() + 0.28) * 35 + "px";
          let curPartical = { top: y, left: x, fontSize, vx, vy };
          this.particals.push(curPartical);
          added++;
        }
        this.spread();
      },
      spread() {
        this.clear();
        this.spreader++;
        this.spreadTimer = setInterval(() => {
          this.particals.forEach(item => {
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
          this.particals.splice(0, particalNum);
          this.isSpreading = false;
        }, 700);
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