import { request } from "./request";

export function getarticle(id = '',type='blog') {
  if (id) {
    id = "?id=" + id
  }
  return request({
    url: `artical/${type}/` + id
  });
}

export function getTags() {
  return request({
    url: "artical/tags/"
  });
}
