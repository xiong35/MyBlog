// dependency: 
// 
<template>
  <ul class="list-unstyled nav-aside pl-4 pt-2">
    <li v-for="(item, index) in links" :key="index">
      <h4 class="nav-class" href="item.href">{{item.name}}</h4>
      <ul>
        <li
          v-for="(navItem, index) in item.items"
          v-show="navItem.show"
          :href="navItem.href"
          :key="index"
        >{{navItem.name}}</li>
      </ul>
    </li>
  </ul>
</template>

<script>
  let links = [
    {
      name: "xxx",
      href: "#",
      items: [
        { name: "iiiii", href: "#", show: true },
        { name: "iiiii", href: "#", show: false },
        { name: "iiiii", href: "#", show: true }
      ]
    },
    {
      name: "xxx",
      href: "#",
      items: [
        { name: "iiiii", href: "#", show: true },
        { name: "iiiii", href: "#", show: true },
        { name: "iiiii", href: "#", show: true },
        { name: "iiiii", href: "#", show: true }
      ]
    },
    {
      name: "xxx",
      href: "#",
      items: [
        { name: "iiiii", href: "#", show: true },
        { name: "iiiii", href: "#", show: true },
        { name: "iiiii", href: "#", show: true }
      ]
    },
    {
      name: "xxx",
      href: "#",
      items: [
        { name: "iiiii", href: "#", show: true },
        { name: "iiiii", href: "#", show: true },
        { name: "iiiii", href: "#", show: true }
      ]
    }
  ];
  export default {
    name: "NavAside",
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
  .nav-item:before {
    content: " - ";
  }
</style>