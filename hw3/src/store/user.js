import $ from 'jquery';
const ModuleUser = {
    state: {
        username: "",
        password: "",
        usage: 0,
        is_login: false,
    },

    //getters存储需要计算的变量
    getters: {
    },
    //mutations不能执行异步
    mutations: {
        updateUser(state, user) {
            state.username = user.username;
            state.password = user.password;
            state.usage = user.usage;
            state.is_login = user.is_login;
        },
        logout(state) {
            state.username = "";
            state.password = "";
            state.usage = 0;
            state.is_login = false;
        }
    },

    //定义对state的各种操作,所有修改操作必须放到mutations里
    actions: {
        login(context, data) {
            $.ajax({
                url: "http://127.0.0.1:5000/login",
                type: "POST",
                data: JSON.stringify({
                    username: data.username,
                    password: data.password,
                }),
                dataType: "json",
                success(resp) {
                    console.log(resp);
                    context.commit("updateUser", {
                        username: resp.username,
                        password: resp.password,
                        usage: resp.usage,
                        is_login: true,
                    });
                    data.success();
                },
                error() {
                    data.error();
                }
            });
        },
        logout(context, data) {
            $.ajax({
                url: "http://127.0.0.1:5000/logout",
                type: "POST",
                data: JSON.stringify({
                    username: data.username,
                }),
                dataType: "json",
                success(resp) {
                    console.log(resp);
                    context.commit("logout");
                    data.success();
                },
                error() {
                    data.error();
                }
            });
        },
    },

    modules: {

    }
};
export default ModuleUser;