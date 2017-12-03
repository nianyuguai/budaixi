DROP TABLE IF EXISTS `t_video`;
CREATE TABLE `t_video` (
  `id` varchar(128) NOT NULL,
  `album_id` varchar(128) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `url` varchar(128) DEFAULT NULL,
  `img_url` varchar(128) DEFAULT NULL,
  `create_time` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY album_id (`album_id`)
) ENGINE=InnoDB CHARSET=utf8;