// dependency: 
// 
<template>
  <div class="briefslot">
    <div class="brief py-2 my-2">
      <slot></slot>
      <!-- <h3>{{blog.headline}}</h3> -->
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
  import { parseTime, dateFormat } from "components/common/time/time";

  export default {
    name: "BriefSlot",
    components: {},
    props: ["blog"],
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
  .brief {
    width: 95%;
    height: auto;
    margin: auto;
    border-bottom: solid 1px #6c757d;
    position: relative;
  }
  .time {
    width: 100%;
    height: auto;
    margin: auto;
    position: relative;
    text-align: right;
  }
  .tag {
    border: solid 1px #000;
    border-radius: 2000px;
    text-align: center;
    padding: 2px 10px 4px 10px;
  }
  .blog-trap {
    height: 4rem;
    width: 100%;
    margin: auto;
    border-bottom: solid 1px #000;
  }
</style>