// dependency: 
// 
<template>
  <div class="notfound">
    <div v-title data-title="404404404404404404404404404404404404" class="notfound">NotFound</div>
    <go-back />
  </div>
</template>

<script>
  import GoBack from "./GoBack";

  export default {
    name: "NotFound",
    components: {
      GoBack
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