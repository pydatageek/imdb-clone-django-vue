/* Generic CRUD for axios */
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.withCredentials = true;

let pre_url = "/api/v1/";

function icGet(name, id, sub) {
  url =
    id && sub
      ? pre_url + name + "/" + id + "/" + sub + "/"
      : id
        ? pre_url + name + "/" + id + "/"
        : pre_url + name + "/";

  return axios
    .get(url)
    .then(res => (id || sub ? res.data : res.data.results))
    .catch(err => console.log(err.response));
}

function icPost(name, obj) {
  return axios
    .post(pre_url + name + "/", obj)
    .then(res => res)
    .catch(err => console.log(err.response));
}

function icPut(name, obj, id) {
  return axios
    .put(pre_url + name + "/" + id + "/", obj)
    .then(res => res)
    .catch(err => console.log(err.response));
}

function icDelete(name, id) {
  return axios
    .delete(pre_url + name + "/" + id + "/")
    .then(res => res)
    .catch(err => console.log(err.response));
}

/* Other Helper Functions */
function icGoto(url, slug) {
  window.location.href = slug ? url + slug + "/" : url;
}

function icChoices() {
  return axios
    .get("/api/v1/choice/")
    .then(res => res.data)
    .catch(err => console.log(err.response));
}

function pageId() {
  var arr = window.location.href.split("/");
  return arr[arr.length - 2];
}

/* Other Helper Functions */
function icChoices() {
  return axios
    .get("/api/v1/choice/")
    .then(res => res.data)
    .catch(err => console.log(err.response));
}