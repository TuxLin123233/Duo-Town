/* Axios配置 */
import axios from 'axios'


//页面跳转
export function goTo(target){
    window.location.href = `http://127.0.0.1:8080//pages/${target}/${target}.html`;
}

async function getCsrfToken() {
    try {
       await axios.get(`http://127.0.0.1:8000//api/csrf`)
    } catch (error) {
        console.log(error)
    }
}

/* 表单发送数据 */
class Submit{
    constructor(){
        axios.defaults.xsrfCookieName = 'csrftoken';
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';
        axios.defaults.withCredentials = true; // 发送时自动携带Cookie

        this.website_url = 'http://127.0.0.1:8000/';

        getCsrfToken().then(() => {console.log("CSRF 设置成功")});
    }

    async register(target, data){
        try {
            const response = await axios.post(
                `${this.website_url}/api/${target}`,
                data,
                {
                    headers:{
                        'Accept': 'application/json',
                        'Content-Type': 'application/json',
                    },
                },
            )
            if (response.data.message === 'repeat_username'){
                window.alert("已有该用户名!")
            }else if (response.data.message === 'ok'){
                window.alert("注册成功！");
                goTo('login');
            }else if (response.data.message === 'short_password'){
                window.alert("密码太短!")
            }
        }catch (error) {
            console.log(error);
        }
    }
}
export const submit = new Submit();