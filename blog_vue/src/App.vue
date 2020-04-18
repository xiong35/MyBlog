<template>
  <div id="app">
    <blog-header />
    <hr width="70%" />
    <div class="container">
      <div class="row">
        <blog-aside />
        <blog-artical />
      </div>
      <blog-footer />
    </div>
  </div>
</template>

<script>
  import BlogHeader from "views/header/Header";
  import BlogAside from "views/aside/Aside";
  import BlogArtical from "views/body/artical/Artical";
  import BlogFooter from "views/footer/Footer";

  export default {
    name: "App",
    components: {
      BlogHeader,
      BlogAside,
      BlogArtical,
      BlogFooter
    }
  };
</script>

<style>
</style>
