<template>
  <div id="app">
    <blog-header />
    <hr />
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
  html {
    font-size: 14px;
  }
  hr {
    max-width: 1200px;
    width: 80%;
  }

  @media (min-width: 768px) {
    html {
      font-size: 16px;
    }
  }

  .container {
    max-width: 1200px;
  }
</style>
