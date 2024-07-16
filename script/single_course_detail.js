const url = window.location.href;
// Extract the value after the hyphen
const value = url.split('?')[1];
// Log the extracted value
console.log(value);

$(document).ready(function () {
    // Fetch courses on page load
    $.ajax({
        type: "GET",
        url: apiLink + "/api/course/get",
        headers: {
            Authorization: "Bearer " + getCookie("token"),
        },
        data: {
            course_id: value,
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
        $("#course").append(`
            <div class="col-12 col-md-8 mx-auto my-3">
                <div class="card mb-3">
                    <div class="row g-0">
                        <div class="col-md-4">
                            <img src="${apiLink + course.course_thumbnil}" class="img-fluid rounded-start" alt="Course Thumbnail" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                                <h5 class="card-title">${course.title}</h5>
                                <p class="card-text my-color">${course.course_outcome}</p>
                                <p class="card-text"><small class="text-muted">Course Info : ${course.course_fee} $</small></p>
                                <a href="/edit_detail?${course.id}" class="btn btn-primary">Edit Course</a>
                                <a href="#" class="btn btn-danger">Delete</a>
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
                        <button class="nav-link" id="lectures-tab-${course.id}" data-bs-toggle="tab" data-bs-target="#lectures-${course.id}" type="button" role="tab" aria-controls="lectures-${course.id}" aria-selected="false">Lectures</button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link" id="add-lecture-tab-${course.id}" data-bs-toggle="tab" data-bs-target="#add-lecture-${course.id}" type="button" role="tab" aria-controls="add-lecture-${course.id}" aria-selected="false">Add Lecture</button>
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
                                <p class="card-text my-color ">${course.course_contain}</p>
                            </div>
                        </div>
                    </div>

                  
                    <div class="tab-pane fade" id="lectures-${course.id}" role="tabpanel" aria-labelledby="lectures-tab-${course.id}">
                        <div class="card mt-3">
                            <div class="card-body" id="lectures-content-${course.id}">
                                <!-- Lectures will be appended here -->
                            </div>
                        </div>
                    </div>
                    <div class="tab-pane fade" id="add-lecture-${course.id}" role="tabpanel" aria-labelledby="add-lecture-tab-${course.id}">
                        <div class="card mt-3">
                            <div class="card-body">
                                <a href="/lecture_up?${course.id}" class="btn btn-primary">Add Lecture</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `);
        fetchLectures(course.id);
    }

    function fetchLectures(courseId) {
        $.ajax({
            type: "GET",
            url: apiLink + "/api/lecture/get",
            headers: {
                Authorization: "Bearer " + getCookie("token"),
            },
            data: {
                course_id: courseId,
            },
            success: function (res) {
                res.forEach(function (lecture) {
                    showLecture(courseId, lecture);
                });
            },
            error: function (err) {
                console.error('Failed to fetch lectures:', err);
            },
        });
    }

    function showLecture(courseId, lecture) {
        $(`#lectures-content-${courseId}`).append(`
       <div class="col-12">
            <div class="card mb-3">
                <div class="row g-0">
                    <div class="col-md-4">
                        <video class="img-fluid rounded-start" width="100%" height="150" controls style="object-fit: cover;">
                            <source src="${apiLink + lecture.video}" type="video/mp4">
                            Your browser does not support the video tag.
                        </video>
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <h5 class="card-title">${lecture.title}</h5>
                            <p class="card-text my-color">${lecture.lecture_description}</p>
                            <div class="lecture-links mb-2">
                               
                                
                                <a href="${apiLink + lecture.video}" target="_blank" class="btn btn-sm btn-outline-secondary">Video</a>
                                <a href="/lec_detail?${lecture.id}" class="btn btn-sm btn-outline-secondary">View Lecture</a>
                                </div>
                          
                        </div>
                    </div>
                </div>
            </div>
        </div>


     `);
    }
});
