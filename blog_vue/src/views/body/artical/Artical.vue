<template>
  <div class="col-12 col-md-9" id="artical">
    <h2>tdfkhtfk</h2>
    <p class="text-left text-wrap">
      aseekt dkcuydrf gaseekt dkcuy dr fga seek tdkcuyd rfgvvvv aseekt dkcuydr f g vvva
      seektd k cuydr fg
    </p>
    <h2>tdfkhtfk</h2>
    <p class="text-left text-wrap">
      aseekt dkcuydrf gaseekt dkcuy dr fga seek tdkcuyd rfgvvvv aseekt dkcuydr f g vvva
      seektd k cuydr fg
    </p>
    <h2>tdfkhtfk</h2>
    <p class="text-left text-wrap">
      aseekt dkcuydrf gaseekt dkcuy dr fga seek tdkcuyd rfgvvvv aseekt dkcuydr f g vvva
      seektd k cuydr fg
    </p>
    <h2>tdfkhtfk</h2>
    <p class="text-left text-wrap">
      aseekt dkcuydrf gaseekt dkcuy dr fga seek tdkcuyd rfgvvvv aseekt dkcuydr f g vvva
      seektd k cuydr fg
    </p>
    <h2>tdfkhtfk</h2>
    <p class="text-left text-wrap">
      aseekt dkcuydrf gaseekt dkcuy dr fga seek tdkcuyd rfgvvvv aseekt dkcuydr f g vvva
      seektd k cuydr fg
    </p>
    <h2>tdfkhtfk</h2>
    <p class="text-left text-wrap">
      aseekt dkcuydrf gaseekt dkcuy dr fga seek tdkcuyd rfgvvvv aseekt dkcuydr f g vvva
      seektd k cuydr fg
    </p>
    <h2>tdfkhtfk</h2>
    <p class="text-left text-wrap">
      aseekt dkcuydrf gaseekt dkcuy dr fga seek tdkcuyd rfgvvvv aseekt dkcuydr f g vvva
      seektd k cuydr fg
    </p>
  </div>
</template>

<script>
  import { getBlog } from "network/artical";

  export default {
    name: "Artical",
    components: {},
    data() {
      return {};
    },
    computed: {},
    watch: {},
    methods: {},
    created() {
      getBlog().then(response => {
        console.log(response);
      });
    },
    mounted() {}
  };
</script>
<style scoped>
</style>