export function setOrGetToken(token) {
  if (token) {
    localStorage.setItem("token", token);
  } else {
    var token = localStorage.getItem("token");
  }
  return token;
}