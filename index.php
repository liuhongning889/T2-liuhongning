<?php

$data = array('code'=>10000);

//模拟 登录
$username = trim($_REQUEST['username']); //账号
$password = trim($_REQUEST['password']);//密码
// 如果是ajax  请求   可以返回 json    使用  json_encode();
if(empty($username)){
    $data['code'] = '10001';
    $data['res'] = '账号不课为空';
    exit(json_encode($data));
};
if(empty($password)){exit('密码不可为空');};
//  模拟账号密码登录  查询数据库
if($username !='admin'  && $password!='123456')  exit('账号或密码错误');
$id = 1;
$_SESSION['id'] = $id;

//  模拟 模拟登录  保存$_SESSION  执行跳转
exit('登录成功');

