$.ajax({
  type: "GET",
  url: "api/skills/all",
  success: function (response) {
    response.map(function (skill) {
      $(".all-skill.skill-flex").append(`
            <span class="skill" data-target="${skill.id}" data-name="${skill.name}" id="skill${skill.id}"> ${skill.name} <i class="fa-solid fa-check second"></i> <i class="fa-solid fa-plus first"></i></span>
        `);
    });
  },
});

// $(document).on('click')
$(".btn-add").click(function (e) {
  e.preventDefault();
  $("#collapse").collapse("show");
  $(this).addClass("d-none");
  $(".btn-save1").removeClass("d-none");
});

$(document).on("click", ".all-skill.skill-flex .skill", function (e) {
  let id = $(this).attr("data-target");
  let name = $(this).attr("data-name");
  $(this).addClass("d-none");
  $(".target-skill.skill-flex").append(`
    <span class="skill my-color" data-target="${id}" data-name="${name}"> ${name} <i class="fa-solid fa-check first"></i> <i class="fa-solid fa-xmark second"></i></span>
    `);
});

$(document).on("click", ".target-skill.skill-flex .skill", function (e) {
  let id = $(this).attr("data-target");
  $(this).remove();
  $(`#skill${id}`).removeClass("d-none");
});
