// dependency: 
// 
<template>
  <div class="blog">
    <div
      class="text-center m-5 text-secondary"
      v-show="pagedarticles.length==0"
      key="placeholder"
    >没有文章呢QwQ</div>
    <transition-group name="brief-list" tag="ul" class="list-unstyled">
      <brief-slot
        class="brief-item"
        v-for="(blog, index) in pagedarticles"
        :key="index"
        :article="blog"
      >
        <h3>{{blog.headline}}</h3>
      </brief-slot>
    </transition-group>

    <pager @page-change="changePage" :pageNum="pageNum" :curIndex="curIndex"></pager>
  </div>
</template>

<script>
  import { getarticle } from "network/article";

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
      filteredarticles() {
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
    methods: {},
    created() {},
    mounted() {
      getarticle().then(response => {
        this.blogs = response.data;
      });
    }
  };
</script>
<style scoped>
</style>