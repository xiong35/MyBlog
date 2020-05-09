// dependency: 
// 
<template>
  <div class="blog-meta m-3 small">
    <table>
      <tbody>
        <tr v-for="(item, key) in fmtMetaDatas" :key="key">
          <td class="px-1">{{item.key}}</td>
          <td class="px-2">{{item.value}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  import { getMeta } from "network/meta";

  export default {
    name: "Meta",
    components: {},
    data() {
      return {
        metaDatas: []
      };
    },
    computed: {
      fmtMetaDatas() {
        let fmt = [];
        if (this.metaDatas.length <= 0) {
          return [];
        }
        for (let item of this.metaDatas) {
          let data = {};
          data.key = item.key.split("/")[0];
          data.value = item.value + " " + item.key.split("/")[1];
          fmt.push(data);
        }
        console.log(fmt);

        return fmt;
      }
    },
    watch: {},
    methods: {},
    created() {},
    mounted() {
      getMeta().then(response => {
        this.metaDatas = response.data;
      });
    }
  };
</script>
<style scoped>
  .show-meta {
    text-align: left;
  }
  tbody tr:not(:last-of-type) {
    border-bottom: solid 1px #c5c5c588;
  }
  table {
    margin: auto;
  }
</style>