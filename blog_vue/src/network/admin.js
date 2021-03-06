import { request } from "./request";

export function postarticle(data, type = "blog") {
  // blog, trap, tag
  return request({
    url: `/article/${type}/`,
    data,
    method: 'post',
    headers: {
      "Content-Type": "application/json;"
    }
  });
}

export function login(password, token = '') {
  let data = { password }
  if (token) {
    data.token = token
  }

  return request({
    url: "authorize/",
    data,
    method: 'post',
    headers: {
      "Content-Type": "application/json;"
    }
  });
}