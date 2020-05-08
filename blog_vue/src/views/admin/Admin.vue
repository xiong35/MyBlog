// dependency: 
// 
<template>
  <div class="admin col-12 col-md-9">
    <ul class="list-inline">
      <li class="list-inline-item m-3">
        <div @click="type='blog'" class="submit">+文章</div>
      </li>
      <li class="list-inline-item m-3">
        <div @click="type='trap'" class="submit">+踩坑</div>
      </li>
      <li class="list-inline-item m-3">
        <div @click="type='tag'" class="submit">+tag</div>
      </li>
      <li class="list-inline-item m-3">
        <input v-model="newTag" class="form-control" type="text" />
      </li>
    </ul>
    <mavon-editor class="mavon-editor" v-model="value" />
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
    <div v-show="type" class="comfirm p-2">
      <div v-for="(value,name) in fmtData" :key="name">
        <h4>{{name}}</h4>
        <pre>{{value}}</pre>
        <hr />
      </div>
      <ul class="choice list-inline">
        <li @click="type=''" class="list-inline-item">
          <div class="text-center choice-box">返回</div>
        </li>
        <li @click="submit" class="list-inline-item">
          <div class="text-center choice-box">提交</div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  import { postArtical } from "network/admin";

  import { getTags } from "network/artical";

  export default {
    name: "Admin",
    components: {},
    data() {
      return {
        value: "",
        newTag: "",
        tags: [],
        showAll: false,
        type: ""
      };
    },
    computed: {
      shownTags() {
        if (this.showAll) {
          return this.tags;
        }
        return this.tags.slice(0, 4);
      },
      fmtData() {
        if (!this.type) {
          return {};
        }
        let data = {};
        let values = this.value.split("======\n");
        switch (this.type) {
          case "blog":
            data = {
              headline: values[0],
              content: values[1],
              tags: this.$store.state.activeTags
            };
            break;
          case "trap":
            data = {
              context: values[0],
              problem: values[1],
              solution: values[2],
              tags: this.$store.state.activeTags
            };
            break;
          case "tag":
            data = {
              tagNames: [this.newTag]
            };
            break;
        }
        return data;
      }
    },
    watch: {},
    methods: {
      submit() {}
    },
    created() {},
    mounted() {
      getTags().then(response => {
        this.tags = response.data.reverse();
      });
      this.$store.commit("cleanTags");
    }
  };
</script>
<style scoped>
  .submit {
    border: solid 1px #000;
    border-radius: 200px;
    padding: 2px 10px 4px 10px;
    cursor: pointer;
  }
  input {
    width: 5rem;
  }
  .comfirm {
    width: 80%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #f5f2ee;
    z-index: 9;
    border-radius: 4px;
    box-shadow: 0 0 6px #aaaaaa8e;
  }
  .mavon-editor {
    z-index: 3;
  }
  .choice-box {
    width: 4rem;
    height: 2rem;
    padding: 2px 10px 4px 10px;
    border-radius: 2000px;
    border: solid 1px #000;
    margin: 7px;
  }
</style>