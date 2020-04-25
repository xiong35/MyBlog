// dependency: 
// 
<template>
  <div id="duck">
    <transition name="rotate">
      <img
        src="~assets/img/duck.png"
        alt="a little duck"
        :class="direction"
        :style="style"
        @click="duckClicked"
        v-if="show"
      />
    </transition>
    <!-- <img src="~assets/img/kill_duck.jpg" class="kill" alt="kill duck" /> -->
  </div>
</template>

<script>
  let dir2num = { left: 1, right: -1 };

  export default {
    name: "Duck",
    components: {},
    data() {
      return {
        wanderTimmer: null,
        direction: "left",
        clientX: 10,
        clientY: 10,
        show: true
      };
    },
    computed: {
      style() {
        return {
          top: this.clientY + "px",
          left: this.clientX + "px"
        };
      }
    },
    watch: {
      clientX: function(newX, oldX) {
        if ((newX - oldX) * dir2num[this.direction] < 0) {
          this.direction = this.direction == "left" ? "right" : "left";
        }
      }
    },
    methods: {
      duckClicked() {
        this.direction = "hit";
        clearInterval(this.wanderTimmer);
        setTimeout(() => {
          this.show = false;
        }, 500);
      },
      wander() {
        this.clientY =
          Math.random() * (document.documentElement.clientHeight - 20);
        this.clientX =
          Math.random() * (document.documentElement.clientWidth - 20);
      }
    },
    created() {},
    mounted() {
      this.wander();
      this.wanderTimmer = setInterval(this.wander, 750);
    }
  };
</script>
<style scoped>
  #duck img {
    width: 1.8rem;
    height: 1.8rem;
    transition: all 0.5s;
    cursor: crosshair;
    position: fixed;
    z-index: 7;
  }
  .right {
    transform: rotateY(180deg);
  }
  .hit {
    transform: rotateY(700deg);
    opacity: 0;
  }
  .kill {
    bottom: 40px;
    right: 40px;
    width: 3rem;
    height: 3rem;
  }
</style>