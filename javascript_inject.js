<script type="text/javascript" src="https://sdk.userbase.com/2/userbase.js"></script>
<script type="text/javascript">

//this can only be ran with new username and password
//frozen until ready to test with more users
async function start() { 

  userbase.init({ 
    appId: 'f3dece1f-eb4b-4a40-bab7-bf63746e1c8d'
  })
  
  title.innerText = 'Creating an account...'
  await userbase.signUp({ 
    username: "test_acct",
    password: "test_psswrd"
  })

  title.innerText = 'Opening database...'
  await userbase.openDatabase({
    databaseName: 'demo',
    changeHandler: function (items) {     
      if (items.length) {
        title.innerText = items[0].item
      }
    }
  })

  await userbase.insertItem({
    databaseName: 'demo',
    item: 'Hello world!\n\n<end-to-end encrypted>'
  })

}

//should be pressed first
async function get_user() { 

  userbase.init({ 
    appId: 'f3dece1f-eb4b-4a40-bab7-bf63746e1c8d'
  })
  
  title.innerText = 'Retreiving account...'
  await userbase.signIn({ 
    username: "test_acct",
    password: "test_psswrd"
  })

}

//pressed second
async function push_data() { 

  userbase.init({ 
    appId: 'f3dece1f-eb4b-4a40-bab7-bf63746e1c8d'
  })
  
  title.innerText = 'Opening database...'
  await userbase.openDatabase({
    databaseName: 'demo',
    changeHandler: function (items) {     
      console.log(items)
      post.innerText = items[items.length -1].item	
      for (let i = 0; i < items.length; i++){
	console.log(items[i].itemId, items[i].item)
      }
      if (items.length) {
        title.innerText = items[0].item
      }
    }
  })
 
  //Frozen until we need to add more posts
  //await userbase.insertItem({
  //  databaseName: 'demo',
  //  item: 'Hegel is always around the Corner'
  //})

  await userbase.getDatabases().then((databases) => {
      console.log(databases)
  })

}


// code for the start button
window.addEventListener("DOMContentLoaded", (event) => {
    const button = document.getElementById('btn')
    button.addEventListener('click', function () { 
      button.style.display = 'none'
      if (sessionStorage) sessionStorage.clear()
      start()
    })
    const title = document.getElementById('title')

    const button2 = document.getElementById('btn2')
    button2.addEventListener('click', function () { 
      button2.style.display = 'none'
      if (sessionStorage) sessionStorage.clear()
      get_user()
    })

    const button3 = document.getElementById('btn3')
    button3.addEventListener('click', function () { 
      button3.style.display = 'none'
      if (sessionStorage) sessionStorage.clear()
      push_data()
    })
});
</script>
