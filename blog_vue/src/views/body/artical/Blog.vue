// dependency: 
// 
<template>
  <div class="blog">
    <div
      class="text-center m-5 text-secondary"
      v-show="pagedBlogs.length==0"
      key="placeholder"
    >没有文章呢QwQ</div>
    <transition-group name="brief-list" tag="ul" class="list-unstyled">
      <brief-slot class="brief-item" v-for="(blog, index) in pagedBlogs" :key="index" :blog="blog">
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
          // if (this.$store.state.activeTags.length == 0) {
          //   return true;
          // }
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
  .brief-item {
    transition: all 0.5s ease;
  }
  .brief-list-enter,
  .brief-list-leave-to {
    opacity: 0;
    transform: translate(30px, 20px);
  }
  /* TODO change to one by one animation  */
</style>