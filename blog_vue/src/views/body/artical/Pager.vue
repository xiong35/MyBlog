// dependency: 
// 
<template>
  <ul class="pager list-unstyled my-3">
    <li class="turn-left list-inline-item">
      <button
        class="turn-box btn"
        :disabled="disabled('left')"
        @click="$emit('page-change',curIndex-1)"
      >
        <i class="fa fa-angle-double-left"></i>
      </button>
    </li>
    <li class="pager-item list-inline-item" v-for="(item, index) in pageNum" :key="index">
      <button
        class="pager-box btn"
        :class="{'cur-page':index==curIndex}"
        @click="$emit('page-change',index)"
      >{{index+1}}</button>
    </li>
    <li class="turn-right list-inline-item">
      <button
        class="turn-box btn"
        :disabled="disabled('right')"
        @click="$emit('page-change',curIndex+1)"
      >
        <i class="fa fa-angle-double-right"></i>
      </button>
    </li>
  </ul>
</template>

<script>
  export default {
    name: "pager",
    props: ["pageNum", "curIndex"],
    data() {
      return {};
    },
    computed: {
      disabled() {
        return value => {
          if (this.curIndex == 0 && value == "left") {
            return true;
          }
          if (this.curIndex == this.pageNum - 1 && value == "right") {
            return true;
          }
          return false;
        };
      }
    },
    watch: {},
    methods: {},
    created() {},
    mounted() {}
  };
</script>
<style scoped>
  .btn {
    border: solid 1px #000;
    border-radius: 2px;
    transition: all 0.3s ease;
    padding-bottom: 0.43rem;
  }
  .pager {
    margin: auto;
    text-align: center;
  }
  .btn:disabled {
    cursor: not-allowed;
  }
  .btn:hover {
    border: solid 1px #007bff;
    color: #007bff;
    box-shadow: 0 0 3px #007bff66;
  }
  .btn.cur-page {
    border: solid 1px #007bff;
    background-color: #1687ff;
    color: #fff;
    font-weight: bold;
  }
</style>