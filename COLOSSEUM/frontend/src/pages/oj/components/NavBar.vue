<template>
  <div id="navheader">
    <Menu mode="horizontal" @on-select="handleRoute" active-name="activeMenu" class="oj-menu">
      <div class="logo"><span>{{website.website_name}}</span></div>
      <MenuItem name="/">
        <Icon type="ios-home-outline"></Icon>
        Home
      </MenuItem>
      <MenuItem name="/problems">
        <Icon type="ios-keypad-outline"></Icon>
        Games
      </MenuItem>
      <MenuItem name="/contests">
        <Icon type="ios-trophy-outline"></Icon>
        Contests
      </MenuItem>
      <!-- <MenuItem name="/status">
        <Icon type="ios-pulse-strong"></Icon>
        Status
      </MenuItem> -->
      <Submenu name="3">
        <template slot="title">
          <Icon type="ios-podium-outline"></Icon>
          Rank
        </template>
        <MenuItem name="acm-rank">
          ACM Rank
        </MenuItem>
        <MenuItem name="oi-rank">
          OI Rank
        </MenuItem>
      </Submenu>
      <!-- <Submenu name="">
        <template slot="title">
          <Icon type="information-circled"></Icon>
          About
        </template>
        <MenuItem name="/about">
          Judger
        </MenuItem>
        <MenuItem name="/FAQ">
          FAQ
        </MenuItem>
      </Submenu> -->
      <template v-if="!isAuthenticated">
        <div class="btn-menu">
          <Button 
                  type="default" 
                  ref="loginBtn"
                  shape="circle"
                  @click="handleBtnClick('login')">Login
          </Button>
          <!-- <Button v-if="website.allow_register" -->
          <Button
                  type="default"
                  shape="circle"
                  @click="handleBtnClick('register')"
                  style="margin-left: 5px;">Register
          </Button>
        </div>
      </template>
      <template v-else>
        <Dropdown class="drop-menu" placement="bottom-end" trigger="click">
        <!-- <Dropdown> -->
          <a href="javascript:void(0)" class="drop-menu-title">{{ 'Welcome,'+ user.firstName + ' ' + user.lastName}}
            <Icon type="ios-arrow-down"></Icon>
          </a>
          <DropdownMenu slot="list">
            <DropdownItem>Submissions</DropdownItem>
            <DropdownItem>Settings</DropdownItem>
            <!-- <DropdownItem name="/user-home">Home</DropdownItem>
            <DropdownItem name="/status?myself=1">Submissions</DropdownItem>
            <DropdownItem name="/setting/profile">Settings</DropdownItem>
            <DropdownItem v-if="isAdminRole" name="/admin">Management</DropdownItem>
            <DropdownItem divided name="/logout">Logout</DropdownItem> -->
          </DropdownMenu>
        </Dropdown>
      </template>
    </Menu>
    <Modal v-model="modalVisible" :width="400">
      <div slot="header" class="modal-title">Welcome to {{website.website_name_shortcut}}</div>
      <component :is="modalStatus.mode" v-if="modalVisible"></component>
      <div slot="footer" style="display: none"></div>
    </Modal>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import login from '@oj/views/user/Login'
  import register from '@oj/views/user/Register'

  export default {
    components: {
      login,
      register
    },
    mounted () {
      this.getProfile()
    },
    methods: {
      ...mapActions(['getProfile', 'changeModalStatus']),
      handleRoute (route) {
        if (route && route.indexOf('admin') < 0) {
          this.$router.push(route)
        } else {
          window.open('/admin/')
        }
      },
      handleBtnClick (mode) {
        this.changeModalStatus({
          visible: true,
          mode: mode
        })
      }
    },
    computed: {
      ...mapGetters(['website', 'modalStatus', 'user', 'isAuthenticated', 'isAdminRole']),
      // 跟随路由变化
      activeMenu () {
        return '/' + this.$route.path.split('/')[1]
      },
      modalVisible: {
        get () {
          return this.modalStatus.visible
        },
        set (value) {
          this.changeModalStatus({visible: value})
        }
      }
    }
  }
</script>
<style lang="less" scoped>
  #navheader {
    position: fixed;
    // overflow: hidden; 
    top: 0;
    left: 0;
    height: 60px;
    width: 100%;
    z-index: 1000;
    background-color: #fff;
    box-shadow: 0 1px 5px 0 rgba(0, 0, 0, 0.1);
    .oj-menu {
      background: #fdfdfd;
    }

    .logo {
      margin-left: 2%;
      margin-right: 2%;
      font-size: 20px;
      float: left;
      line-height: 60px;
    }

    .drop-menu {
      float: right;
      margin-right: 40px;
      &-title {
        font-size: 16px;
      }
    }
    .btn-menu {
      font-size: 16px;
      float: right;
      margin-right: 10px;
    }
  }
  .modal {
    &-title {
      font-size: 18px;
      font-weight: 600;
    }
  }
</style>