<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>SkilNexus</title>
  <link href="../style/bootstrap.min.css" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  <link rel="stylesheet" href="../style/style.css" />
  <style>
    .course-list-item {
      display: flex;
      align-items: center;
      border-bottom: 1px solid #ddd;
      padding: 15px 0;
    }
    .course-thumbnail {
      width: 70%;
      height: 70%;
      object-fit: cover;
    
    }
    .course-details {
      flex-grow: 1;
    }
    .course-title {
      margin: 0;
      font-size: 1.5rem; /* increased size */
      font-weight: bold;
    }
    .course-outcome {
      margin: 10px 0;
      font-family:cursive;
      font-size: 1rem; /* increased size */
    }
    .course-actions {
      display: flex;
      align-items: center;
      /* margin-left: 400px; */
      gap: 10px; /* Adjust the gap between buttons */
    }
    .course-actions button {
      /* margin-bottom: 5px; */
      width: 100px;
    }
    .modal-content {
      font-size: 1rem; /* Adjust modal font size */
    }
  
  </style>
</head>
<body>
  <div aria-live="polite" aria-atomic="true" class="position-relative">
    <div class="toast-container top-0 end-0 p-3">
      <!-- Then put toasts within -->
    </div>
  </div>
  <?php include 'sidebar.php' ?>
  <div class="my-round" id="body">
    <nav aria-label="breadcrumb" class="mybg-t breadcrumb">
      <ol class="breadcrumb">
        <li class="breadcrumb-item"><a href="/">Home</a></li>
        <li class="breadcrumb-item" aria-current="page">Showing Lecture Details</li>
      </ol>
    </nav>
    <!-- main body-->
    <div class="row my-color mybg my-row" id="course" style="font-family: cursive">
      <!-- Edit Modal -->
     
    </div>
    <!-- main body-->
  </div>
  <script src="../script/bootstrap.bundle.min.js"></script>
  <script src="../script/jquery-3.7.1.min.js"></script>
  <script src="../script/script.js"></script>
 
  <script>
    $(document).ready(function () {
      on_page_load([]);
      const url = window.location.href;
      const courseId = url.split('?')[1]; // Extract the course ID from the URL

      // Fetch course lecture details based on the course ID
      $.ajax({
        type: "GET",
        url: apiLink + "/api/course_video/get",
        headers: {
          Authorization: "Bearer " + getCookie("token"),
        },
        data: {
          course_id: courseId,
        },
        success: function (res) {
          $("#course").html("");
          res.forEach(function (courseLecture) {
            showCourseLecture(courseLecture);
          });
        },
        error: function (err) {
          console.error('Failed to fetch course lectures:', err);
        },
      });

      // Function to display course lecture details
      function showCourseLecture(courseLecture) {
        $("#course").append(`
          <div class="col-12">
            <div class="video-card ms-5">
              <center><h2 style="color:blue;">Showing Lecture Details</h2></center><br>
              <div class="video-thumbnail">
               <center> <video src="${apiLink + courseLecture.video}" controls style="width: 100%; "></video></center>
              </div>
              <div class="video-details">
                <h4 class="video-title my-color">Lecture title : ${courseLecture.title}</h4>
                
                <h4 class="video-description my-color" style="font-family:cursive;">Lecture Description : ${courseLecture.lecture_description}</h4>
                <a href="${apiLink + courseLecture.material}" target="_blank" class="btn btn-sm btn-outline-secondary">Download Material</a>
                <a href="#" class="btn btn-danger" style="float:right;">Delete</a></center> &nbsp &nbsp
                <a href="/edit_video?${courseLecture.id}" class="btn btn-primary" style="float:right;">Edit Lecture</a>
                
                
              </div>
            </div>
          </div>
        `);
      }

      // Function to handle edit video
      window.editVideo = function (id, title, description) {
        console.log("Edit button clicked"); // Debug log
        $('#lectureTitle').val(title);
        $('#lectureDescription').val(description);
        $('#editModal').modal('show');

        $('#saveChanges').off('click').on('click', function () {
          const updatedTitle = $('#lectureTitle').val();
          const updatedDescription = $('#lectureDescription').val();
          const updatedMaterial = $('#lectureMaterial')[0].files[0];
          const updatedVideo = $('#lectureVideo')[0].files[0];

          const formData = new FormData();
          formData.append('id', id);
          formData.append('title', updatedTitle);
          formData.append('lecture_description', updatedDescription);
          if (updatedMaterial) {
            formData.append('material', updatedMaterial);
          }
          if (updatedVideo) {
            formData.append('video', updatedVideo);
          }

          $.ajax({
            type: "POST",
            url: apiLink + "/api/course_video/edit",
            headers: {
              Authorization: "Bearer " + getCookie("token"),
            },
            data: formData,
            processData: false,
            contentType: false,
            success: function (res) {
              $('#editModal').modal('hide');
              location.reload();
            },
            error: function (err) {
              console.error('Failed to update course lecture:', err);
            },
          });
        });
      };

      // Function to handle delete video (adjust this as per your backend logic)
      window.deleteVideo = function (id) {
        if (confirm("Are you sure you want to delete this video?")) {
          $.ajax({
            type: "DELETE",
            url: apiLink + "/api/course_video/delete/" + id,
            headers: {
              Authorization: "Bearer " + getCookie("token"),
            },
            success: function (res) {
              location.reload();
            },
            error: function (err) {
              console.error('Failed to delete video:', err);
            },
          });
        }
      };
    });
  </script>
</body>
</html>
