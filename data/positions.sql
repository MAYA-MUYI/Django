
DROP TABLE IF EXISTS `positions`;
CREATE TABLE `positions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cate_name` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `job_name` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `salary_range` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `working_city` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `experience_required` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL,
  `education_required` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL,
  `job_type` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `position_label` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL,
  `publish_time` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `job_advantage` text CHARACTER SET utf8mb4,
  `job_detail` text CHARACTER SET utf8mb4 NOT NULL,
  `working_address` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `company_lagou_url` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `company_name` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `company_field` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `financing_status` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL,
  `company_size` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL,
  `company_url` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cate_name` (`cate_name`)
) ENGINE=InnoDB AUTO_INCREMENT=6671 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vietnamese_ci;
