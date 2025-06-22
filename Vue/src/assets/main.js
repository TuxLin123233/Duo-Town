//页面跳转
import axios from "axios";

export function goTo(target){
    window.location.href = `http://localhost:8000//pages/${target}/${target}.html`;
}

/* 表单发送数据 */
class Submit{
    constructor(){
        this.axios = axios.create({
            baseURL: 'http://localhost:8000',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        })
    }

    async register(target, data){

    }
}
export const submit = new Submit();