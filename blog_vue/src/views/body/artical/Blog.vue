// dependency: 
// 
<template>
  <div class="blog">
    <brief-slot v-for="(blog, index) in pagedBlogs" :key="index" :blog="blog">
      <h3>{{blog.headline}}</h3>
    </brief-slot>
    <pager @page-change="changePage" :pageNum="pageNum" :curIndex="curIndex"></pager>
  </div>
</template>

<script>
  import { getBlog } from "network/artical";

  import BriefSlot from "./BriefSlot";
  import Pager from "./Pager";

  export default {
    name: "Blog",
    components: {
      BriefSlot,
      Pager
    },
    props: {
      perPage: {
        type: Number,
        default: 7
      }
    },
    data() {
      return {
        blogs: [],
        tags: ["2333", "test"],
        curIndex: 0
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
      },
      pagedBlogs() {
        let begin = this.curIndex * this.perPage;
        return this.filteredBlogs.slice(begin, begin + this.perPage);
      },
      pageNum() {
        return Math.ceil(this.filteredBlogs.length / this.perPage);
      }
    },
    watch: {},
    methods: {
      getFmtDate(dataStr) {
        return dateFormat("YYYY年mm月dd日 HH:MM", this.parseTime(dataStr));
      },
      changePage(pageIndex) {
        this.curIndex = pageIndex;
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