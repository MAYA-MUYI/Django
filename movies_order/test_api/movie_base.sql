/*
Navicat MySQL Data Transfer

Source Server         : maya
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : movies_vip

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2019-07-17 15:44:33
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `movie_base`
-- ----------------------------
DROP TABLE IF EXISTS `movie_base`;
CREATE TABLE `movie_base` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `movie_name` varchar(20) NOT NULL,
  `ellipsis` varchar(100) NOT NULL,
  `time` varchar(20) NOT NULL,
  `vision` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of movie_base
-- ----------------------------
INSERT INTO `movie_base` VALUES ('1', '5月天诺亚方舟', 'Mayday nowhere 3D', '2013-09-19', '3D');
INSERT INTO `movie_base` VALUES ('2', '厉鬼将映', 'โปรแกรมหน้า วิญญาณอาฆาต', '2008-10-30', '');
INSERT INTO `movie_base` VALUES ('3', '哥斯拉2：怪兽之王', 'Godzilla: King of the Monsters', '2019-05-31', '3DIMAX');
INSERT INTO `movie_base` VALUES ('4', '战狼', 'Wolf Warriors', '2015-04-02', '3D');
INSERT INTO `movie_base` VALUES ('5', '潜艇总动员：外星宝贝计划', 'Happy Little Submarine：Space Pals', '2019-06-01', '3D');
INSERT INTO `movie_base` VALUES ('6', '忠烈杨家将', 'Saving General Yang', '2013-04-04', '');
INSERT INTO `movie_base` VALUES ('7', '卡拉斯：为爱而声', 'Maria by Callas', '2019-05-31', '');
INSERT INTO `movie_base` VALUES ('8', '花儿与歌声', 'Flowers and songs', '2019-05-31', '');
INSERT INTO `movie_base` VALUES ('9', '尺八·一声一世', 'One Sound, One Life', '2019-05-31', '');
INSERT INTO `movie_base` VALUES ('10', '好小子，好功夫', 'Good boy and kongfu', '2019-05-31', '');
INSERT INTO `movie_base` VALUES ('11', '夏洛特烦恼', 'Goodbye Mr. Loser,Xia Luo Te Fan Nao', '2015-09-30', '');
INSERT INTO `movie_base` VALUES ('12', '托马斯大电影之世界探险记', 'Thomas & Friends: Big World! Big Adventures! The Movie', '2019-05-31', '');
INSERT INTO `movie_base` VALUES ('13', '西游记之大圣归来', 'Monkey King: Hero is Back', '2015-07-10', '3D');
INSERT INTO `movie_base` VALUES ('14', '唐人街探案', 'Detective Chinatown', '2015-12-31', '');
INSERT INTO `movie_base` VALUES ('15', '追龙Ⅱ', 'Chasing the Dragon Ⅱ', '2019-06-06', '');
INSERT INTO `movie_base` VALUES ('16', '五月天人生无限公司', 'Mayday Life', '2019-05-24', '3D');
INSERT INTO `movie_base` VALUES ('17', '一条狗的使命2', 'A Dog\'s Journey', '2019-05-17', '');
INSERT INTO `movie_base` VALUES ('18', '大侦探皮卡丘', 'POKÉMON Detective Pikachu', '2019-05-10', '3DIMAX');
INSERT INTO `movie_base` VALUES ('19', 'X战警：黑凤凰', 'X-Men: Dark Phoenix', '2019-06-06', '3DIMAX');
INSERT INTO `movie_base` VALUES ('20', '哆啦A梦：大雄的月球探险记', '映画ドラえもん のび太の月面探査記', '2019-06-01', '');
INSERT INTO `movie_base` VALUES ('21', '阿拉丁', 'Aladdin', '2019-05-24', '3DIMAX');
