const btn = document.getElementById('menu-btn')
const nav = document.getElementById('menu')

btn.addEventListener('click', () => {
    btn.classList.toggle('open')
    nav.classList.toggle('flex')
    nav.classList.toggle('hidden')
})


// Sidebar icon in user dashboard
// const side_btn = document.getElementById('sidebar-menu-btn')
// const side_nav = document.getElementById('side-menu')

// side_btn.addEventListener('click', () => {
//    side_btn.classList.toggle('open')
//    side_nav.classList.toggle('flex')
//    side_nav.classList.toggle('hidden')
//  })


// Get the button
let mybutton = document.getElementById("btn-back-to-top");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (
    document.body.scrollTop > 20 ||
    document.documentElement.scrollTop > 20
  ) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}
// When the user clicks on the button, scroll to the top of the document
mybutton.addEventListener("click", backToTop);

function backToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}


//Check Passwords of User when registering

function checkuserpass()
{
    if(document.usersignup.userpass.value!=document.usersignup.userrepass.value)
    {
        alert('Passwords not matching..!');
        document.usersignup.userrepass.focus();
        return false;
    }
    return true;
}

//Check Passwords of Department When Registering

function checkPassword()
{
    if(document.depsignup.pass.value!=document.depsignup.repass.value)
      {
        alert('Passwords not matching !');
        document.depsignup.repass.focus();
        return false;
      }
      return true;
}


// side bar opening and closing 


   function Close(){
     document.querySelector('.sidebar').classList.toggle('hidden');
   }

   function Open(){
     //document.getElementById('sidebar').style.left='270px';
     document.querySelector('.sidebar').classList.toggle('flex');
   }

   // content changing when sidebar appears on user dashboard

  //  $(function(){
  //     $('#side-menu-btn').on('click', function(){
  //         $('#side-menu-btn,#user_content').toggleClass('active');
  //     });

  //  });


