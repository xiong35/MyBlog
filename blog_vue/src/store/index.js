import Vue from "vue";
import vuex from "vuex";
// better extract mutations and actions out to another file
// import mutations from "./mutations";
// import actions from "./actions";

Vue.use(vuex);

const state = {
  duckAlive: true
}

const store = new vuex.Store({
  // use store to get state
  state,
  // use store.commit('methodName', payload)
  mutations: {
    someMethod(state, payload) { },
    toggleDuck(state) {
      state.duckAlive = !state.duckAlive
    }
  },
  // use store.diapatch('methodName', payload)
  // context == this, use context.state
  actions: {
    someMethod(context, payload) { }
  }
});

export default store;
// 在main.js里, 传入的对象里直接多写一个store就行了