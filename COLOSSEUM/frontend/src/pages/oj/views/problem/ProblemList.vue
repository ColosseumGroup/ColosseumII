<template>
  <Row type="flex" :gutter="18">    
    <!-- <Col :span=19> -->
    <Col>
    <Panel shadow>
      <div slot="title">Ongoing Games</div>
      <div slot="extra">
        <ul class="filter">
          <li>
            <span><b>Select Port:</b></span>
            <Dropdown @on-click="selectPort">
              <span>{{query.port}}
                <Icon type="md-arrow-dropdown"></Icon>
              </span>
              <Dropdown-menu slot="list">
                <Dropdown-item name="0">0</Dropdown-item>
                <Dropdown-item name="1">1</Dropdown-item>
                <Dropdown-item name="2">2</Dropdown-item>
                <Dropdown-item name="3">3</Dropdown-item>
              </Dropdown-menu>
            </Dropdown>
          </li>
          <li>
            <span><b>Select Game Type:</b></span>            
            <!-- <Dropdown @on-click="filterByDifficulty"> -->
            <Dropdown @on-click="selectGameType">
              <span>{{query.gameType}}
                <Icon type="md-arrow-dropdown"></Icon>
              </span>
              <Dropdown-menu slot="list">
                <Dropdown-item name="dealer_renju">dealer_renju</Dropdown-item>
                <Dropdown-item name="dealer_poker">dealer_poker</Dropdown-item>
              </Dropdown-menu>
            </Dropdown>
          </li>

          <!-- <li>
            <i-switch size="large" @on-change="handleTagsVisible">
              <span slot="open">Tags</span>
              <span slot="close">Tags</span>
            </i-switch>
          </li> -->
          <!-- <li>
            <Input v-model="query.keyword"
                   @on-enter="filterByKeyword"
                   @on-click="filterByKeyword"
                   placeholder="keyword"
                   icon="ios-search-strong"/>
          </li> -->
          <li>
            <Button type="info" @click="createGame">
              <Icon type="md-add"></Icon>
              Create New Game!
            </Button>
          </li>
        </ul>
      </div>

      <Table style="width: 100%; font-size: 16px;"
             :columns="problemTableColumns"
             :data="problemList"
             ></Table>
             <!-- :loading="loadings.table" -->
             
    </Panel>  
    <!-- <Pagination :total="total" :page-size="limit" @on-change="pushRouter" :current.sync="query.page"></Pagination> -->
    <!-- </Col> -->
    <!-- <Col :span="5"> -->
    <!-- <Panel :padding="10">
      <div slot="title" class="taglist-title">Tags</div> -->
      <!-- <Button v-for="tag in tagList"
              :key="tag.name"
              @click="filterByTag(tag.name)"
              type="ghost"
              :disabled="query.tag === tag.name"
              shape="circle"
              class="tag-btn">{{tag.name}}
      </Button>
      <Button long id="pick-one" @click="pickone">
        <Icon type="shuffle"></Icon>
        Pick one
      </Button> -->
    <!-- </Panel> -->
    <!-- <Spin v-if="loadings.tag" fix size="large"></Spin> -->
    </Col>
  </Row>
</template>

