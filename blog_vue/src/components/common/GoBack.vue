// dependency: 
// font-awesome
<template>
  <div class="p-1">
    <h5 class="m-2 text-secondary" @click="$router.back()">
      <i class="fa fa-angle-double-left"></i> 返回
    </h5>
  </div>
</template>

<script>
  export default {
    name: "GoBack",
    components: {},
    data() {
      return {};
    }
  };
</script>
<style scoped>
  h5:hover {
    color: #006ee4 !important;
    transition: all 0.3s ease;
  }
  h5 {
    transition: all 0.3s ease;
    cursor: pointer;
  }
</style>