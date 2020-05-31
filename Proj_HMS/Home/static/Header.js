document.write(`<nav id = navsticky>

<div id='alert'>

        {% if messages %}
            {% for message in messages %} 
                <script>
                    document.getElementById('alert').innerHTML='<p class =" alert   ">{{message}}</p>'; 
                    setTimeout(function() {
                        document.getElementById('alert').innerHTML='';
                        },3000);
                </script>     
            {% endfor %}
        {% endif %}
    </div>  
    <div class="logo">
        <h4>HMS</h4>
    </div>
    
    <!-- For navbar-->
    <ul class="navbar">

    
        
        <li><a href="index.html">Home</a></li>
        <li><a href="index.html#aboutus">Services</a></li>
        <li><a href="index.html#contactus">Contact us</a></li>
        <li><a href="Login.html">Login</a></li>
    </ul>
   <!--For making three lines at place of navbar-->
    <div class="burger">
        <div class="line1"></div>
        <div class="line2"></div>
        <div class="line3"></div>
    </div>
   
</nav>`);