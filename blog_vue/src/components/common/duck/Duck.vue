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
        @click="handleClick"
        v-show="show"
      />
    </transition>
  </div>
</template>

<script>
  import { commitKill } from "network/meta";

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
        show: true,
        alive: true,
        wanderTime: 700
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
      },
      "$store.state.duckAlive": function(newState, oldState) {
        if (!newState) {
          this.direction = "hit";
          clearInterval(this.wanderTimmer);
          setTimeout(() => {
            this.show = false;
          }, 500);
        } else {
          this.show = true;
          this.direction = "left";
          setTimeout(() => {
            this.wander();
          }, 20);
          this.wanderTimmer = setInterval(this.wander, this.wanderTime);
        }
        this.alive = !this.alive;
      }
    },
    methods: {
      wander() {
        this.clientY =
          Math.random() * (document.documentElement.clientHeight - 20);
        this.clientX =
          Math.random() * (document.documentElement.clientWidth - 20);
      },
      handleClick() {
        let data = sessionStorage.getItem("duckKilled");
        if (!data) {
          sessionStorage.setItem("duckKilled", 1);
          alert("你抓住了小黄鸭!");
          alert(
            "数据已经提交, 用电脑打开博客, 刷新后可以看到小黄鸭一共被抓住了多少次!"
          );
          data = 0;
        }
        if (data > 9) {
          alert("我忍你很久了啊");
          alert("秘技: 封印!");
          alert("你现在别想和小黄鸭玩耍了!!");
          return;
        }
        sessionStorage.setItem("duckKilled", +data + 1);
        if (data == 2) {
          alert("喂, 你是不是过于残忍了??");
          alert("哦, 我太了解你了, ");
          alert("你杀了这么多小黄鸭只是为了把计分上的次数抬高不是吗???");
          alert("好, 你喜欢玩");
          alert("小黄鸭生气了!!");
          alert("等着瞧吧!!");
          this.wanderTime = 400;
        } else if (data >= 5) {
          alert("好好好");
          alert("你赢了");
          alert("求你放过小黄鸭吧QwQ");
        }
        commitKill();
        this.$store.commit("toggleDuck");
      }
    },
    created() {},
    mounted() {
      this.wander();
      this.wanderTimmer = setInterval(this.wander, this.wanderTime);
    }
  };
</script>
<style scoped>
  #duck img {
    width: 1.8rem;
    height: 1.8rem;
    transition: all 0.7s ease;
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
</style>