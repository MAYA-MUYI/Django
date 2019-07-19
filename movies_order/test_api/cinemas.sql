/*
Navicat MySQL Data Transfer

Source Server         : maya
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : movies_vip

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2019-07-17 15:44:26
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `cinemas`
-- ----------------------------
DROP TABLE IF EXISTS `cinemas`;
CREATE TABLE `cinemas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cinema_name` varchar(50) NOT NULL,
  `address` text NOT NULL,
  `price` varchar(2) NOT NULL,
  `city` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of cinemas
-- ----------------------------
INSERT INTO `cinemas` VALUES ('1', '保利万和国际影城(都江堰店)', '都江堰市彩虹大道南段295号（22点后请走斯维登公寓电梯）', '28', '成都');
INSERT INTO `cinemas` VALUES ('2', '天智创客影城(川外店)', '都江堰市大观镇高尔夫大街367号四川外国语大学成都学院33栋百汇园4楼', '30', '成都');
INSERT INTO `cinemas` VALUES ('3', '太平洋电影城(都江堰店)', '都江堰市建设路172号时代春天广场4楼（都江堰古城）', '34', '成都');
INSERT INTO `cinemas` VALUES ('4', '希望电影城', '都江堰市建设路天和盛世4栋3楼（近沃尔玛超市）', '47', '成都');
INSERT INTO `cinemas` VALUES ('5', '横店电影城(百伦广场店)', '都江堰市都江堰大道211号百伦广场7楼', '34', '成都');
INSERT INTO `cinemas` VALUES ('6', 'YOODOO悠渡影城(都江堰店)', '都江堰市都江堰翔凤路168号悦熙广场2层', '47', '成都');
INSERT INTO `cinemas` VALUES ('7', '金逸影城(第六洲店)', '崇州市崇阳大道2199号嘉裕第六洲内', '47', '成都');
INSERT INTO `cinemas` VALUES ('8', '太平洋影城(金鸡店)', '崇州市崇州经济开发区创新路一段1号金鸡生活广场10号', '34', '成都');
INSERT INTO `cinemas` VALUES ('9', '太平洋院线崇州激光影城', '崇州市蜀州中路246号中港城四楼', '47', '成都');
INSERT INTO `cinemas` VALUES ('10', '星美影商城(崇州店)', '崇州市崇庆北路276号', '40', '成都');
INSERT INTO `cinemas` VALUES ('11', '万达影城(崇州唐人街店)', '崇州市崇阳街道唐安东路368号', '29', '成都');
INSERT INTO `cinemas` VALUES ('12', '万达影城(崇州万达广场店)', '崇州市永康东路299号万达广场4楼万达影城', '24', '成都');
INSERT INTO `cinemas` VALUES ('13', '巨洋国际影城', '崇州市蜀州南路59号春熙里', '30', '成都');
INSERT INTO `cinemas` VALUES ('14', '星美国际影商城(成都温江店)', '温江区国色天乡摩天轮商业街12栋购物中心三楼（永辉超市楼上）', '30', '成都');
INSERT INTO `cinemas` VALUES ('15', 'CGV影城(温江店)', '温江区光华大道三段1588号珠江新城国际购物中心4层401室', '24', '成都');
INSERT INTO `cinemas` VALUES ('16', '泽海影城', '温江区文庙街1号楼3楼', '28', '成都');
INSERT INTO `cinemas` VALUES ('17', '太平洋电影城(温江和盛店)', '温江区和盛镇艺苑生活圈2楼（星艺大道南）', '29', '成都');
INSERT INTO `cinemas` VALUES ('18', '澄园国际影城', '温江区南熏大道三段702号', '30', '成都');
INSERT INTO `cinemas` VALUES ('19', '欢乐小马影城', '温江区光华大道1868号德坤新天地2号楼4楼', '28', '成都');
INSERT INTO `cinemas` VALUES ('20', '旭和影城(温江店)', '温江区文化路1号人民商场旁3楼（人民商场对面）', '34', '成都');
INSERT INTO `cinemas` VALUES ('21', '太平洋影城(温江大学城店)', '温江区南熏大道三段855号金强大学城4楼（近大学城）', '30', '成都');
INSERT INTO `cinemas` VALUES ('22', '中影文星国际影城(温江店)', '温江区南浦路西段247号2楼', '40', '成都');
