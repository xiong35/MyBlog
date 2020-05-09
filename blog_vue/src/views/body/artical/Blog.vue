// dependency: 
// 
<template>
  <div class="blog">
    <div
      class="text-center m-5 text-secondary"
      v-show="pagedArticals.length==0"
      key="placeholder"
    >没有文章呢QwQ</div>
    <transition-group name="brief-list" tag="ul" class="list-unstyled">
      <brief-slot class="brief-item" v-for="(blog, index) in pagedArticals" :key="index" :artical="blog">
        <h3>{{blog.headline}}</h3>
      </brief-slot>
    </transition-group>

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
        blogs: []
      };
    },
    computed: {
      filteredBlogs() {
        return this.blogs.filter((value, index, array) => {
          for (let tag of this.$store.state.activeTags) {
            if (value.tags.indexOf(tag) == -1) {
              return false;
            }
          }
          return true;
        });
      }
    },
    watch: {
      "$store.state.activeTags": function() {
        this.curIndex = 0;
      }
    },
    methods: {
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