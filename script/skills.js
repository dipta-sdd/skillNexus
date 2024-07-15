$.ajax({
  type: "GET",
  url: "api/skills/get",
  headers: {
    Authorization: "Bearer " + getCookie("tooken"),
  },
  success: function (response) {
    console.log(response);
  },
});