<script>
  import { mapGetters } from 'vuex'
  import api from '@oj/api'
  import utils from '@/utils/utils'
  import { ProblemMixin } from '@oj/components/mixins'
  import Pagination from '@oj/components/Pagination'

  export default {
    name: 'ProblemList',
    mixins: [ProblemMixin],
    components: {
      Pagination
    },
    data () {
      return {
        // tmpdata:[],
        value1: '1',
        tagList: [],
        problemTableColumns:[
          {
              type: 'index',
              width: 60,
              align: 'center'
          },          
          {
            title:'Game ID',
            align:'center',            
            key:'game_ID'
          },
          {
            title:'Game Type',
            align:'center',            
            key:'game_type'
          },
          {
            title:'Players',
            key:'players',
            align:'center'            
          },
          {
            title:'Further Information',
            align:'center',
            render: (h, params) => {
              return h('Button', {
                props: {
                  type: 'info'
                },
                on: {
                  click: () => {
                    // console.log("hi")
                    console.log(params)
                    // console.log(this.problemList[params.index]['game_ID'])
                    this.$router.push({name: 'problem-details', params: {gameID:this.problemList[params.index]['game_ID']}})
                    // this.$router.push({name: 'problem-details', params: {problemID:params.index}})
                  }
                }
              },'More')
            }      
          }
        ],
        // problemTableColumns: [
        //   {
        //     title: '#',
        //     key: '_id',
        //     render: (h, params) => {
        //       return h('Button', {
        //         props: {
        //           type: 'text',
        //           size: 'large'
        //         },
        //         on: {
        //           click: () => {
        //             this.$router.push({name: 'problem-details', params: {problemID: params.row._id}})
        //           }
        //         },
        //         style: {
        //           padding: '2px 0'
        //         }
        //       }, params.row._id)
        //     }
        //   },
        //   {
        //     title: 'Title',
        //     width: '35%',
        //     render: (h, params) => {
        //       return h('Button', {
        //         props: {
        //           type: 'text',
        //           size: 'large'
        //         },
        //         on: {
        //           click: () => {
        //             this.$router.push({name: 'problem-details', params: {problemID: params.row._id}})
        //           }
        //         },
        //         style: {
        //           padding: '2px 0'
        //         }
        //       }, params.row.title)
        //     }
        //   },
        //   {
        //     title: 'Level',
        //     render: (h, params) => {
        //       let t = params.row.difficulty
        //       let color = 'blue'
        //       if (t === 'Low') color = 'green'
        //       else if (t === 'High') color = 'yellow'
        //       return h('Tag', {
        //         props: {
        //           color: color
        //         }
        //       }, params.row.difficulty)
        //     }
        //   },
        //   {
        //     title: 'Total',
        //     key: 'submission_number'
        //   },
        //   {
        //     title: 'AC Rate',
        //     render: (h, params) => {
        //       return h('span', this.getACRate(params.row.accepted_number, params.row.submission_number))
        //     }
        //   }
        // ],
        problemList: [
          // {
          //   game_ID: 1,
          //   game_type: 'dealer_renju',
          //   players: '1/2'
          // },
          // {
          //   game_ID: 2,
          //   game_type: 'dealer_renju',
          //   players: '2/2'
          // },
        ],
        limit: 10,
        total: 0,
        loadings: {
          table: true,
          tag: true
        },
        routeName: '',
        query: {
          keyword: '',
          port: '0',
          gameType: 'dealer_renju',
          tag: '',
          page: 1
        }
      }
    },
    mounted () {
      this.init()
    },
    methods: {
      init (simulate = false) { 
        this.problemList=[]
        this.getProblemList()
        // console.log("tmpdata.data"+tmpdata.data)
        // this.problemList.push(tmpdata[0])
        // console.log(tmpdata)
        this.routeName = this.$route.name
        let query = this.$route.query
        this.query.difficulty = query.difficulty || ''
        this.query.keyword = query.keyword || ''
        this.query.tag = query.tag || ''
        this.query.page = parseInt(query.page) || 1
        if (this.query.page < 1) {
          this.query.page = 1
        }
        // if (!simulate) {
          // this.getTagList()
        // }
        
        // this.getProblemList()
      },
      pushRouter () {
        this.$router.push({
          name: 'problem-list',
          query: utils.filterEmptyValue(this.query)
        })
      },
      getProblemList () {
        console.log("getproblemlistagain!")
        this.problemList=[]
        this.loadings.table = true
        let offset = (this.query.page - 1) * this.limit          
        
        // api.getProblemList().then(res=>{
        //   for(var arr in res.data){
        //     console.log(res.data[arr]['players'])
        //     var length = 0;
        //     for(var key in res.data[arr]['players'])
        //       length++
        //     res.data[arr].players= length
        //     this.problemList.push(res.data[arr])
        //   }          
        // })
        this.total = 0;        
        api.getProblemList().then(res => {
          for(var key in res.data[arr])
            this.total++
          for(var arr in res.data){
            console.log(res.data[arr]['players'])
            var length = 0;
            for(var key in res.data[arr]['players'])
              length++
            res.data[arr].players= length
            this.problemList.push(res.data[arr])
          }   
        this.loadings.table = false
          // this.problemList = res.data.data.results
          // this.problemList = res.data
          // if (this.isAuthenticated) {
          //   this.addStatusColumn(this.problemTableColumns, res.data.data.results)
          // }
        }, res => {
          this.loadings.table = false
        })
      },
      getTagList () {
        api.getProblemTagList().then(res => {
          this.tagList = res.data.data
          this.loadings.tag = false
        }, res => {
          this.loadings.tag = false
        })
      },
      selectPort(port){
        this.query.port = port
      },
      selectGameType(gameType){
        this.query.gameType = gameType
      },
      filterByTag (tagName) {
        this.query.tag = tagName
        this.query.page = 1
        this.pushRouter()
      },
      filterByDifficulty (difficulty) {
        this.query.difficulty = difficulty
        this.query.page = 1
        this.pushRouter()
      },
      filterByKeyword () {
        this.query.page = 1
        this.pushRouter()
      },
      handleTagsVisible (value) {
        if (value) {
          this.problemTableColumns.push(
            {
              title: 'Tags',
              align: 'center',
              width: '200px',
              render: (h, params) => {
                let tags = []
                params.row.tags.forEach(tag => {
                  tags.push(h('Tag', {}, tag))
                })
                return h('div', {
                  style: {
                    margin: '8px 0'
                  }
                }, tags)
              }
            })
        } else {
          this.problemTableColumns.splice(this.problemTableColumns.length - 1, 1)
        }
      },
      createGame () {
        let username = this.$store.state.user.profile.username
        api.createNewGame(username,this.query.port,this.query.gameType)
        this.getProblemList();
        this.$router.push({name: 'problem-list'})
      },
      pickone () {
        api.pickone().then(res => {
          this.$success('Good Luck')
          this.$router.push({name: 'problem-details', params: {problemID: res.data.data}})
        })
      }
    },
    computed: {
      ...mapGetters(['website', 'modalStatus', 'user', 'isAuthenticated', 'isAdminRole']),
      // 跟随路由变化
    },
    watch: {
      '$route' (newVal, oldVal) {
        if (newVal !== oldVal) {
          this.init(true)
        }
      },
      'isAuthenticated' (newVal) {
        if (newVal === true) {
          this.init()
        }
      }
    }
  }
</script>

<style scoped lang="less">
  .taglist-title {
    margin-left: -10px;
    margin-bottom: -10px;
  }

  .tag-btn {
    margin-right: 5px;
    margin-bottom: 10px;
  }

  #pick-one {
    margin-top: 10px;
  }
</style>
