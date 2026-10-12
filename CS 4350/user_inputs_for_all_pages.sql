
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;


CREATE TABLE `user_inputs_for_all_pages` (
  `id` int(2) DEFAULT NULL,
  `variable_name` varchar(31) DEFAULT NULL,
  `page` int(1) DEFAULT NULL,
  `page_order` int(1) DEFAULT NULL,
  `text_for_display` varchar(51) DEFAULT NULL,
  `html_input_selector` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;


INSERT INTO `user_inputs_for_all_pages` (`id`, `variable_name`, `page`, `page_order`, `text_for_display`, `html_input_selector`) VALUES
(1, 'first_name', 1, 1, 'First Name', 'text'),
(2, 'last_name', 1, 2, 'Last Name', 'text'),
(3, 'move_in_date', 1, 3, 'Move in Date', 'date'),
(4, 'major', 1, 4, 'Which major are you planing on selecting?', 'select'),
(5, 'completed_registration', 2, 1, 'I completed registration', 'checkbox'),
(6, 'found_dorm_room', 2, 2, 'I found my dorm room', 'checkbox'),
(7, 'found_cafeteria', 2, 3, 'I found the cafeteria', 'checkbox'),
(8, 'made_a_friend', 2, 4, 'I made a friend', 'checkbox'),
(9, 'paid_tuition', 2, 5, 'I paid my tuition', 'checkbox'),
(10, 'degree_selected', 2, 6, 'I have selected the following degree', 'radio'),
(11, 'hogwarts_house', 2, 7, 'My Hogwarts House is:', 'select'),
(12, 'favorite_harry_potter_character', 2, 8, 'My Favorite Harry Potter Character is:', 'radio'),
(13, 'birthday_as_week_year', 3, 1, 'Birthday (month and year):', 'month'),
(14, 'color_enjoyed', 3, 2, 'Select a color you enjoy:', 'color'),
(15, 'favorite_day_this_month', 3, 3, 'What day was your favorite this month?', 'number'),
(16, 'school_email', 3, 4, 'Enter your school email (.edu):', 'email'),
(17, 'personal_email', 3, 5, 'Enter your personal email (not .edu):', 'email'),
(18, 'secret_code', 4, 1, 'Please create a secret code:', 'password'),
(19, 'secret_code_verification', 4, 2, 'Verify Secret Code:', 'password'),
(20, 'suu_website_rating', 4, 3, 'How would you rate your current website experience?', 'range'),
(21, 'prefered_time_to_meet_advisor', 4, 4, 'Select a time you would like to see an advisor:', 'time'),
(22, 'favorite_webpage', 4, 5, 'What is your favorite webpage:', 'url'),
(23, 'favorite_week_of_year', 4, 6, 'What is your favorite week of the year?', 'week');
COMMIT;
