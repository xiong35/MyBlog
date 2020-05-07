// dependency: 
// 
<template>
  <div class="blog">
    <brief-slot
      v-for="(blog, index) in pagedBlogs"
      :key="index"
      :blog="blog"
    >
      <h3>{{blog.headline}}</h3>
    </brief-slot>
    <pager @page-change="changePage" :pageNum="pageNum" :curIndex="curIndex"></pager>
  </div>
</template>

<script>
  import { getBlog } from "network/artical";

  import BriefSlot from "./BriefSlot";
  import Pager from "./Pager";

  import { PagerMixin } from "./PagerMixin";

  export default {
    mixins: [PagerMixin],
    name: "Blog",
    components: {
      BriefSlot,
      Pager
    },
    data() {
      return {
        blogs: [],
        tags: []
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