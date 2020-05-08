import { request } from "./request";

export function postArtical(data, type = "blog") {
  // blog, trap, tag
  return request({
    url: `/artical/${type}/`,
    data,
    method: 'post',
    headers: {
      "Content-Type": "application/json;"
    }
  });
}