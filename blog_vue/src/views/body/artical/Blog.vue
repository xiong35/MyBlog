// dependency: 
// 
<template>
  <div class="blog">
    <div class="blog-brief my-2" v-for="(blog, index) in filteredBlogs" :key="index">
      <h3>{{blog.headline}}</h3>
      <ul class="list-unstyled list-inline">
        <li class="list-inline-item m-1" v-for="(tag, index) in blog.tags" :key="index">
          <div class="tag">{{tag}}</div>
        </li>
      </ul>
      <div class="time text-secondary my-2">
        <span>上次修改于：{{getFmtDate(blog.last_update)}}</span>
      </div>
    </div>
  </div>
</template>

<script>
  import { getBlog } from "network/artical";
  import { parseTime, dateFormat } from "components/common/time/time";

  export default {
    name: "Blog",
    components: {},
    data() {
      return {
        blogs: [],
        tags: ["2333","test"]
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
      parseTime,
      dateFormat,
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