import types from '../types'
import api from '@oj/api'
import storage from '@/utils/storage'
import { STORAGE_KEY, USER_TYPE, PROBLEM_PERMISSION } from '@/utils/constants'

const state = {
  profile: {
    // user:{}
  }
}

const getters = {
  // user: state => state.profile.user || {},
  user: state => state.profile || {},
  profile: state => state.profile,
  isAuthenticated: (state, getters) => {
    return !!getters.user.username
  },
  isAdminRole: (state, getters) => {
    return getters.user.admin_type === USER_TYPE.ADMIN ||
      getters.user.admin_type === USER_TYPE.SUPER_ADMIN
  },
  isSuperAdmin: (state, getters) => {
    return getters.user.admin_type === USER_TYPE.SUPER_ADMIN
  },
  hasProblemPermission: (state, getters) => {
    return getters.user.problem_permission !== PROBLEM_PERMISSION.NONE
  }
}

const mutations = {
  [types.CHANGE_PROFILE] (state, {profile}) {
    state.profile = profile
    storage.set(STORAGE_KEY.AUTHED, !!profile.user)
  }
}

const actions = {
  // getProfile (username) {
    // api.getUserInfo({"username":"abc"})
  getProfile ({commit},username) {
      api.getUserInfo({"username":username}).then(res => {
      commit(types.CHANGE_PROFILE, {
        profile : res.data || {}
      })
      console.log(state.profile.firstName)
    })
  },
  clearProfile ({commit}) {
    commit(types.CHANGE_PROFILE, {
      profile: {}
    })
    storage.clear()
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}

// let obj = {
//   str: "ASA",
//   ass: "ass"
// }

// let str = obj.str

// {str, ass}=bj