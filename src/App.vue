<template>
    <div>
        <h1 >KioDoc</h1>
        <p v-if="state.num == 1">Doctor Login</p>
        <input v-if="state.num == 1" name="FirstName" type="text" placeholder="username"></input>
        <input v-if="state.num == 1"  name="Password" type="password" placeholder="password"></input>
        <button v-if="state.num == 1" v-on:click="login()">Doctor Login</button>
        <h1 v-if="state.num == 2">Welcome to the KioDoc Doctor Console</h1>
        <button v-if="state.num == 2" v-on:click="chat()">Click Here to Talk to Next Patient</button>
        <p v-if="state.num == 3">Patient Info:<br />Heart Rate: 80 BPM<br />Temperature: 37C<br /></p>
        <textarea v-model="message" v-if="state.num == 3" placeholder="type message here"></textarea>
        <button v-if="state.num == 3" >Click Here to Send Message</button>
        <br />
        <br />
        <p v-html="messages" v-if="state.num == 3" ref="messages">Doctor: {{message}}</p>
        


    </div>

</template>

<script lang='ts'>
import Vue from 'vue';
// import socketio from 'socket.io';
// import VueSocketIO from 'vue-socket.io';
// // import request from "request";

// declare module 'vue/types/vue' {
//   interface Vue {
//     sockets: any;
//   }
// }

// declare module 'vue/types/options' {
//   interface ComponentOptions<V extends Vue> {
//     sockets?: any;
//   }
// }

export type State = {
  value: string,
  num: number
};

export type ReturnVue = {
  state: State,
  isConnected: boolean,
  socketMessage: string
}

let returnVal : ReturnVue;

let sockMessage : string;

const state: State = {
  value: "",
  num: 1
};

// export const SocketInstance = socketio('http://localhost:8765');
// Vue.use(VueSocketIO, SocketInstance)



function login() {
  state.num = 2;
}

function chat() {
  state.num = 3;
  // socket = new WebSocket("wss://10.245.33.58:8765")
  // while(socket.readyState != 1);
  // socket.send("Doctor Connected")
  // console.log("connected?")
}

export default Vue.extend({
  methods: { login : login,
              chat : chat },
  data: function() {
    return {
      state: state,
      // socket : socket,
      isConnected: false,
      socketMessage : '',
      messages: null
    };
  }

  // sockets: {
  //   connect() {
  //     // Fired when the socket connects.
  //     this.isConnected = true;
  //   },

  //   disconnect() {
  //     this.isConnected = false;
  //   },

  //   // Fired when the server sends something on the "messageChannel" channel.
  //   messageChannel(data:string) {
  //     this.socketMessage = data
  //   }
  // }
});
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1 {
  font-size: 3em;
  color: black;
  text-align: center;
  margin: 0.5em;
  text-shadow: 3px 2px black;
}
</style>
