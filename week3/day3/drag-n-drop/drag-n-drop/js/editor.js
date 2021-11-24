const _imgs = [
  {
   src: 'images/img-1.jpg',
   desc: 'Image 1 description'
  },
  {
    src: 'images/img-2.jpg',
    desc: 'Image 2 description'
  },
  {
    src: 'images/img-3.jpg',
    desc: 'Image 3 description'
  }
];

let _current_drag_obj;
let _current_drag_target;

function init() {
  document.getElementById('sidebar-content').style.height = screen.height+"px";
  loadImages();
  loadEvents();
}

function loadImages() {
  let _ul = document.querySelector('ul#img-list');
  for(var x in _imgs) {
    var _li = document.createElement('li');
    var _img = document.createElement('img');
    var _p = document.createElement('p');

    _li.setAttribute('draggable','true');

    _p.innerText = _imgs[x].desc;

    _img.setAttribute('src', _imgs[x].src);
    _img.setAttribute('alt', _imgs[x].desc);
    _img.setAttribute('ondrag','drag(this,event)');

    _li.appendChild(_p);
    _li.appendChild(_img);
    _ul.appendChild(_li);
  }
}

function loadEvents(){
  let _btn = document.getElementById('submit-button');
  let _frm = document.forms['frm'];

  _btn.addEventListener("click", function(event) {
      // alert(_frm); debug
      if(validate(_frm)){
        // alert(_frm.elements[0].value + " " + _frm.elements[1].value);
        document.getElementById('h-title').innerText =  _frm.elements[0].value;
        document.getElementById('p-contnet').innerText =  _frm.elements[1].value;
      }
  });

  let _drop_targets = document.getElementsByClassName("drop-target");

  document.addEventListener("dragend", function(event) {
    if(_current_drag_target){
      _current_drag_target.replaceChild(_current_drag_obj.cloneNode(true), _current_drag_target.childNodes[0]);
    }
  });

  for(var i = 0; i < _drop_targets.length; i++){
    let _target =_drop_targets[i];
    _target.addEventListener("dragenter", function(event) {
        _current_drag_target = _target;
    });
    _target.addEventListener("dragleave", function(event) {
      //  _current_drag_target = null;
    });
  }

}

function validate(_form) {
  let _title = _form.elements[0].value;
  let _content = _form.elements[1].value;
  if( _title.trim() == "" || _content.trim() == ""){
    alert("Title Or Content is empty...");
    return false;
  }
  return true;
}

function drag(obj, event){
  _current_drag_obj = obj;
}
