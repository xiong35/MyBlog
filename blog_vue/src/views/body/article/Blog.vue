// dependency: //
<template>
  <div class="blog">
    <div
      class="text-center m-5 text-secondary"
      v-show="pagedarticles.length == 0"
      key="placeholder"
    >
      没有文章呢QwQ
    </div>
    <transition-group name="brief-list" tag="ul" class="list-unstyled">
      <brief-slot
        class="brief-item"
        v-for="(blog, index) in pagedarticles"
        :key="index"
        :article="blog"
      >
        <h3>{{ blog.Headline | clip }}</h3>
      </brief-slot>
    </transition-group>

    <pager
      @page-change="changePage"
      :pageNum="pageNum"
      :curIndex="curIndex"
    ></pager>
  </div>
</template>

<script>
  import { getArticle } from "network/article";

  import BriefSlot from "./BriefSlot";
  import Pager from "./Pager";

  import { PagerMixin } from "./PagerMixin";

  export default {
    mixins: [PagerMixin],
    name: "Blog",
    components: {
      BriefSlot,
      Pager,
    },
    props: ["type"],
    data() {
      return {
        blogs: [],
      };
    },
    computed: {
      filteredarticles() {
        if (this.blogs.length == 0) {
          return [];
        }
        return this.blogs.filter((value, index, array) => {
          for (let tag of this.$store.state.activeTags) {
            if (value.Tags.map((it) => it.TagName).indexOf(tag) == -1) {
              return false;
            }
          }
          return true;
        });
      },
    },
    watch: {
      "$store.state.activeTags": function () {
        this.curIndex = 0;
      },
    },
    filters: {
      clip(value) {
        if (value.length >= 45) {
          return value.slice(0, 44) + "...";
        } else {
          return value;
        }
      },
    },
    methods: {},
    created() {},
    watch: {
      type() {
        getArticle("", this.type).then((response) => {
          this.blogs = response.data;
        });
      },
    },
    mounted() {
      getArticle("", this.type).then((response) => {
        this.blogs = response.data;
      });
    },
  };
</script>
<style scoped></style>
