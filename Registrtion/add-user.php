<?php session_strat(); ?>
<?php require_once('inc/connection.php');?>
<?php require_once('inc/functions.php');?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Add New User</title>
        <link rel"stylesheet" href="css/main.css">
</head>
<body>
    <header>
        <div class="appname">User Management System</div>
        <div class="loggedin">Welcome<?php echo $_SESSION['first_name']; ?>! <a href="logout.oho">Log  out</a></div>
    </header>

    <main>
        <h1>Add New User<span><a href="users.php"> < Back to User List</a></span></h1>

        <form action="add-user.php" method="post" class="userform">

            <p>
                <label for="">First Name:</label>
                <input type="text" name="first_name">
            </P>

            <p>
                <label for="">Last Name</label>
                <input type="text" name="last_name">
            </p>

            <p>
                <label for="">Email Address</label>
                <input type="email" name="email">
            </p>

            <p>
                <label for="">New PassWord></label>
                <input type="password name"="password">
            </p>

            <p>
                <label for="&nbsp;"></label>
                <button type="submit" name="submit">Save</button>
            </p>

        </form>
    </main>
</body>
</html>