<template>
  <div id="header" class="px-3 py-2 pt-md-4 pb-md-3 mx-auto text-center">
    <h1 class="display-1 heading">{{$route.path.split('/')[1]}}</h1>
  </div>
</template>

<script>
  export default {
    name: "Header",
    components: {},
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