<template>
  <div v-title data-title="Artical" class="col-12 col-md-9" id="artical">
    <ul class="nav nav-tabs my-2">
      <li class="nav-item">
        <big class="nav-link active" href="#">文章</big>
      </li>
      <li class="nav-item">
        <big class="nav-link" href="#">踩坑记录</big>
      </li>
    </ul>

    <transition-group name="tag-ul" tag="ul" class="tag-list p-2 list-inline">
      <li
        class="list-inline-item m-1 tag"
        v-for="(tag, index) in shownTags"
        :key="index"
        :class="{'activeTag': $store.state.activeTags.indexOf(tag.tag_name) != -1 }"
        @click="$store.commit('toggleActiveTag',tag.tag_name)"
      >{{tag.tag_name}}</li>
      <li class="list-inline-item m-1 tag toggle-tags" key="toggle" @click="showAll = !showAll">
        {{!showAll?'更多':'收起'}}
        <i class="fa fa-angle-double-down" :class="{'toggle-up':showAll}"></i>
      </li>
    </transition-group>
    <div>
      <blog></blog>
    </div>
  </div>
</template>

<script>
  import Blog from "./Blog";
  import Trap from "./Trap";

  import { getTags } from "network/artical";

  export default {
    name: "Artical",
    components: {
      Blog,
      Trap
    },
    data() {
      return {
        tags: [],
        showAll: false
      };
    },
    computed: {
      shownTags() {
        if (this.showAll) {
          return this.tags;
        }
        return this.tags.slice(0, 4);
      }
    },
    watch: {},
    methods: {},
    mounted() {
      getTags().then(response => {
        this.tags = response.data.reverse();
      });
    }
  };
</script>
<style>
  #artical {
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
</style>