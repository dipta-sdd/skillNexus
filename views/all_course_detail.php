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
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
      integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    />
    <link rel="stylesheet" href="../style/style.css" />
    <style>
      .course-list-item {
        display: flex;
        align-items: center;
        border-bottom: 1px solid #ddd;
        padding: 15px 0;
      }
      .course-thumbnail {
        width: 150px;
        height: 100px; /* Set a fixed height */
        object-fit: cover; /* Ensure the image fits within the given height */
        margin-right: 20px;
        flex-shrink: 0; /* Prevent the image from shrinking */
      }
      .course-details {
        flex-grow: 1;
      }
      .course-title {
        margin: 0;
        font-size: 1.25rem;
        font-weight: bold;
      }
      .course-outcome {
        margin: 10px 0;
        font-size: 0.9rem;
        height: 3rem; /* Set a fixed height for descriptions */
        overflow: hidden; /* Hide overflow text */
      }
      .course-actions {
        margin-left: auto;
        display: flex;
        flex-direction: column;
        align-items: flex-end;
      }
      .course-actions a,
      .course-actions button {
        margin-bottom: 5px;
        width: 100px; /* Set a fixed width for buttons */
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
          <li class="breadcrumb-item" aria-current="page">Login</li>
        </ol>
      </nav>

      <!-- main body-->
      <div class="row my-color mybg my-row" id="course" style="font-family: cursive;">
      </div>
      <!-- main body-->
    </div>

    <script src="../script/bootstrap.bundle.min.js"></script>
    <script src="../script/jquery-3.7.1.min.js"></script>
    <script src="../script/script.js"></script>
    <script src="../script/all_course_detail.js"></script>
    <script>
      $(document).ready(function () {
        on_page_load([]);
      });
    </script>
  </body>
</html>
