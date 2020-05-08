import { request } from "./request";

export function getBlog(id = '') {
  if (id) {
    id = "?id=" + id
  }
  return request({
    url: "/artical/blog/" + id
  });
}

export function getTags() {
  return request({
    url: "/artical/tags/"
  });
}
