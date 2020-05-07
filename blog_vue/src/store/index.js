import Vue from "vue";
import vuex from "vuex";
// better extract mutations and actions out to another file
// import mutations from "./mutations";
// import actions from "./actions";



Vue.use(vuex);

const state = {
  duckAlive: true,
  scrollManager: null
}

const store = new vuex.Store({
  // use store to get state
  state,
  // use store.commit('methodName', payload)
  mutations: {
    someMethod(state, payload) { },
    toggleDuck(state) {
      state.duckAlive = !state.duckAlive
    },
    setScroll(state, payload) {
      state.scrollManager = payload
    }
  },
  // use store.diapatch('methodName', payload)
  // context == this, use context.state
  actions: {
    someMethod(context, payload) { },
    scrollTo(context, payload) {
      if (payload) {
        var { x, y, time } = payload
      } else {
        var [x, y, time] = [0, 0, 300]
      }
      context.state.scrollManager.scrollTo(x, y, time);
    }
  }
});

export default store;
// 在main.js里, 传入的对象里直接多写一个store就行了