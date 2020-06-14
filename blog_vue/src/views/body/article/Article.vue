<template>
  <div v-title data-title="article" class="col-12 col-md-9" id="article">
    <ul class="nav nav-tabs my-2">
      <li
        class="nav-item"
        v-for="(item, index) in ['文章', '踩坑记录']"
        :key="index"
      >
        <big
          class="nav-link"
          :class="{ active: activeIndex == index }"
          @click="activeIndex = index"
          >{{ item }}</big
        >
      </li>
    </ul>

    <transition-group
      name="tag-ul"
      tag="ul"
      class="tag-list p-2 list-inline"
    >
      <li
        class="list-inline-item m-1 tag"
        v-for="(tag, index) in shownTags"
        :key="index + 'article'"
        :class="{
          activeTag: $store.state.activeTags.indexOf(tag.tag_name) != -1,
        }"
        @click="$store.commit('toggleActiveTag', tag.tag_name)"
      >
        {{ tag.tag_name }}
      </li>
      <li
        class="list-inline-item m-1 tag toggle-tags"
        key="toggle"
        @click="showAll = !showAll"
      >
        {{ !showAll ? "更多" : "收起" }}
        <i
          class="fa fa-angle-double-down"
          :class="{ 'toggle-up': showAll }"
        ></i>
      </li>
    </transition-group>
    <keep-alive>
      <Blog :type='["blog", "trap"][activeIndex]' />
    </keep-alive>
  </div>
</template>

<script>
  import Blog from "./Blog";

  import { getTags } from "network/article";

  export default {
    name: "article",
    components: {
      Blog,
    },
    data() {
      return {
        tags: [],
        showAll: false,
        activeIndex: 0,
      };
    },
    computed: {
      shownTags() {
        if (this.showAll) {
          return this.tags;
        }
        return this.tags.slice(0, 4);
      },
    },
    watch: {},
    methods: {},
    mounted() {
      getTags().then((response) => {
        this.tags = response.data.reverse();
      });
    },
  };
</script>
<style>
  #article {
    width: 100%;
  }
  .nav-tabs,
  .tag-list {
    width: 90%;
    margin: auto;
  }
  .tag {
    border: solid 1px #000;
    border-radius: 2000px;
    text-align: center;
    padding: 2px 10px 4px 10px;
    transition: all 0.3s ease;
    cursor: pointer;
  }
  .tag:hover,
  .activeTag {
    box-shadow: 0 0 5px #007bff71;
    background-color: #0da5fd;
    color: #fff !important;
    border-color: #0da5fd !important;
  }
  .nav-item {
    cursor: pointer;
  }
  .tag-ul-enter,
  .tag-ul-leave-to {
    opacity: 0;
    transform: translateY(30px);
  }
  .tag-ul-leave-active {
    position: absolute;
  }
  .toggle-up {
    transform: rotate(180deg);
  }
  .toggle-tags i {
    transition: all 0.5s ease;
  }
  /* TODO change to one by one animation  */

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
