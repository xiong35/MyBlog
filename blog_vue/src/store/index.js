import Vue from "vue";
import vuex from "vuex";
// better extract mutations and actions out to another file
// import mutations from "./mutations";
// import actions from "./actions";



Vue.use(vuex);

const state = {
  duckAlive: true,
  activeTags: []
}

const store = new vuex.Store({
  // use store to get state
  state,
  // use store.commit('methodName', payload)
  mutations: {
    toggleDuck(state) {
      state.duckAlive = !state.duckAlive
    },
    toggleActiveTag(state, payload) {
      // give a tag id
      for (let index in state.activeTags) {
        if (state.activeTags[index] == payload) {
          state.activeTags.splice(index, 1)
          return
        }
      }
      state.activeTags.push(payload)
    },
    cleanTags(state) {
      state.activeTags.length = 0
    }
  },
  // use store.diapatch('methodName', payload)
  // context == this, use context.state
  actions: {
    scrollTo(context, payload) {
      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    }
  }
});

export default store;
// 在main.js里, 传入的对象里直接多写一个store就行了