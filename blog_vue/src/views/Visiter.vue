<template>
  <div @click="callParticle" id="visiter">
    <blog-header />
    <hr />
    <div class="container">
      <div class="row">
        <blog-aside />
        <keep-alive>
          <router-view />
        </keep-alive>
      </div>
      <blog-footer />
    </div>

    <particle ref="particle"></particle>
    <duck ref="duck" />
    <float-nav />
  </div>
</template>

<script>
  import BlogHeader from "views/header/Header";
  import BlogAside from "views/aside/Aside";
  import Blogarticle from "views/body/article/Article";
  import BlogFooter from "views/footer/Footer";

  import Particle from "@/components/common/particle/Particle";
  import Duck from "@/components/common/duck/Duck";
  import FloatNav from "@/components/context/floatNav/FloatNav";

  export default {
    name: "Visiter",
    components: {
      BlogHeader,
      BlogAside,
      Blogarticle,
      BlogFooter,
      Particle,
      Duck,
      FloatNav
    },
    methods: {
      callParticle(event) {
        this.$refs.particle.fatherClick(event);
      }
    }
  };
</script>

<style>
</style>
