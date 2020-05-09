// dependency: 
// 
<template>
  <div class="trap">
    <div
      class="text-center m-5 text-secondary"
      v-show="pagedArticals.length==0"
      key="placeholder"
    >没有记录呢QwQ</div>

    <transition-group name="brief-list" tag="ul" class="list-unstyled">
      <brief-slot
        class="brief-item"
        v-for="(artical, index) in pagedArticals"
        :key="index"
        :artical="artical"
        :type="'trap'"
      >
        <h4>{{artical.context}}</h4>
        <p>{{artical.problem.length>20?artical.problem.slice(0,20)+'...':artical.problem}}</p>
      </brief-slot>
    </transition-group>

    <pager @page-change="changePage" :pageNum="pageNum" :curIndex="curIndex"></pager>
  </div>
</template>

<script>
  import { getArtical } from "network/artical";

  import BriefSlot from "./BriefSlot";
  import Pager from "./Pager";

  import { PagerMixin } from "./PagerMixin";

  export default {
    mixins: [PagerMixin],
    name: "Trap",
    components: {
      BriefSlot,
      Pager
    },
    data() {
      return {
        traps: []
      };
    },
    computed: {
      filteredArticals() {
        return this.traps.filter((value, index, array) => {
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
      getArtical("", "trap").then(response => {
        // console.log(this.traps);
        // console.log(response);
        this.traps = response.data;
      });
    }
  };
</script>
<style scoped>
</style>