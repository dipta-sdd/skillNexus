
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

    case 'experience' :
        require __DIR__ . '/views/experience.php';
        break;
    case 'manage_education' :
        require __DIR__ . '/views/manage_education.php';
        break;
    case 'training' :
        require __DIR__ . '/views/training.php';
        break;
    default:
            http_response_code(404);
        require __DIR__ . '/views/404.php';
        
        break;
}

?>