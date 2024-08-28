require 'vendor/autoload.php';

use PDFParser\Parser;

function extractTableRows($pdfFile) {
$parser = new Parser();
$pdfText = $parser->parseFile($pdfFile);

$allRows = [];

foreach ($pdfText as $page) {
// Assuming you have a function to detect tables in a page
$tables = detectTables($page);

foreach ($tables as $table) {
$rows = extractRowsFromTable($table);
$allRows = array_merge($allRows, $rows);
}
}

return $allRows;
}

// Function to detect tables in a page (replace with your logic)
function detectTables($page) {
// ...
}

// Function to extract rows from a table (replace with your logic)
function extractRowsFromTable($table) {
// ...
}

// Example usage
$pdfFile = 'sum23.pdf';
$allRows = extractTableRows($pdfFile);

print_r($allRows);