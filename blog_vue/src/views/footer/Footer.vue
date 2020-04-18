<template>
  <footer class="pt-4 my-md-5 pt-md-5 border-top" style="width: 80%;margin: auto;">
    <div class="row">
      <contributer />
      <comment />
      <contact-me />
    </div>
    <p class="small text-muted text-center">
      <i class="fa fa-copyright"></i> 2019-2020
    </p>
  </footer>
</template>

<script>
  import Contributer from "./components/Contributer";
  import Comment from "./components/Comment";
  import ContactMe from "./components/ContactMe";

  export default {
    name: "Footer",
    components: {
      Contributer,
      Comment,
      ContactMe
    },
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
</style>