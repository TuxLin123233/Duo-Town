# 自动化删除组件+页面程序

echo "警告! 该程序会删除某些重要文件!!!请谨慎操作!!!"
read -r -p "请输入要删除的组件名：" name
first_char_uppercase="${name^}"

# 进入pages/文件夹
cd ../pages/ || exit
rm -r "$name"

cd "../src/views/" || exit
rm -r "$first_char_uppercase"

echo "($name)组件已删除成功!"