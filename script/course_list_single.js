const url = window.location.href;
  // Extract the value after the hyphen
  const value = url.split('?')[1];
  // Log the extracted value
  console.log(value);

  $(document).ready(function () {
    // Fetch courses on page load
    $.ajax({
        type: "GET",
        url: apiLink + "/api/course_list_single/get",
        headers: {
            Authorization: "Bearer " + getCookie("token"),
        },
        data:{
            course_id:value,
        },
        success: function (res) {
            $("#course").html("");
            res.forEach(function (course) {
                showCourse(course);
            });
        },
        error: function (err) {
            console.error('Failed to fetch courses:', err);
        },
    });

    function showCourse(course) {
        $('#course_fee').html(course.course_fee);
        $("#course").append(`
            <div class="col-12 col-md-8 mx-auto my-3">
                <div class="card mb-3">
                    <div class="row g-0">
                        <div class="col-md-4">
                            <img src="${apiLink+course.course_thumbnil}" class="img-fluid rounded-start" alt="Course Thumbnail" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                                <h5 class="card-title">${course.title}</h5>
                                <p class="card-text my-color">${course.course_outcome}</p>
                                <p class="card-text"><small class="text-muted">Course Info : ${course.course_fee} $</small></p>
                                <a href="/edit_detail?${course.id}" class="btn btn-primary" id="enroll">Enroll Now</a>
                                
                            </div>
                        </div>
                    </div>
                </div>
                <ul class="nav nav-tabs my-color" id="myTab-${course.id}" role="tablist">
                    <li class="nav-item" role="presentation">
                        <button class="nav-link active" id="learn-tab-${course.id}" data-bs-toggle="tab" data-bs-target="#learn-${course.id}" type="button" role="tab" aria-controls="learn-${course.id}" aria-selected="true">What you'll learn</button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link" id="content-tab-${course.id}" data-bs-toggle="tab" data-bs-target="#content-${course.id}" type="button" role="tab" aria-controls="content-${course.id}" aria-selected="false">Course content</button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link" id="reviews-tab-${course.id}" data-bs-toggle="tab" data-bs-target="#reviews-${course.id}" type="button" role="tab" aria-controls="reviews-${course.id}" aria-selected="false">Reviews</button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link" id="instructors-tab-${course.id}" data-bs-toggle="tab" data-bs-target="#instructors-${course.id}" type="button" role="tab" aria-controls="instructors-${course.id}" aria-selected="false">Instructors</button>
                    </li>
                </ul>
                <div class="tab-content" id="myTabContent-${course.id}">
                    <div class="tab-pane fade show active" id="learn-${course.id}" role="tabpanel" aria-labelledby="learn-tab-${course.id}">
                        <div class="card mt-3">
                            <div class="card-body">
                                <p class="card-text my-color">${course.course_outcome}</p>
                            </div>
                        </div>
                    </div>
                    <div class="tab-pane fade" id="content-${course.id}" role="tabpanel" aria-labelledby="content-tab-${course.id}">
                        <div class="card mt-3">
                            <div class="card-body">
                                <p class="card-text my-color">${course.course_contain}</p>
                            </div>
                        </div>
                    </div>
                    <div class="tab-pane fade" id="reviews-${course.id}" role="tabpanel" aria-labelledby="reviews-tab-${course.id}">
                        <div class="card mt-3">
                            <div class="card-body">
                                <p class="card-text my-color">No reviews yet.</p>
                            </div>
                        </div>
                    </div>
                    <div class="tab-pane fade" id="instructors-${course.id}" role="tabpanel" aria-labelledby="instructors-tab-${course.id}">
                        <div class="card mt-3">
                            <div class="card-body">
                                <p class="card-text my-color">Instructor details coming soon.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `);
    } 
    
    $(document).on("click","#enroll",function(e) {
        e.preventDefault();
        $('#addTrainModel').modal('show');
    });
    
  }); 

