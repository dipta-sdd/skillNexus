<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">

    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>SkilNexus</title>
    <link
      href="../style/bootstrap.min.css"
      rel="stylesheet"
       
    />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
      integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    />
    <link rel="stylesheet" href="../style/style.css" />
    <link rel="stylesheet" href="../style/skills.css" />
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
              <li class="breadcrumb-item" aria-current="page">My Skills</li>
            </ol>
          </nav>
          <!-- Modal -->
          <div class="modal fade modal-lg" style="z-index: 6000" id="modal" tabindex="-1" aria-labelledby="myModel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">
              <div class="modal-content">
                <div class="modal-header">
                  <h1 class="modal-title fs-5 my-color" id="myModel">Are you sure to add this skills?</h1>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <div class="row">
                    <div class="target-skill skill-flex">
                        <!-- selected skills gowes here -->
                    </div>
                  </div>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                  <button type="button" class="btn btn-primary">Save changes</button>
                </div>
              </div>
            </div>
          </div>
          <!-- Modal -->
          
          <div class="row my-color mybg my-row">
            <div class="d-flex">
              <h2 class="flex-grow-1 mb-2 text-primary"><b>My Skills</b></h2>
              <div class="mb-2">
                <a href="/my_program" class="btn btn-outline-primary d-none btn-save1" data-bs-toggle="modal" data-bs-target="#modal">
                  Save
                </a>
                <a class="btn btn-outline-primary btn-add" >
                  Add Skills
                </a>
              </div>
            </div>
            <hr class="profile-hr" />
            <div class="col-12">
              <div class="row details">
                <div class="col ">
                  <div class="row px-5 details-con">
                    <!-- <center class="text-danger">No skills found.</center> -->
                    <div class="collapse" id="collapse">
                      <div class="card card-body">
                        <strong class="mb-2">Select skills to add:</strong>
                        <div class="all-skill skill-flex">
                        
                        </div>
                      </div>
                    </div>
                    
                    
                  </div>  




                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- main body-->
          <!-- main body-->
          <!-- main body-->
          <!-- main body-->
          <!-- main body-->
          <!-- main body-->
          <!-- main body-->
        </div>
      </div>
    </div>

    <script src="../script/bootstrap.bundle.min.js"></script>

    <script src="../script/jquery-3.7.1.min.js"></script>
    <script src="../script/script.js"></script>
    <script src="../script/skills.js"></script>
    <script>
      $(document).ready(function () {
        on_page_load(['Student']);
      });
    </script>
  </body>
</html>
 