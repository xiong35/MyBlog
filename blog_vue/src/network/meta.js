import { request } from "./request";

export function getMeta() {
  return request({
    url: "/meta"
  });
}