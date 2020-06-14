import { request } from "./request";

export function getArticle(id = '',type='blog') {
  if (id) {
    id = "?id=" + id
  }
  return request({
    url: `articles/${type}` + id
  });
}

export function getTags() {
  return request({
    url: "articles/tags"
  });
}
