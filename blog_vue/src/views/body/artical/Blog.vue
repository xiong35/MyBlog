// dependency: 
// 
<template>
  <div class="blog">
    <brief-slot v-for="(blog, index) in blogs" :key="index" :blog="blog">
      <h3>{{blog.headline}}</h3>
    </brief-slot>
  </div>
</template>

<script>
  import { getBlog } from "network/artical";
  import BriefSlot from "./BriefSlot";

  export default {
    name: "Blog",
    components: {
      BriefSlot
    },
    data() {
      return {
        blogs: [],
        tags: ["2333", "test"]
      };
    },
    computed: {
      filteredBlogs() {
        return this.blogs.filter((value, index, array) => {
          if (this.tags.length == 0) {
            return true;
          }
          for (let tag of this.tags) {
            if (value.tags.indexOf(tag) != -1) {
              return true;
            }
          }
          return false;
        });
      }
    },
    watch: {},
    methods: {
      getFmtDate(dataStr) {
        return dateFormat("YYYY年mm月dd日 HH:MM", this.parseTime(dataStr));
      }
    },
    created() {
      getBlog().then(response => {
        this.blogs = response.data;
      });
    },
    mounted() {}
  };
</script>
<style scoped>
</style>