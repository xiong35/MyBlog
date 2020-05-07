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
    pagedBlogs() {
      let begin = this.curIndex * this.perPage;
      return this.filteredBlogs.slice(begin, begin + this.perPage);
    },
    pageNum() {
      return Math.ceil(this.filteredBlogs.length / this.perPage);
    }
  }
}