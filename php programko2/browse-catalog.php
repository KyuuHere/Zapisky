<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Browse catalog</title>
</head>
<body>
    <h1>Browse catalog</h1>
    <p>Here you can browse the catalog of available files.</p>
    <?php
    # List files in the "files" directory with download buttons
    $files = scandir('files');
    foreach ($files as $file) {
        if ($file !== '.' && $file !== '..') {
            $filePath = "files/$file";
            $fileExtension = strtolower(pathinfo($file, PATHINFO_EXTENSION));
            $imageExtensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp'];
            
            echo "<p>";
            if (in_array($fileExtension, $imageExtensions)) {
                echo "<img src='$filePath' alt='$file' style='max-width: 100px; max-height: 100px; margin-right: 10px;'>";
            }
            echo "$file <a href='$filePath' download>Download</a></p>";

        }
    }
    ?>
    <button onclick="window.location.href='index.html'">Back</button>
</body>
</html>