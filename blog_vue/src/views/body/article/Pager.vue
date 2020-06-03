// dependency: 
// 
<template>
  <ul class="pager list-unstyled my-3">
    <li class="turn-left list-inline-item">
      <button class="turn-box btn" :disabled="disabled('left')" @click="btnClick(curIndex - 1)">
        <i class="fa fa-angle-double-left"></i>
      </button>
    </li>
    <li
      class="list-inline-item"
      :class="{'left-more':index<pageNum-1&&index>2&&index==curIndex,
               'right-more':index<pageNum-3&&index>0&&index==curIndex
                ||(index==1&&pageNum>4&&(curIndex==0||curIndex==pageNum-1))}"
      v-for="(index) in displayList()"
      :key="index"
    >
      <button
        class="pager-box btn"
        :class="{'cur-page': index == curIndex}"
        @click="btnClick(index)"
      >{{index+1}}</button>
    </li>
    <li class="turn-right list-inline-item">
      <button class="turn-box btn" :disabled="disabled('right')" @click="btnClick(curIndex + 1)">
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
          if (this.curIndex <= 0 && value == "left") {
            return true;
          }
          if (this.curIndex >= this.pageNum - 1 && value == "right") {
            return true;
          }
          return false;
        };
      }
    },
    watch: {},
    methods: {
      btnClick(index) {
        this.$emit("page-change", index);
        // this.$store.dispatch("scrollTo");
      },
      displayList() {
        if (this.pageNum <= 4) {
          return [...new Array(this.pageNum).keys()];
        }
        if (this.curIndex < this.pageNum - 2 && this.curIndex > 1) {
          return [0, 1, this.curIndex, this.pageNum - 2, this.pageNum - 1];
        }
        return [0, 1, this.pageNum - 2, this.pageNum - 1];
      }
    },
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
    box-shadow: 0 0 3px #007bff80;
    color: #fff;
    font-weight: bold;
  }
  .left-more::before {
    content: "... ";
  }
  .right-more::after {
    content: " ...";
  }
</style>