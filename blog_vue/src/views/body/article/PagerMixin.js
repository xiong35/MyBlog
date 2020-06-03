export var PagerMixin = {
  methods: {
    changePage(pageIndex) {
      this.curIndex = pageIndex;
    }
  },
  props: {
    perPage: {
      type: Number,
      default: 7
    }
  },
  data() {
    return {
      curIndex: 0
    }
  },
  computed: {
    pagedarticles() {
      let begin = this.curIndex * this.perPage;
      return this.filteredarticles.slice(begin, begin + this.perPage);
    },
    pageNum() {
      return Math.ceil(this.filteredarticles.length / this.perPage);
    }
  }
}