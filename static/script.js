<script>
        function validateForm() {
            var name = document.forms["userForm"]["name"].value;
            var email = document.forms["userForm"]["email"].value;
            var age = document.forms["userForm"]["age"].value;
            var dob = document.forms["userForm"]["dob"].value;
            var emailRegex = /^\S+@\S+\.\S+$/;

            if (name == "") {
                alert("Name must be filled out");
                return false;
            }

            if (!emailRegex.test(email)) {
                alert("Invalid email format");
                return false;
            }

            if (isNaN(age) || age <= 0) {
                alert("Age must be a positive number");
                return false;
            }

            return true;
        }
    </script>