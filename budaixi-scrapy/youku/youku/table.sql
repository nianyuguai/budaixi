DROP TABLE IF EXISTS `t_video`;
CREATE TABLE `t_video` (
  `id` varchar(128) NOT NULL COMMENT '视频ID',
  `album_id` varchar(128) NOT NULL COMMENT '视频播单',
  `url` varchar(255) DEFAULT NULL COMMENT '视频URL',
  `title` varchar(255) DEFAULT NULL COMMENT '视频标题',
  `tags` varchar(255) DEFAULT NULL COMMENT '标签id，多个以分号隔开',
  `img_url` varchar(128) DEFAULT NULL COMMENT '图片URL',
  `create_time` timestamp DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY album_id (`album_id`)
) ENGINE=InnoDB CHARSET=utf8;


DROP TABLE IF EXISTS `t_tag`;
CREATE TABLE `t_tag` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '标签id',
  `tag_name` varchar(128) NOT NULL COMMENT '标签名称',
  `tag_type` TINYINT NOT NULL COMMENT '标签类型',
  `create_time` timestamp DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB CHARSET=utf8;


DROP TABLE IF EXISTS `t_scrapy_task`;
CREATE TABLE `t_scrapy_task` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '任务id',
  `domain` varchar(128) NOT NULL COMMENT '域名',
  `start_urls` varchar(255) NOT NULL COMMENT '开始url',
  `url` varchar(255) NOT NULL  COMMENT 'url',
  `album_id` varchar(128) NOT NULL COMMENT '视频播单',
  `rule_id` varchar(128) NOT NULL COMMENT '解析规则id',
  `create_time` timestamp DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB CHARSET=utf8;

