<script type="text/javascript" src="https://sdk.userbase.com/2/userbase.js"></script>
<script type="text/javascript">
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

async function return() { 

  userbase.init({ 
    appId: 'f3dece1f-eb4b-4a40-bab7-bf63746e1c8d'
  })
  
  title.innerText = 'Retreiving account...'
  await userbase.signIn({ 
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

    const button = document.getElementById('btn2')
    button.addEventListener('click', function () { 
      button.style.display = 'none'
      if (sessionStorage) sessionStorage.clear()
      return()
    })
});
</script>
