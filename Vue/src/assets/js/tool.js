//页面跳转
export function goTo(target, alert=null) {
    if (alert !== null) {
        window.alert(alert);
    }
    window.location.href = getUrl(target);
}

export function alert(content){
    window.alert(content);
}

//快捷获取URL
export function getUrl(target){
    return `http://localhost:8080/pages/${target}/${target}.html`
}

//设置指定ID的内容
export function setContent(id_name, content){
    document.getElementById(id_name).setHTMLUnsafe(content)
}

//设置头像
export function setHeadshot(name){
    document.getElementById('headshot').src = `http://localhost:8000/api/image/headshot/${name}`;
}

//获取头像图片路径
export function getHeadshotUrl(name){
    return `http://localhost:8000/api/image/headshot/${name}`
}