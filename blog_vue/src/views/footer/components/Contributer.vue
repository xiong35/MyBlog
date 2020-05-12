// dependency: 
// bootstrap
<template>
  <div class="col-6 col-md-3" id="contributer">
    <h5>Contributers</h5>
    <table class="table mt-3">
      <tbody>
        <tr v-for="(info, duty, index) in contributers" :key="index">
          <td>{{duty}}</td>
          <td>
            <a :href="info.link" class="text-secondary">{{info.name}}</a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  let xiong35 = {
    name: "xiong35",
    link: "http://101.133.217.104/"
  };
  export default {
    name: "Contributer",
    components: {},
    data() {
      return {
        contributers: {
          PM: xiong35,
          UI: xiong35,
          前端: xiong35,
          后端: xiong35,
          运维: xiong35
        }
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
</style>