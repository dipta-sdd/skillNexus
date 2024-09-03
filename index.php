
<?php

$request =  trim($_SERVER['REQUEST_URI'], '/');
$requests= explode('?',$request);
// echo $_SERVER['REQUEST_URI'];
switch ($requests[0]) {
    case '/' :
        require __DIR__ . '/views/home.html';
        break;
    case '' :
        require __DIR__ . '/views/home.html';
        break;
    case 'login' :
        require __DIR__ . '/views/login.php';
        break;
    case 'signup' :
        require __DIR__ . '/views/reg.php';
        break;
    case 'profile' :
        require __DIR__ . '/views/profile.php';
        break;
    case 'profile2' :
        require __DIR__ . '/views/profile2.php';
        break;
    case 'education' :
        require __DIR__ . '/views/education.php';
        break;
    case 'my_skills' :
        require __DIR__ . '/views/skills.php';
        break;
    case 'experience' :
        require __DIR__ . '/views/experience.php';
        break;
    case 'manage_education' :
        require __DIR__ . '/views/manage_education.php';
        break;
    case 'training' :
        require __DIR__ . '/views/training.php';
        break;
    case 'programs' :
        require __DIR__ . '/views/programs.php';
        break;
    case 'users' :
        require __DIR__ . '/views/users.php';
        break;
    // -------------------------------------------------------------------------------


    // case 'lecture_up' :
    //     require __DIR__ . '/views/programs.php';
    //     break;
    case 'program' :
        require __DIR__ . '/views/program.php';
        break;
        
    case 'lecture_up' :
            require __DIR__ . '/views/lecture_up.php';
            break;
    
    case 'all_course_detail' :
                require __DIR__ . '/views/all_course_detail.php';
                break;
    case 'course_detail' :
                require __DIR__ . '/views/course_detail.php';
                 break;
    case 'course_list' :
          require __DIR__ . '/views/course_list.php';
           break;
    case 'course_list_single' :
            require __DIR__ . '/views/course_list_single.php';
             break;
    case 'edit_detail' :
             require __DIR__ . '/views/edit_detail.php';
            break;
    case 'edit_video' :
             require __DIR__ . '/views/edit_video.php';
            break;
    case 'create_course' :
            require __DIR__ . '/views/create_course.php';
            break;
    case 'lec_detail' :
        require __DIR__ . '/views/lec_detail.php';
        break;
    case 'student_view_lec_detail' :
        require __DIR__ . '/views/student_view_lec_detail.php';
        break;
    case 'training' :
        require __DIR__ . '/views/training.php';
        break;
    case 'videoshow' :
            require __DIR__ . '/views/videoshow.php';
            break;
    case 'allvideoshow' :
            require __DIR__ . '/views/allvideoshow.php';
            break;
    default:
            http_response_code(404);
        require __DIR__ . '/views/404.php';
        
        break;
}

?>
