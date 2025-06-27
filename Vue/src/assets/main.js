//页面跳转
import axios from "axios";

export function goTo(target, alert=null) {
    if (alert !== null) {
        window.alert(alert);
    }
    window.location.href = `http://localhost:8080/pages/${target}/${target}.html`;
}

/* 表单发送数据 */
class Submit{
    constructor(){
        this.csrf_token = null;     // CSRFToken

        // 创建Axios对象
        this.axios = axios.create({
            baseURL: 'http://localhost:8000',
            withCredentials: true,   // 允许携带Cookie
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }
        })

        // 记录最后一次请求的时间戳
        this.lastRequestTime = 0;
        this.get_token().then(r => {});
    }

    // 检查是否允许发送请求(防抖)
    canSend(){
        const now = Date.now();     //获取此刻时间
        if (now - this.lastRequestTime < 10000){
            window.alert("操作太频繁，请10秒后再试！")
            return false;
        }

        //更新时间戳
        this.lastRequestTime = now;
        return true
    }

    //获取CSRF_TOKEN
    async get_token(){
         await this.axios({
            method: 'get',
            url: 'api/csrf'
        }).then((request) => {
            this.csrf_token = request.data['csrf'];
         })
    }

    //注册操作
    async register(data){
        if (! this.canSend()){ return; }    // 防抖处理

        await this.axios({
            method: 'post',
            url: 'api/add_user',
            headers: {
                'X-CSRFToken': this.csrf_token
            },
            data: data
        }).then((request) => {      // 成功后跳转到登录页面
            if (request.data['status'] === 200){
                // 跳转到登录页面
                goTo("login", "注册成功! 为你跳转到登录页面");
            }
            else if(request.data['status'] === 'repeat'){
                // 用户名重复
                window.alert("已有该帐号！")
            }else if (request.data['status'] === 'password_error'){
                // 密码太短
                window.alert("密码太短！")
            }
        })
    }

    //登录操作
    async login(data){
        if (! this.canSend()){ return; }     // 防抖处理
        await this.axios({
            method: 'post',
            url: 'api/check_user',
            headers: {
                'X-CSRFToken': this.csrf_token
            },
            data: data
        }).then((request) => {
            if (request.data['status'] === 200){
                //跳转到个人主页
                goTo("me", "登录成功!");
            }else if (request.data['status'] === 'no_user'){
                window.alert("你还没登录! ")
            }else if (request.data['status'] === 'password_error'){
                window.alert("密码错误! ")
            }
        })
    }
}
export const submit = new Submit();