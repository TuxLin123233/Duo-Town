/* Axios配置 */
import axios from 'axios'

/* 表单发送数据 */
class Submit{
    constructor(){
        axios.defaults.xsrfCookieName = 'csrftoken';
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';
        axios.defaults.withCredentials = true; // 允许携带 Cookie

        this.api_url = 'http://127.0.0.1:8000/';
    }
    async register(target, data){
        try {
            const response = await axios.post(
                `${this.api_url}/api/${target}`,
                data,
                {
                    headers:{
                        'Accept': 'application/json',
                    }
                }
            )
        }catch (error) {
            console.log(error);
        }
    }
}
export const submit = new Submit();
