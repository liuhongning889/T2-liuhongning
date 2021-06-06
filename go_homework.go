package main
import (
	"fmt"
	"time")

func main() {
	now := time.Now()
	sec := now.Unix()
	fmt.Println(now) // 当前服务器时间
	fmt.Println(sec) //返回当前服务器的时间戳

}
