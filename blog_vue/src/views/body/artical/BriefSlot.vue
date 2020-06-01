// dependency: 
// 
<template>
  <router-link tag="div" :to="{path: type+'/'+ article.id}">
    <div class="back-border my-2">
      <div class="brief p-2">
        <slot></slot>
        <ul class="list-unstyled list-inline">
          <li class="list-inline-item m-1" v-for="(tag, index) in article.tags" :key="index">
            <div
              class="tag"
              :class="{'activeTag': $store.state.activeTags.indexOf(tag) != -1 }"
              @click.stop="$store.commit('toggleActiveTag',tag)"
            >{{tag}}</div>
          </li>
        </ul>
        <div class="time text-secondary">
          <span>上次修改于：{{getFmtDate(article.last_update)}}</span>
        </div>
      </div>
    </div>
  </router-link>
</template>

<script>
  import { parseTime, dateFormat } from "components/common/time/time";

  export default {
    name: "BriefSlot",
    components: {},
    props: {
      article: {
        type: Object,
        default: {}
      },
      type: {
        type: String,
        default: "blog"
      }
    },
    computed: {},
    methods: {
      parseTime,
      dateFormat,
      getFmtDate(dataStr) {
        return dateFormat("YYYY年mm月dd日 HH:MM", this.parseTime(dataStr));
      }
    },
    mounted() {}
  };
</script>
<style scoped>
  ul {
    margin: 0;
  }
  .back-border {
    width: 95%;
    height: auto;
    margin: auto;
    position: relative;
    padding: 2px;
    background-image: linear-gradient(
      -50deg,
      #3a00da 30%,
      #3a99ff 59%,
      #00c3ff 69%,
      #fff 70%
    );
    transition: all 1s ease;
    background-size: 420%;
    cursor: pointer;
  }
  .back-border:hover {
    background-position: 46%;
    box-shadow: 1px 1px 7px #00a2ff86;
    color: #007bff;
    border-radius: 2px;
  }
  .back-border:hover .tag {
    border: solid 1px #0046c7;
    color: #0b52d6;
  }
  .brief {
    box-shadow: 1px 2px 6px #9c9c9c57;
    background-color: #fff;
    width: 100%;
    border-radius: 2px;
  }
  .time {
    width: 100%;
    height: auto;
    margin: auto;
    position: relative;
    text-align: right;
  }
  .tag:hover {
    transition: all 0.3s ease;
  }
  .blog-trap {
    height: 4rem;
    width: 100%;
    margin: auto;
    border-bottom: solid 1px #000;
  }
</style>