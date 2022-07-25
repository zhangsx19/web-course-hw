import { createStore } from 'vuex'
import ModuleUser from './user';

export default createStore({
  //定义变量
  state: {

  },
  //getters存储需要计算的变量
  getters: {
  },
  //mutations不能执行异步
  mutations: {

  },
  //定义对state的各种操作,所有修改操作必须放到mutations里
  actions: {

  },
  modules: {
    user: ModuleUser,
  }
});
