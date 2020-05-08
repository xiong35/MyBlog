<template>
  <div @click="callPartical" id="visiter">
    <scroll class="wrapper" ref="scroll" :probe-type="3">
      <blog-header />
      <hr />
      <div class="container">
        <div class="row ">
          <blog-aside />
          <router-view />
        </div>
        <blog-footer />
      </div>
    </scroll>

    <partical ref="partical"></partical>
    <duck ref="duck" />
    <float-nav />
  </div>
</template>

<script>
  import BlogHeader from "views/header/Header";
  import BlogAside from "views/aside/Aside";
  import BlogArtical from "views/body/artical/Artical";
  import BlogFooter from "views/footer/Footer";

  import Scroll from "@/components/common/scroll/Scroll";
  import Partical from "@/components/common/partical/Partical";
  import Duck from "@/components/common/duck/Duck";
  import FloatNav from "@/components/context/floatNav/FloatNav";

  export default {
    name: "Visiter",
    components: {
      BlogHeader,
      BlogAside,
      BlogArtical,
      BlogFooter,
      Scroll,
      Partical,
      Duck,
      FloatNav
    },
    methods: {
      callPartical(event) {
        this.$refs.partical.fatherClick(event);
      }
    }
  };
</script>

<style>
</style>
