// dependency:
// font-awesome, bootstrap
<template>
  <div class="col-6 col-md-3 icon">
    <h5 class="pb-2">Social</h5>
    <ul class="list-unstyled text-justify" id="social">
      <li v-for="(item, index) in linkList" :key="index" class="m-2">
        <a v-if="item.link" :href="item.link" class="text-body">
          <i :class="item.iclass" class="fa"></i>
        </a>
        <i v-else :class="item.iclass" @click="iconClick($event,item)" class="fa"></i>
        <transition name="fade" v-if="item.img">
          <img v-show="item.show" :src="item.img" class="bin_code img-thumbnail" alt="二维码" />
        </transition>
      </li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: "ContactMe",
    components: {},
    data() {
      return {
        linkList: [
          {
            iclass: "fa-github",
            link: "https://github.com/xiong35",
            img: null,
            show: false
          },
          {
            iclass: "fa-qq",
            link: null,
            img: require("assets/img/q.jpg"),
            show: false
          },
          {
            iclass: "fa-weixin",
            link: null,
            img: require("assets/img/v.jpg"),
            show: false
          }
        ]
      };
    },
    computed: {},
    watch: {},
    methods: {
      iconClick(event, item) {
        if (item.show) {
          item.show = false;
          return;
        }
        this.linkList.forEach(curLink => {
          if (!curLink.link) {
            curLink.show = false;
          }
        });
        item.show = true;
      }
    },
    created() {},
    mounted() {}
  };
</script>
<style scoped>
  #social li {
    display: inline;
    font-size: 1.6rem;
  }

  .bin_code {
    display: block;
    width: 200px;
    height: 200px;
    margin: auto;
    position: absolute;
    max-width: none;
    top: -170px;
  }
  @media (min-width: 768px) {
    .bin_code {
      top: 91px;
    }
  }
  .fade-enter-active,
  .fade-leave-active {
    transition: all 0.3s ease;
  }
  .fade-enter,
  .fade-leave-to {
    transform: translateX(10px);
    opacity: 0;
  }
</style>