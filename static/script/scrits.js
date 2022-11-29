i=0;
function btt(){
    let block = document.getElementById('block');
    let node = document.createElement('div');
    let textnode = document.createTextNode('Série');
    node.appendChild(textnode);
    block.appendChild(node);
    node.classList.add("blocks");
}

function add(id){
    let tadd = document.getElementById(id+'--ep')
    ep = parseInt(tadd.innerHTML);
    ep += 1;
    tadd.innerHTML = ep;
    }

function sub(id){
    let tadd = document.getElementById(id+'--ep')
    ep = parseInt(tadd.innerHTML);
    if (ep > 0){
        ep -= 1;
        tadd.innerHTML = ep;
    }    
    }
//let card = document.getElementById("{{name['id']}}-card");

//card.addEventListener("mouseout",function(){
  //      card.style.color = "white";
        
//});
//card.addEventListener("mouseover",function(){
      //  card.style.color = "grey";
       // alert("you on")
//});

document.querySelectorAll('.card-header').forEach(item => {
    item.addEventListener('click', event => {
      //handle click 
        idstr =   item.id     
        id = idstr.substring(0,(idstr.length-5))
        console.log(id)
        document.getElementById(id).submit();
    })
  })

