
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


CREATE TABLE `info_for_select_and_radio_input` (
  `id` int(2) DEFAULT NULL,
  `selector` varchar(14) DEFAULT NULL,
  `option` varchar(31) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;


INSERT INTO `info_for_select_and_radio_input` (`id`, `selector`, `option`) VALUES
(1, 'hogwarts_house', 'Gryffindor'),
(2, 'hogwarts_house', 'Hufflepuff'),
(3, 'hogwarts_house', 'Ravenclaw'),
(4, 'hogwarts_house', 'Slytherin'),
(5, 'major', 'Accounting'),
(6, 'major', 'Agriculture'),
(7, 'major', 'Anthropology'),
(8, 'major', 'Area/Group Studies'),
(9, 'major', 'Art & Art History'),
(10, 'major', 'Arts Administration'),
(11, 'major', 'Aviation'),
(12, 'major', 'Biology'),
(13, 'major', 'Business'),
(14, 'major', 'Chemistry'),
(15, 'major', 'Communication'),
(16, 'major', 'Computer Science'),
(17, 'major', 'Construction'),
(18, 'major', 'Criminal Justice'),
(19, 'major', 'Cybersecurity'),
(20, 'major', 'Dance'),
(21, 'major', 'Data Science'),
(22, 'major', 'Economics'),
(23, 'major', 'Education'),
(24, 'major', 'Engineering'),
(25, 'major', 'English'),
(26, 'major', 'Environmental Studies'),
(27, 'major', 'Exercise Science'),
(28, 'major', 'Family Life & Human Development'),
(29, 'major', 'Film'),
(30, 'major', 'Finance'),
(31, 'major', 'General Studies'),
(32, 'major', 'Geography'),
(33, 'major', 'Geology'),
(34, 'major', 'Graphic Design'),
(35, 'major', 'Health Sciences'),
(36, 'major', 'History'),
(37, 'major', 'Hospitality Management'),
(38, 'major', 'Information Technology'),
(39, 'major', 'Interdisciplinary Studies'),
(40, 'major', 'Languages'),
(41, 'major', 'Leadership'),
(42, 'major', 'Library Media/School Library'),
(43, 'major', 'Management'),
(44, 'major', 'Marketing'),
(45, 'major', 'Mathematics'),
(46, 'major', 'Military Science'),
(47, 'major', 'Music'),
(48, 'major', 'Nursing'),
(49, 'major', 'Nutrition'),
(50, 'major', 'Outdoor Recreation'),
(51, 'major', 'Philosophy'),
(52, 'major', 'Physical Education'),
(53, 'major', 'Physics'),
(54, 'major', 'Political Science'),
(55, 'major', 'Psychology'),
(56, 'major', 'Public Administration'),
(57, 'major', 'Secondary Education'),
(58, 'major', 'Social Studies'),
(59, 'major', 'Social Work'),
(60, 'major', 'Sociology'),
(61, 'major', 'Software Development'),
(62, 'major', 'Sports'),
(63, 'major', 'Theatre'),
(64, 'hp_character', 'Harry Potter'),
(65, 'hp_character', 'Hermione Granger'),
(66, 'hp_character', 'Albus Dumbledore'),
(67, 'hp_character', 'Cho Chang'),
(68, 'hp_character', 'Luna Lovegood'),
(69, 'hp_character', 'Draco Malfoy'),
(70, 'hp_character', 'A character not listed');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
