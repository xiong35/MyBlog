<template>
  <div class="col-6 col-md-3 icon" id="contact-me">
    <h5 class="pb-2 text-secondary">Social</h5>
    <ul class="list-unstyled text-justify">
      <li v-for="(item, index) in linkList" :key="index">
        <a v-if="item.link" :href="item.link">
          <i :class="item.iclass" class="fa"></i>
        </a>
        <i v-else :class="item.iclass" class="fa"></i>
        <img v-if="item.img" v-show="item.show" :src="item.img" alt="二维码" />
      </li>
      <!-- <li>
        <a href="https://github.com/xiong35">
          <i
            class="fa text-secondary fa-github m-2"
            style="font-size:1.9rem;transform: translateY(2px);"
          ></i>
        </a>
      </li>
      <li>
        <i class="fa text-secondary fa-qq m-2" style="font-size:1.6rem"></i>
        <img src="q.jpg" alt="qq二维码" class="img-thumbnail bin_code" />
      </li>
      <li>
        <i class="fa text-secondary fa-weixin m-2" style="font-size:1.6rem"></i>
        <img style="display: none;" src="v.jpg" alt="微信二维码" class="img-thumbnail bin_code" />
      </li>-->
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
    methods: {},
    created() {},
    mounted() {}
  };
</script>
<style scoped>
</style>