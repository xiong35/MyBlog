// dependency: 
// 
<template>
  <div class="recommend col-6 col-md-3">
    <h5>Recommends</h5>
    <hr />
    <ul class="list-unstyled">
      <li class="p-2 link-out text-secondary" v-for="(item, index) in links" :key="index">
        <h6>
          <a class="text-secondary" :href="item.href">{{item.name}}</a>
        </h6>
        <small>{{item.discription}}</small>
      </li>
    </ul>
  </div>
</template>

<script>
  let links = [
    {
      name: "Jaya's Blog",
      discription: "主业研究Unity, 副业啥都学的漂亮姐姐的博客, 快去踩踩吧👆",
      href: "http://39.102.64.20/"
    }
  ];
  export default {
    name: "Recommend",
    components: {},
    data() {
      return {
        links
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
  .link-out {
    box-shadow: 1px 1px 3px #c9c9c986;
    transition: all 0.3s;
  }
  .link-out:hover {
    box-shadow: 1px 1px 5px #aaaaaa86;
    transform: translate(-2px, -2px);
  }
</style>