// dependency: 
// 
<template>
  <div class="admin py-5 px-3 container text-right">
    <h1 class="text-center m-3">Admin</h1>

    <mavon-editor class="mavon-editor" :toolbars="config" :tabSize="4" v-model="value" />

    <transition-group name="tag-ul" tag="ul" class="tag-list mt-5 list-inline">
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

    <ul class="list-inline">
      <li
        v-for="(value, name) in {blog:'+文章',trap:'+踩坑',tags:'+tags'}"
        :key="name"
        class="list-inline-item m-3"
      >
        <div @click="type=name" class="submit">{{value}}</div>
      </li>
      <li class="list-inline-item m-3">
        <input v-model="newTag" class="form-control" type="text" />
      </li>
    </ul>

    <transition name="toggle">
      <div v-if="type" class="comfirm p-2">
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
          <li class="list-inline-item">
            <input v-model="password" placeholder="请输入密码" class="form-control" type="text" />
          </li>
        </ul>
      </div>
    </transition>
  </div>
</template>

<script>
  import { postArticle, login } from "network/admin";
  import { getTags } from "network/article";

  import { setOrGetToken } from "components/common/methods/token";

  let config = {
    underline: true, // 下划线
    strikethrough: true, // 中划线
    mark: true, // 标记
    superscript: true, // 上角标
    subscript: true, // 下角标
    imagelink: true, // 图片链接
    fullscreen: true, // 全屏编辑
    readmodel: true, // 沉浸式阅读
    subfield: true, // 单双栏模式
    preview: true // 预览
  };

  export default {
    name: "Admin",
    components: {},
    data() {
      return {
        value: "",
        newTag: "",
        tags: [],
        showAll: false,
        type: "",
        config,
        password: ""
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
        let content = this.value
        let one = /^# (.*)$/gm.exec(this.value)[1]
        let two = /^## (.*)$/gm.exec(this.value)[1]
        let data = {};
        switch (this.type) {
          case "blog":
            data = {
              headline: one,
              content,
              tags: this.$store.state.activeTags
            };
            break;
          case "trap":
            data = {
              context: one,
              problem: two,
              solution: content,
              tag_names: this.$store.state.activeTags
            };
            break;
          case "tags":
            data = {
              tag_names: [this.newTag]
            };
            break;
        }
        return data;
      }
    },
    watch: {},
    methods: {
      submit() {
        let fmtData = this.fmtData;
        let type = this.type;
        let token = setOrGetToken();

        login(this.password, token).then(response => {
          fmtData.token = response.token;
          setOrGetToken(response.token);

          postArticle(fmtData, type)
            .then(response => {
              if (response.status == 200) {
                alert("成功!");
              } else if (response.status == 401) {
                alert("未登录!");
              } else {
                alert(response.status);
              }
            })
            .then(() => {
              getTags().then(response => {
                this.tags = response.data.reverse();
              });
            });
        });
        this.type = "";
      }
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
    width: 7rem;
  }
  .comfirm {
    width: 80%;
    position: absolute;
    top: 100px;
    left: 10%;
    background-color: #f5f2ee;
    z-index: 9;
    border-radius: 4px;
    box-shadow: 0 0 6px #aaaaaa8e;
  }
  .comfirm h4,
  .comfirm pre {
    text-align: initial;
  }
  .mavon-editor {
    z-index: 3;
    width: 100% !important;
  }
  .choice-box {
    width: 4rem;
    height: 2rem;
    padding: 2px 10px 4px 10px;
    border-radius: 2000px;
    border: solid 1px #000;
    margin: 7px;
    cursor: pointer;
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

  .toggle-enter-active,
  .toggle-leave-active {
    transition: opacity 0.4s;
  }
  .toggle-enter,
  .toggle-leave-to {
    opacity: 0;
  }
</style>