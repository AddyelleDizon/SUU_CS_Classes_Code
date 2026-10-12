<?php
    $devices = [
        [
            "name" => "Device A",
            "info" => "This is a test paragraph for a specific device.",
            "more" => "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        ],
        [
            "name" => "Device B",
            "info" => "This is the other test paragraph for the other device.",
            "more" => "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        ]
    ];
?>
<!DOCTYPE html>
<html>
<head>
    <title>Device Comparison</title>
    <link rel="stylesheet" href="external/styles.css">
</head>

<body>
    <header>
        <h1 id="mainTitle"><a class="title" href="index.php">Title In Works</a></h1>
    </header>
    
    <ul>
        <li><a href="index.php">Home</a></li>
        <li><a href="devices.php">More Devices</a></li>
        <li><a href="about.php">About Us</a></li>
        <li><a href="login.php">Login</a></li>
    </ul>

    <div>
        <video width="1280" height="720" controls>
            <source src="media/Macromolecules.mp4" type="video/mp4">
            <source src="media/Macromolecules.ogg" type="video/ogg">
        </video>

        <div class="container">
            <div class="leftHalf" id="leftDev">
                <h2><?php echo htmlspecialchars($devices[0]['name']); ?></h2>
                <p id="leftDevInfo"><?php echo htmlspecialchars($devices[0]['info']); ?></p>
                <p id="leftDevInfoMore"><?php echo htmlspecialchars($devices[0]['more']); ?></p>
                <button type="button" onclick="changeInfoLeft()">Click For More Info!</button>
            </div>

            <div class="rightHalf" id="rightDev">
                <h2><?php echo htmlspecialchars($devices[1]['name']); ?></h2>
                <p id="rightDevInfo"><?php echo htmlspecialchars($devices[1]['info']); ?></p>
                <p id="rightDevInfoMore"><?php echo htmlspecialchars($devices[1]['more']); ?></p>
                <button type="button" onclick="changeInfoRight()">Click For More Info!</button>
            </div>
        </div>
    </div>
</body>

<footer>
    <p id="trademark">Device Comparison&trade; of Addyelle Kein J. Dizon</p>
    <script src="external/javascript.js"></script>
</footer>

</html>