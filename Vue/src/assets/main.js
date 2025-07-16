import axios from "axios";


//页面跳转
export function goTo(target, alert=null) {
    if (alert !== null) {
        window.alert(alert);
    }
    window.location.href = getUrl(target);
}

//提示
export function alert(message){
    window.alert(message)
}

//快捷获取URL
function getUrl(target){
    return `http://localhost:8080/pages/${target}/${target}.html`
}

//设置指定ID的内容
function setContent(id_name, content){
    document.getElementById(id_name).setHTMLUnsafe(content)
}

//设置头像
function setHeadshot(name){
    document.getElementById('headshot').src = `http://localhost:8000/api/image/headshot/${name}`;
}

/* 发送数据类 */
class Basic{
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
        return true;
    }

    //判断登录状态
    async is_logged(){
        //适用于所有页面, 每个vue文件必须含有此项!!!
        await this.axios({
            method: 'get',
            url: 'api/check_session/'
        }).then((request) => {
            const url = window.location.href;   //获取当前的URL地址
            if (request.data['message'] === 'logged_in'){   // 如果登录好
                if (url === getUrl("register") || url === getUrl("login")){
                    //如果处于登录或者注册页面
                    goTo("me", "欢迎加入Duo小镇！");
                }
                //如果处于非公开页面，则不做任何事情
            }else if(request.data['message'] === 'not_logged_in'){  // 没有登录，转到注册页面
                if (url !== getUrl("register") && url !== getUrl("login")){     //如果都不在登录和注册页面
                    goTo("register", "没有权限访问该页面, 因为你并没有登录！");
                }
            }
        })
    }

    //获取CSRF_TOKEN
    async get_token(){
         await this.axios({
            method: 'get',
            url: 'api/csrf/'
        }).then((request) => {
            this.csrf_token = request.data['csrf'];
         })
    }
}

class View extends Basic{
    constructor() {
        super();
        this.get_token().then();
    }

    //注册操作
    async register(data){
        if (! this.canSend()){ return; }     // 防抖处理

        await this.axios({
            method: 'post',
            url: 'api/add_user/',
            headers: {
                'X-CSRFToken': this.csrf_token
            },
            data: data
        }).then((request) => {      // 成功后跳转到登录页面
            if (request.data['message'] === 'success'){
                // 跳转到登录页面
                goTo("login", "注册成功! 为你跳转到登录页面");
            }
            else if(request.data['message'] === 'repeat'){
                // 用户名重复
                window.alert("已有该帐号！")
            }else if (request.data['message'] === 'password_error'){
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
            url: 'api/check_user/',
            headers: {
                'X-CSRFToken': this.csrf_token
            },
            data: data
        }).then((request) => {
            if (request.data['message'] === 'success'){
                //跳转到个人主页
                goTo("me", "登录成功! 欢迎加入Duo小镇！");
            }else if (request.data['message'] === 'no_user'){
                window.alert("你还没登录! ")
            }else if (request.data['message'] === 'password_error'){
                window.alert("密码错误! ")
            }
        })
    }

    async get_user_data(content){
        this.axios({
            method: 'get',
            url: 'api/get_user/',
            headers: {
                'X-CSRFToken': this.csrf_token
            }
        }).then((request) => {
            const data = request.data;
            for (let i = 0; i < content.length; i++) {
                if (content[i] === 'age'){
                    setContent(content[i], `${data[content[i]]} 岁`);
                    continue;
                }
                setContent(content[i], data[content[i]]);
            }
            if (request.data['headshot'] !== "U"){
                setHeadshot(data['headshot']);
            }
        })
    }

    async add_blog(data){
        this.axios({
            method: 'post',
            url: 'api/add_blog',
            headers: {
                'X-CSRFToken': this.csrf_token
            },
            data: data
        }).then((request) => {
            if (request.data['message'] === 'blog_added'){
                goTo("me", "文章发送成功!")
            }
        })
    }
}


export const basic_api = new Basic();
export const view_api = new View();