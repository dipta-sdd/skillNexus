<?php
$servername = "localhost"; // Your database server
$username = "sankarsa_dhruba"; // Your database username
$password = "Spider@2580"; // Your database password
$dbname = "sankarsa_dhruba"; // Your database name
header("Access-Control-Allow-Origin: *");

// Allow specific HTTP methods
header("Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE, PUT");

// Allow specific headers
header("Access-Control-Allow-Headers: Content-Type, Authorization");
echo ""sdfgfgfgfgfgfgfgfgfgfgfgfgfgfgfgfgfgfgfg;
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Get data from POST request
    echo 'hhhhhhhhhhh';
    echo $sender;
    $sender = $_POST['sender'];
    echo $sender;
    $interest = $_POST['interest'];
    $email = $_POST['email'];

    // Prepare and bind
    $stmt = $conn->prepare("INSERT INTO message (sender, interest, email) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $sender, $interest, $email);

    // Execute the statement
    if ($stmt->execute()) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the statement
    $stmt->close();
} else {
    echo "No data posted";
}
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// SQL query to check if the table exists
$checkTableQuery = "SHOW TABLES LIKE 'message'";
$result = $conn->query($checkTableQuery);

if ($result->num_rows == 0) {
    // Table does not exist, create the table
    $createTableQuery = "CREATE TABLE message (
        id INT AUTO_INCREMENT PRIMARY KEY,
        sender VARCHAR(255) NOT NULL,
        interest VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
    )";

    if ($conn->query($createTableQuery) === TRUE) {
        // echo "Table 'message' created successfully<br>";
    } else {
        die("Error creating table: " . $conn->error);
    }
} 
// Check if data is sent via POST method
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Get data from POST request
    echo $sender;
    $sender = $_POST['sender'];
    echo $sender;
    $interest = $_POST['interest'];
    $email = $_POST['email'];

    // Prepare and bind
    $stmt = $conn->prepare("INSERT INTO message (sender, interest, email) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $sender, $interest, $email);

    // Execute the statement
    if ($stmt->execute()) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the statement
    $stmt->close();
} else {
    echo "No data posted";
}

// Close connection
$conn->close();
?>
