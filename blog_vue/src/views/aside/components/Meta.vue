// dependency: //
<template>
  <div class="blog-meta m-3 small">
    <table>
      <tbody>
        <tr v-for="(item, key) in meta" :key="key">
          <td class="px-1">{{ item.key }}</td>
          <td class="px-1">{{ item.value + " " + item.addition }}</td>
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
        meta: [],
      };
    },
    computed: {},
    watch: {},
    methods: {},
    created() {},
    async mounted() {
      let { data } = await getMeta();

      let new_date = new Date();
      let old_date = new Date("2020-5-12 12:00:00");

      let difftime = new_date - old_date;
      let day = Math.round(difftime / 24 / 60 / 60 / 1000);

      data.push({ key: "站点存活", value: day, addition: "天" });

      this.meta = data;
    },
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
