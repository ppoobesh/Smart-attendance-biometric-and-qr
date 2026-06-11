-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 27, 2025 at 07:15 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `studentqrcode`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `id` int(50) NOT NULL auto_increment,
  `date` varchar(50) NOT NULL,
  `regno` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `intime` varchar(50) NOT NULL,
  `outtime` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`id`, `date`, `regno`, `name`, `intime`, `outtime`, `status`) VALUES
(1, '2025-05-07', '123456', 'sundar', '13:57:23.289131', '', 'present');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` int(10) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `address` varchar(100) NOT NULL,
  `password` varchar(10) NOT NULL,
  `otp` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `name`, `gender`, `email`, `phone`, `address`, `password`, `otp`) VALUES
(1, 'sam', 'male', 'sundarv06@gmail.com', '7904461600', 'trichy', 'admin', ''),
(2, 'pandiyan', 'male', 'sundarv06@gmail.com', '7904461600', 'trichy', 'admin12', ''),
(3, 'sample', 'male', 'sundarv06@gmail.com', '9840234119', 'trichy', 'admin1', ''),
(4, 'sundar', 'male', 'sundarv06@gmail.com', '7904461600', 'trichy', 'admin3', ''),
(5, 'sundar', 'male', 'sundarv06@gmail.com', '7904461600', 'trichy', '12345', '4209'),
(6, 'sample', 'male', 'sundarv06@gmail.com', '7904461600', 'trichy', 'sample', ''),
(7, 'sundar', 'male', 'sundarv06@gmail.com', '7904461600', 'trichy', '1234567890', '1144'),
(8, 'sundar', 'male', 'sundarv06@gmail.com', '7904461600', 'trichy', '123456', '3425');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` int(50) NOT NULL auto_increment,
  `regno` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `emailid` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `year` varchar(100) NOT NULL,
  `profileimage` varchar(100) NOT NULL,
  `qrimage` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `regno`, `name`, `gender`, `dob`, `emailid`, `phone`, `address`, `department`, `year`, `profileimage`, `qrimage`) VALUES
(1, '123456', 'sundar', 'male', '2025-05-07', 'sundarv06@gmail.com', '7904461600', 'trichy', 'MSC', '2', 'user_img.jpg', '123456.png');
